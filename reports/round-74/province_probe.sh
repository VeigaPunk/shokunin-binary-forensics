#!/usr/bin/env bash
# revenger r74 — coverage criterion P: province surface probe.
# Every surface PROVINCE.md names must either (a) verify present by probe on
# this host, or (b) carry a dated absent record in PROVINCE.md. Anything else
# prints UNRECORDED-ABSENT and exits 1.
# Usage: bash reports/round-74/province_probe.sh [LANE_DIR]  (default: repo root
# inferred from this script's location).
set -u
L=$(cd "$(dirname "$0")/../.." && pwd)
[ "${1:-}" = "" ] || L=$1
P="$L/PROVINCE.md"
[ -f "$P" ] || { echo "PROVINCE not found: $P"; exit 2; }
fail=0
unresolved=0

check() { # <name> <absent-marker-in-PROVINCE.md> <probe...>
  local name=$1 marker=$2; shift 2
  if "$@" >/dev/null 2>&1; then
    printf '%-28s PRESENT (probe exit 0)\n' "$name"
  elif grep -qF -- "$marker" "$P"; then
    printf '%-28s ABSENT-RECORDED (dated marker in PROVINCE.md)\n' "$name"
  else
    printf '%-28s UNRECORDED-ABSENT\n' "$name"
    unresolved=$((unresolved + 1))
    fail=1
  fi
}

REA_DIR="$HOME/.agents/skills/reverse-engineer-anything"
check "rea-skill-dir"       "[absent on this host, 2026-10-31" bash -c "[ -d \"$REA_DIR\" ]"
check "rea-cli"             "[absent on this host, 2026-10-31" rea --version
check "npx-fallback"        "[absent on this host, 2026-10-31" npx --version
check "engine-ghidra"       "[absent on this host, 2026-10-31: ghidra" bash -c "command -v ghidra || command -v analyzeHeadless"
check "engine-ida"          "[absent on this host, 2026-10-31: ida"    bash -c "command -v ida || command -v ida64"
check "engine-jadx"         "[absent on this host, 2026-10-31: jadx"   command -v jadx
check "engine-binwalk"      "[absent on this host, 2026-10-31: binwalk" bash -c "command -v binwalk || command -v unblob"
check "engine-pwntools"     "[absent on this host, 2026-10-31: pwntools" python -c "import pwn"
check "demand-context"      "[absent on this host, 2026-10-31" bash -c "[ -d \"$HOME/Projects/gamez/research\" ]"
check "bounty-triage-module" "[absent on this host, 2026-10-31" bash -c "[ -f \"$L/corpus/training/bounty-triage/MODULE.md\" ]"
check "lane-repo"           "shokunin-binary-forensics" bash -c "[ -d \"$L/.git\" ]"

total=11
resolved=$((total - unresolved))
score=$(python -c "print(f'{10*($resolved)/$total:.1f}')")
printf 'PROVINCE_SURFACES_RESOLVED=%d/%d UNRECORDED_ABSENT=%d P_SCORE=%s\n' "$resolved" "$total" "$unresolved" "$score"
[ "$fail" = 0 ]
