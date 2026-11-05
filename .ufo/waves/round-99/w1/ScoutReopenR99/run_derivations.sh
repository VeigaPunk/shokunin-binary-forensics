#!/bin/sh
# ScoutReopenR99 — re-run every deriving command of the candidate's `### Derivation table`
# exactly as written (markdown `\|` unescaped to `|`), from the lane root.
set -u
LANE=/home/vgpnk/Projects/shokunin/revenger-shokunin
OUT=/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-99/w1/ScoutReopenR99/derivations.log
cd "$LANE" || { echo "cd failed" >&2; exit 9; }
DOCTOR=corpus/live/runs/round-98/rea-doctor-r98.txt
INSPECT=corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt
SC='sed -n '"'"'/^scope_checks/,/^informational_checks/p'"'"''
{
echo "# derivations re-run 2026-11-05 from lane root: $LANE"
echo

echo '== D01 doctor verdict lines'
echo '$ sed -n 1,2p corpus/live/runs/round-98/rea-doctor-r98.txt'
sed -n 1,2p $DOCTOR
echo "rc=$?"

echo
echo '== D02a scope-check count ok:true'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -c '    ok: true'"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -c '    ok: true'
echo "rc=$?"

echo
echo '== D02b scope-check count ok:false'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -c '    ok: false'"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -c '    ok: false'
echo "rc=$?"

echo
echo '== D03 scope-check classes'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -oE 'classification: [a-z_]+' | sort | uniq -c"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -oE 'classification: [a-z_]+' | sort | uniq -c
echo "rc=$?"

echo
echo '== D04 registration states'
echo "$ awk '/^    - client:/{c=\$3} /^      state:/{print c, \$2}' corpus/live/runs/round-98/rea-doctor-r98.txt"
awk '/^    - client:/{c=$3} /^      state:/{print c, $2}' $DOCTOR
echo "rc=$?"

echo
echo '== D05 client registration count'
echo "$ grep -c '^    - client:' corpus/live/runs/round-98/rea-doctor-r98.txt"
grep -c '^    - client:' $DOCTOR
echo "rc=$?"

echo
echo '== D06 registration state split'
echo "$ awk '/^    - client:/{c=\$3} /^      state:/{print \$2}' corpus/live/runs/round-98/rea-doctor-r98.txt | sort | uniq -c"
awk '/^    - client:/{c=$3} /^      state:/{print $2}' $DOCTOR | sort | uniq -c
echo "rc=$?"

echo
echo '== D07 missing-or-stale registrations'
echo "$ awk '/^    - client:/{c=\$3} /^      state:/{print \$2}' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -cE '^(missing|stale)$'"
awk '/^    - client:/{c=$3} /^      state:/{print $2}' $DOCTOR | grep -cE '^(missing|stale)$'
echo "rc=$?"

echo
echo '== D08 ghidra scope checks healthy'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -A1 '^  - name: ghidra' | grep -c '    ok: true'"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -A1 '^  - name: ghidra' | grep -c '    ok: true'
echo "rc=$?"

echo
echo '== D09 ghidra scope-check names'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -oE '^  - name: ghidra[a-z_-]*' | sed 's/^  - name: //' | paste -sd' '"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -oE '^  - name: ghidra[a-z_-]*' | sed 's/^  - name: //' | paste -sd' '
echo "rc=$?"

echo
echo '== D10 doctor-printed ghidra and java versions'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -A3 -E '^  - name: ghidra-(version|java)$' | grep 'detail:'"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -A3 -E '^  - name: ghidra-(version|java)$' | grep 'detail:'
echo "rc=$?"

echo
echo '== D11 engine and jadx classifications'
echo "$ sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -A3 -E '^  - name: (hopper|ida-registration|kuna-installation|jadx)$' | grep -E 'name:|classification:' | paste - - | sed -E 's/^ *- name: //; s/\t *classification: / /'"
sed -n '/^scope_checks/,/^informational_checks/p' $DOCTOR | grep -A3 -E '^  - name: (hopper|ida-registration|kuna-installation|jadx)$' | grep -E 'name:|classification:' | paste - - | sed -E 's/^ *- name: //; s/\t *classification: / /'
echo "rc=$?"

echo
echo '== D12 installation paths count'
echo "$ grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt | sed 's/^    paths\[3\]: //' | tr ',' '\n' | grep -c ."
grep '^    paths\[3\]: ' $DOCTOR | sed 's/^    paths\[3\]: //' | tr ',' '\n' | grep -c .
echo "rc=$?"

echo
echo '== D13 installation state'
echo "$ grep -c '^    state: multiple' corpus/live/runs/round-98/rea-doctor-r98.txt"
grep -c '^    state: multiple' $DOCTOR
echo "rc=$?"

echo
echo '== D14 CLI package version'
echo "$ grep cli_package_version corpus/live/runs/round-98/rea-doctor-r98.txt"
grep cli_package_version $DOCTOR
echo "rc=$?"

echo
echo '== D15 inventory Evidence ID'
echo "$ grep -m1 evidence_id corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt"
grep -m1 evidence_id $INSPECT
echo "rc=$?"

echo
echo '== D16 inventory substep status'
echo "$ grep -m1 'status: completed' corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt"
grep -m1 'status: completed' $INSPECT
echo "rc=$?"

echo
echo '== D17 inventory member sizes'
echo "$ grep -E 'declared_size: ' corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt | sed 's/^ *//'"
grep -E 'declared_size: ' $INSPECT | sed 's/^ *//'
echo "rc=$?"

echo
echo '== D18 fixture digest'
echo '$ sha256sum corpus/fixtures/archive-r2/fixture.zip'
sha256sum corpus/fixtures/archive-r2/fixture.zip
echo "rc=$?"

echo
echo '== D19 record file digests'
echo '$ sha256sum corpus/live/runs/round-98/*'
sha256sum corpus/live/runs/round-98/*
echo "rc=$?"

echo
echo '== D20 S506 body digest'
echo '$ sha256sum reports/round-98/quote-receipts/raw/S506.body'
sha256sum reports/round-98/quote-receipts/raw/S506.body
echo "rc=$?"

echo
echo '== D21 S506 body length'
echo '$ wc -c < reports/round-98/quote-receipts/raw/S506.body'
wc -c < reports/round-98/quote-receipts/raw/S506.body
echo "rc=$?"
} > "$OUT" 2>&1
echo "written $OUT"
