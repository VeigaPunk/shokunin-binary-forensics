# Draft — appended correction for `corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (D1)

File: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/2026-10-12-rea-readiness-checklist.md`
(67 lines at freeze `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`; last byte `0a`).

Line 67 exactly (`sed -n '67p'`, read 2026-11-04; the dash is U+2014):

```
(`corpus/live/runs/round-89/`, round 89) — a record, not an admitted finding.
```

with its sentence starting at :66: `still unprobed. The Android route now has a recorded producer run`.

## Append (after line 67; one blank line, then the paragraph; lines 1–67 byte-unchanged)

```

Correction (round 90, 2026-11-04): line 67 names `corpus/live/runs/round-89/`,
which does not resolve after the round-89 adjudication `bd575ca` relocated the
android record (`inspection.json`, `receipt.json`, `LEDGER.md`) to
`reports/round-89/rejected-android-record/`. The record was rejected — preserved
outside the counted surface, not admitted (`lessons/round-89-verifier-spotcheck.md`
D1). Read line 67's path as `reports/round-89/rejected-android-record/`; the
sentence's "a record, not an admitted finding" stands. Lines 1–67 are unchanged.
```

If round 90's C2 lands a counted android record under `corpus/live/runs/round-90/`, the
landing commit may add one further sentence naming that path; this draft does not assume it.

## Acceptance checks for the integrator (read-only)

- `git diff --numstat <base> <landing> -- corpus/knowledge/2026-10-12-rea-readiness-checklist.md`
  → `N 0` (zero deletions; claims.md no-harm, `reports/round-90/claims.md:108-110`).
- `head -n 67 <file> | sha256sum` equals the same over `git show c7767789:<file>`.
- `ls reports/round-89/rejected-android-record/` → `LEDGER.md inspection.json receipt.json`
  (observed 2026-11-04).
