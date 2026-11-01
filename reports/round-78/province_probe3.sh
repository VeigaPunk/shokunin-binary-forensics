#!/usr/bin/env bash
# revenger r78 — coverage criterion P3: province surface probe, revision 3.
#
# Supersedes reports/round-75/province_probe2.sh (v2) as the criterion's
# measuring instrument. Carries the r77 non-author spotcheck routed item and
# the r77 lesson "Routed forward" note: v2's surface list predates the browser
# surface, so a stale or unrecorded browser-surface record was invisible to it
# by construction (v2 is a fixed token list). v3 carries the eleven v2 checks
# byte-identically and adds a twelfth surface, cdp-browser, with its own
# dedicated absent-sentinel token (the r75 per-surface-token rule: each
# surface's marker is written only if that surface is ever recorded absent).
# Presence is not readiness (Q05): the probe resolves the recorded browser
# binaries exactly as the engine rows resolve theirs.
# v3 semantics per surface (unchanged from v2):
#   probe present + that surface's absent-record token in PROVINCE.md -> STALE-RECORD (fail)
#   probe present, no absent-record token                             -> PRESENT (ok)
#   probe absent  + absent-record token present                       -> ABSENT-RECORDED (ok)
#   probe absent  + no absent-record token                            -> UNRECORDED-ABSENT (fail)
# Usage: bash reports/round-78/province_probe3.sh [LANE_DIR]
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
# twelfth surface (r78): the loopback CDP browser surface recorded PRESENT in
# PROVINCE.md since r77 (S447). The sentinel token below is written into
# PROVINCE.md only if that surface is ever recorded absent.
check "cdp-browser"         "[absent on this host: cdp-browser]" bash -c "[ -f \"/c/Program Files/Google/Chrome/Application/chrome.exe\" ] || [ -f \"/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe\" ]"

total=12
resolved=$((total - unresolved - stale))
score=$(python -c "print(f'{10*($resolved)/$total:.1f}')")
printf 'P3_SURFACES_RESOLVED=%d/%d UNRECORDED_ABSENT=%d STALE_RECORDS=%d P3_SCORE=%s\n' "$resolved" "$total" "$unresolved" "$stale" "$score"
[ "$fail" = 0 ]
