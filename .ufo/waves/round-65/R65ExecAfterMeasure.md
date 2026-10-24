PASS — the copied current corpus with only the scratch README C05 flip yields all requested round-65 targets and counter exit 0.

## Evidence

- Read the frozen contract at `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` before measuring. The counter reads C1 from `corpus/README.md` and backed entry files (`measure.py:28-38`), checks C5 (`measure.py:259-306`), and computes V3 (`measure.py:321-331`). Final committed-archive measurement remains the admission-order step in `claims.md:110-124`.
- Copied the current working `corpus/` to `/tmp/revenger-r65-aftermeasure.97SwNp/corpus`. In that copy only, changed README row 34 from `| C05 | Android packages (APK) | — | — | frontier |` to `| C05 | Android packages (APK) | `knowledge/round-65-apk-axml-byte-evidence.md` | — | held |`. The copied row was read back at `/tmp/revenger-r65-aftermeasure.97SwNp/corpus/README.md:34`. The real README remains `frontier` at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md:34`.
- Input hashes: real working README `9fc7eb3fe326dda0cfa2390699af536aa880f684d80cbd92bf85814309d0349f`; scratch README with C05 flip `be3163744aa453ef1015edfce49159599c81b5a5ddd7a3238ab5cae5d27d3637`; scratch fixture APK `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`.
- Ran from `/`:

  `TMPDIR=/tmp/revenger-r65-aftermeasure.97SwNp python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py /tmp/revenger-r65-aftermeasure.97SwNp; rc=$?; printf 'COUNTER_EXIT=%s\n' "$rc"; exit "$rc"`

  Exact relevant stdout from the captured run:

  ```text
  K_HELD=9/14 score=6.4
  K_ROW C05 status=held
  K_HELD_BACKED=9/14
  K_HELD_BACKED_STRICT=9/14
  STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
  README_TOKEN_LEGEND_MISMATCH=0 rows=[]
  C2_CONTROLS_PASS=2/2
  C2_RECEIPT_B_KILLED=2/2
  C2_D2_KILLED=2/2
  C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
  C3_CONTROLS_PASS=2/2
  C3_RECEIPT_KILLED_ATTRIBUTED=2/2
  C4_CONTROLS_PASS=2/2
  C4_RECEIPT_KILLED_ATTRIBUTED=2/2
  C5_CONTROL_PRESENT=2/2
  C5_CONTROLS_PASS=2/2
  C5_RECEIPT_KILLED=2/2
  C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
  HOLD_CALIBRATION=4/4
  HOLD_REPLAY=10/10
  HOLDS_OK=yes
  HOLDS_OK_V2=yes
  HOLDS_OK_V3=yes
  COUNTER_EXIT=0
  ```

- C5 attribution was specifically `MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted` and `MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted`.

## Files, behavior, limits

- Repository file changed: this report only. No production files or real README were edited. The temporary corpus copy is at `/tmp/revenger-r65-aftermeasure.97SwNp/corpus`.
- Behavior: on the simulated C05 held row, the counter counts the candidate entry as backed and strict-backed, reports C05 held and C5 attributed 2/2, with V3 yes and exit 0.
- Risk/limit: this is the requested dry run against current working-tree corpus bytes plus a synthetic README flip, not a committed-tree `git archive` measurement. The final committed-tip measurement is still required by the frozen contract. No other blockers observed.
