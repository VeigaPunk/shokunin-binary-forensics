#!/usr/bin/env bash
# VoterBlindR99 derivation re-run. Read-only. All commands verbatim from the
# candidate entry's derivation table (markdown \| unescaped) plus prose checks.
cd /home/vgpnk/Projects/shokunin/revenger-shokunin || exit 9
DOC=corpus/live/runs/round-98/rea-doctor-r98.txt
EV=corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt

run() { printf '\n$ %s\n' "$1"; bash -c "$1"; printf '[rc=%d]\n' "$?"; }

echo '=== D1 doctor verdict lines ==='
run "sed -n 1,2p $DOC"
echo '=== D2 scope-check ok:true / ok:false counts ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -c '    ok: true'"
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -c '    ok: false'"
echo '=== D3 scope-check classes ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -oE 'classification: [a-z_]+' | sort | uniq -c"
echo '=== D4 registration states (pairs) ==='
run "awk '/^    - client:/{c=\$3} /^      state:/{print c, \$2}' $DOC"
echo '=== D5 client registration count ==='
run "grep -c '^    - client:' $DOC"
echo '=== D6 registration state split ==='
run "awk '/^    - client:/{c=\$3} /^      state:/{print \$2}' $DOC | sort | uniq -c"
echo '=== D7 missing-or-stale count ==='
run "awk '/^    - client:/{c=\$3} /^      state:/{print \$2}' $DOC | grep -cE '^(missing|stale)$'"
echo '=== D8 ghidra scope checks healthy ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -A1 '^  - name: ghidra' | grep -c '    ok: true'"
echo '=== D9 ghidra scope-check names ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -oE '^  - name: ghidra[a-z_-]*' | sed 's/^  - name: //' | paste -sd' '"
echo '=== D10 doctor-printed ghidra and java versions ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -A3 -E '^  - name: ghidra-(version|java)\$' | grep 'detail:'"
echo '=== D11 engine and jadx classifications ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -A3 -E '^  - name: (hopper|ida-registration|kuna-installation|jadx)\$' | grep -E 'name:|classification:' | paste - - | sed -E 's/^ *- name: //; s/\t *classification: / /'"
echo '=== D12 installation paths count ==='
run "grep '^    paths\[3\]: ' $DOC | sed 's/^    paths\[3\]: //' | tr ',' '\n' | grep -c ."
echo '=== D12b the paths line itself ==='
run "grep -n 'paths\[3\]: ' $DOC"
echo '=== D13 installation state ==='
run "grep -c '^    state: multiple' $DOC"
echo '=== D14 CLI package version ==='
run "grep cli_package_version $DOC"
echo '=== D15 inventory Evidence ID ==='
run "grep -m1 evidence_id $EV"
echo '=== D16 inventory substep status ==='
run "grep -m1 'status: completed' $EV"
echo '=== D17 inventory member sizes ==='
run "grep -E 'declared_size: ' $EV | sed 's/^ *//'"
echo '=== D18 fixture digest ==='
run "sha256sum corpus/fixtures/archive-r2/fixture.zip"
echo '=== D19 record file digests ==='
run "sha256sum corpus/live/runs/round-98/*"
echo '=== D20 S506 body digest ==='
run "sha256sum reports/round-98/quote-receipts/raw/S506.body"
echo '=== D21 S506 body length ==='
run "wc -c < reports/round-98/quote-receipts/raw/S506.body"

echo '=== P1 doctor record has no binwalk/unblob check ==='
run "grep -cE 'binwalk|unblob' $DOC"
echo '=== P2 jadx detail quote in doctor record ==='
run "grep -nF \"This checks configuration, not whether a selected APK fits in the worker's memory.\" $DOC"
echo '=== P3 all scope-check name+classification pairs (skill identity check) ==='
run "sed -n '/^scope_checks/,/^informational_checks/p' $DOC | grep -A1 '^  - name:' | paste - - | sed -E 's/^ *- //'"
echo '=== P4 ghidra-installation detail (headless launcher location) ==='
run "grep -A3 '^  - name: ghidra-installation\$' $DOC"
echo '=== P5 no rc= lines inside doctor record (exit codes are session observations) ==='
run "grep -c 'rc=' $DOC"
run "grep -c 'rc=' $EV"
echo '=== P6 S506 body numbered lines 28-40 (paraphrase line attribution) ==='
run "awk 'NR>=28 && NR<=40 {printf \"%d|%s\n\", NR, \$0}' reports/round-98/quote-receipts/raw/S506.body"
echo '=== P7 fetch-log S506 row ==='
run "grep -n 'S506' reports/round-98/quote-receipts/fetch-log.md"
echo '=== P8 K05 row of the 2026-10-12 checklist ==='
run "grep -n 'K05' corpus/knowledge/2026-10-12-rea-readiness-checklist.md"
echo '=== P9 truth.json (ZIP expectation source, fixed round 2) ==='
run "cat corpus/fixtures/archive-r2/truth.json"
echo '=== P10 evidence_id / provider / operation lines in inspect record ==='
run "grep -nE 'provider|operation|evidence_id|status:|declared_size|path:' $EV"
