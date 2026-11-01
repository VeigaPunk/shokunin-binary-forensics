#!/usr/bin/env bash
# revenger r75 — coverage criterion P2: province surface probe, revision 2.
#
# Supersedes reports/round-74/province_probe.sh (v1) for the criterion's
# measuring instrument. v1's engine probes were PATH-only, so an off-PATH
# install made a false "absent" record pass as ABSENT-RECORDED: ghidra
# 12.1.4 sat at C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC since 2026-10-26
# while v1 printed engine-ghidra ABSENT-RECORDED on 2026-10-31 (exit 0).
# v2 semantics per surface:
#   probe present + that surface's absent-record token in PROVINCE.md -> STALE-RECORD (fail)
#   probe present, no absent-record token                             -> PRESENT (ok)
#   probe absent  + absent-record token present                       -> ABSENT-RECORDED (ok)
#   probe absent  + no absent-record token                            -> UNRECORDED-ABSENT (fail)
# v1's absent markers were one shared generic string consulted only on
# probe-failure; the STALE branch consults them on probe-success, so each
# surface needs its OWN token. Surfaces with no absent-record vocabulary yet
# use a dedicated sentinel token (written only if that surface is ever
# recorded absent): [absent on this host: rea-cli] etc.
# Engine probes look beyond PATH: the host tools convention (~/tools/<name>*)
# and, for ida, /c/Program Files. Presence is not readiness (Q05).
# Usage: bash reports/round-75/province_probe2.sh [LANE_DIR]
set -u
L=$(cd "$(dirname "$0")/../.." && pwd)
[ "${1:-}" = "" ] || L=$1
P="$L/PROVINCE.md"
[ -f "$P" ] || { echo "PROVINCE not found: $P"; exit 2; }
fail=0
unresolved=0
stale=0

check() { # <name> <absent-marker-in-PROVINCE.md> <probe...>
  local name=$1 marker=$2; shift 2
  if "$@" >/dev/null 2>&1; then
    if grep -qF -- "$marker" "$P"; then
      printf '%-28s STALE-RECORD (surface present on host; PROVINCE.md still records it absent)\n' "$name"
      stale=$((stale + 1))
      fail=1
    else
      printf '%-28s PRESENT (probe exit 0)\n' "$name"
    fi
  elif grep -qF -- "$marker" "$P"; then
    printf '%-28s ABSENT-RECORDED (dated marker in PROVINCE.md)\n' "$name"
  else
    printf '%-28s UNRECORDED-ABSENT\n' "$name"
    unresolved=$((unresolved + 1))
    fail=1
  fi
}

REA_DIR="$HOME/.agents/skills/reverse-engineer-anything"
TOOLS="$HOME/tools"
check "rea-skill-dir"       "[absent on this host, 2026-10-31 — the packaged" bash -c "[ -d \"$REA_DIR\" ]"
check "rea-cli"             "[absent on this host: rea-cli]" rea --version
check "npx-fallback"        "[absent on this host: npx]" npx --version
check "engine-ghidra"       "[absent on this host, 2026-10-31: ghidra" bash -c "command -v ghidra || command -v analyzeHeadless || ls \"$TOOLS\"/ghidra_*/support/analyzeHeadless.* >/dev/null 2>&1"
check "engine-ida"          "[absent on this host, 2026-10-31: ida"    bash -c "command -v ida || command -v ida64 || ls \"$TOOLS\"/ida* >/dev/null 2>&1 || ls \"/c/Program Files/IDA\"* >/dev/null 2>&1"
check "engine-jadx"         "[absent on this host, 2026-10-31: jadx"   bash -c "command -v jadx || ls \"$TOOLS\"/jadx* >/dev/null 2>&1"
check "engine-binwalk"      "[absent on this host, 2026-10-31: binwalk" bash -c "command -v binwalk || command -v unblob || python -c 'import binwalk' || python -c 'import unblob'"
check "engine-pwntools"     "[absent on this host, 2026-10-31: pwntools" python -c "import pwn"
check "demand-context"      "[absent on this host, 2026-10-31 — no ~/Projects tree exists]" bash -c "[ -d \"$HOME/Projects/gamez/research\" ]"
check "bounty-triage-module" "[absent on this host: bounty-triage module]" bash -c "[ -f \"$L/corpus/training/bounty-triage/MODULE.md\" ]"
check "lane-repo"           "[absent on this host: lane repo]" bash -c "[ -d \"$L/.git\" ]"

total=11
resolved=$((total - unresolved - stale))
score=$(python -c "print(f'{10*($resolved)/$total:.1f}')")
printf 'P2_SURFACES_RESOLVED=%d/%d UNRECORDED_ABSENT=%d STALE_RECORDS=%d P2_SCORE=%s\n' "$resolved" "$total" "$unresolved" "$stale" "$score"
[ "$fail" = 0 ]
