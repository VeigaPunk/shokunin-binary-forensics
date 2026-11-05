#!/usr/bin/env bash
# VoterGateR99 — re-run every derivation-table command of the C14 candidate
# against the saved round-98 records and diff against the entry's recorded output.
# Read-only. Scratch receipts go to $S.
S=/fast/scratch/hyaku/revenger-r99/VoterGateR99
cd /home/vgpnk/Projects/shokunin/revenger-shokunin || exit 9
D=corpus/live/runs/round-98/rea-doctor-r98.txt
I=corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt
P=corpus/live/runs/round-98/host-probes-r98.txt
pass=0; fail=0
norm() { printf '%s' "$1" | sed -E 's/^[[:space:]]+//; s/[[:space:]]+$//; s/[[:space:]]+/ /g'; }
chk() { # name expected actual
  if [ "$(norm "$2")" = "$(norm "$3")" ]; then echo "OK   $1"; pass=$((pass+1));
  else echo "FAIL $1"; echo "--- expected ---"; printf '%s\n' "$2"; echo "--- actual ---"; printf '%s\n' "$3"; fail=$((fail+1)); fi
}

a=$(sed -n 1,2p "$D"); chk "doctor-verdict-lines" "healthy: false
environment_healthy: false" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -c '    ok: true'); chk "scope-ok-true=11" "11" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -c '    ok: false'); chk "scope-ok-false=13" "13" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -oE 'classification: [a-z_]+' | sort | uniq -c); chk "scope-classes" "10 config_drift
11 healthy
3 missing_analysis_engine" "$a"
a=$(grep -c '^    - client:' "$D"); chk "client-count=14" "14" "$a"
a=$(awk '/^    - client:/{c=$3} /^      state:/{print $2}' "$D" | sort | uniq -c); chk "state-split" "4 aligned
1 manual
8 missing
1 stale" "$a"
a=$(awk '/^    - client:/{c=$3} /^      state:/{print c, $2}' "$D"); chk "reg-states" "antigravity missing
claude_code missing
codex aligned
copilot_cli missing
cursor missing
devin aligned
gemini_cli missing
grok_bot manual
grok_build aligned
kimi missing
omp stale
opencode missing
pi missing
zcode aligned" "$a"
a=$(awk '/^    - client:/{c=$3} /^      state:/{print $2}' "$D" | grep -cE '^(missing|stale)$'); chk "missing-or-stale=9" "9" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -A1 '^  - name: ghidra' | grep -c '    ok: true'); chk "ghidra-healthy=8" "8" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -oE '^  - name: ghidra[a-z_-]*' | sed 's/^  - name: //' | paste -sd' '); chk "ghidra-names" "ghidra ghidra-platform ghidra-architecture ghidra-installation ghidra-version ghidra-headless ghidra-native_decompiler ghidra-java" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -A3 -E '^  - name: ghidra-(version|java)$' | grep 'detail:'); chk "doctor-versions" "detail: 12.1.4
detail: 21.0.13; 64-bit; JDK; /usr/lib/jvm/java-21-openjdk; accepted a 64-bit full JDK 21 or newer" "$a"
a=$(sed -n '/^scope_checks/,/^informational_checks/p' "$D" | grep -A3 -E '^  - name: (hopper|ida-registration|kuna-installation|jadx)$' | grep -E 'name:|classification:' | paste - - | sed -E 's/^ *- name: //; s/\t *classification: / /'); chk "engine-jadx" "hopper missing_analysis_engine
ida-registration missing_analysis_engine
jadx healthy
kuna-installation missing_analysis_engine" "$a"
a=$(grep '^    paths\[3\]: ' "$D" | sed 's/^    paths\[3\]: //' | tr ',' '\n' | grep -c .); chk "install-paths=3" "3" "$a"
a=$(grep '^    paths\[3\]: ' "$D"); echo "INFO install-paths raw line: $a"
a=$(grep -c '^    state: multiple' "$D"); chk "install-state=1" "1" "$a"
a=$(grep cli_package_version "$D"); chk "cli-version" "cli_package_version: 6.7.0" "$a"
a=$(grep -m1 evidence_id "$I"); chk "evidence-id" "evidence_id: ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382" "$a"
a=$(grep -m1 'status: completed' "$I"); chk "substep-status" "status: completed" "$a"
a=$(grep -E 'declared_size: ' "$I" | sed 's/^ *//'); chk "member-sizes" "declared_size: 2964
declared_size: 84
declared_size: 16160" "$a"
a=$(sha256sum corpus/fixtures/archive-r2/fixture.zip | cut -d' ' -f1); chk "fixture-digest" "857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e" "$a"
a=$(sha256sum "$P" | cut -d' ' -f1 | cut -c1-8); chk "probes-digest-prefix" "94eaa6ff" "$a"
a=$(sha256sum "$D" | cut -d' ' -f1 | cut -c1-8); chk "doctor-digest-prefix" "fb9a4824" "$a"
a=$(sha256sum "$I" | cut -d' ' -f1 | cut -c1-8); chk "inspect-digest-prefix" "c373f656" "$a"
a=$(python3 -c "import json;d=json.load(open('corpus/fixtures/archive-r2/truth.json'));print(d['archive_sha256']==open('corpus/fixtures/archive-r2/fixture.zip','rb').read() and '' or 'x')" ; sha256sum corpus/fixtures/archive-r2/fixture.zip | grep -c 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e); chk "fixture-matches-truth-json" "1" "$(echo "$a" | tail -n1)"
echo "SUMMARY pass=$pass fail=$fail"
