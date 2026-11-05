#!/bin/sh
# Commands actually run by seat ConnectorOverlap (2026-11-05) to produce measurement.tsv.
# Read-only: git show extracts committed bytes to scratch; no lane or sibling file is modified.
set -eu

LANE=/home/vgpnk/Projects/shokunin/revenger-shokunin
R=02050cb2a6758e3bd9cec696ff0e42df6f23511a   # round-93 freeze commit
S=${HYAKU_SCRATCH:-/fast/scratch/hyaku}/revenger-r93/ConnectorOverlap
mkdir -p "$S/bytes"

# 1. Extract the committed bytes every verdict is read from (at the r93 freeze tip; claims files are frozen and never change after their freeze).
for f in \
  reports/round-89/claims.md reports/round-90/claims.md reports/round-91/claims.md reports/round-92/claims.md \
  SCORECARD.md \
  corpus/lessons/round-89.md corpus/lessons/round-90.md corpus/lessons/round-91.md corpus/lessons/round-92.md \
  corpus/lessons/round-89-verifier-spotcheck.md corpus/lessons/round-90-verifier-spotcheck.md \
  corpus/lessons/round-91-verifier-spotcheck.md corpus/lessons/round-92-verifier-spotcheck.md
do
  git -C "$LANE" show "$R:$f" > "$S/bytes/$(printf '%s' "$f" | tr '/' '_')"
done

# 2. Verdict lines (grep -niE over the extracted bytes; per-file line numbers feed measurement.tsv).
grep -niE 'met.contested|not verified|not-verified|killed|honest stop|rejected-honest|C1_VERDICT|C2_VERDICT|verdict:' "$S/bytes" ||
true
# Scorecard section headers (section ranges: r88 :1524, r89 :1588, r90 :1649, r91 :1674, r92 :1705):
grep -nE '^## Round (8[89]|9[0-3])' "$S/bytes/SCORECARD.md" || true

# 3. The stale-heading contradiction the rate must not inherit (r91 D2 correction of record lives in the r92 section):
grep -n 'Correction row (r91 D2)' "$S/bytes/SCORECARD.md" || true

# 4. Running rate from measurement.tsv (exercised; output also echoed into the report).
awk -F '\t' '
  /^r8[9]|^r9[0-2]/ { n++; if ($5 !~ /^clean/) inv++ }   # every row in this file is an invalid-class row
  END { if (n > 0) printf "claims=%d invalid=%d running_rate=%d/%d = %.0f%%\n", n, inv, inv, n, 100*inv/n }
' /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-93/w1/ConnectorOverlap/measurement.tsv
