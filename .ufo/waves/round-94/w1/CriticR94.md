# CriticR94 — round-94 attack pass (scoped report)

Full findings, ranked: `.ufo/waves/round-94/w1/CriticR94/findings.md`. Per-Q adjudication (contains the
candidate digest `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`):
`.ufo/waves/round-94/w1/CriticR94/evidence.md`. Vote: `.ufo/waves/round-94/w1/CriticR94/vote.json`.
Per-attempt stdout: `.ufo/waves/round-94/w1/CriticR94/receipts/`. Driver: `.ufo/waves/round-94/w1/CriticR94/attacks/attacks.py`.

## Result

- Frozen twelve reproduce on the v3 counter (tree mode): 12/12 killed. Self-test: `SELFTEST_C1V3=pass legs=14`.
- 27 fresh forgeries plus 2 controls and 1 honest residual, each run through `--rev` (landing path) and
  `--tree` where it matters. Seventeen forgeries pass v3. Two controls kill as required.
- Three HIGH findings:
  - H1: an indented second `admission-status:` line passes (the r93 dup-status class in a new shape).
  - H2: C1_QUOTES verifies receipt self-consistency, not a fetch. A stale `fetched_at` passes, and an
    invented body with recomputed sha/quote/span passes.
  - H3: the C15 "backed by the entry" link is a substring check. The K count reaches 11/15 with the
    entry only named, and with a nonexistent `legacy/knowledge/...` path.
- Wording: `claims.md` names a leg `C1_REGISTRY` that the counter does not have (the check sits inside
  `C1_VOTES`). The C1 opening-evidence sentence overstates what C1_QUOTES reads. C2's "classes" should read
  "named vectors". C1_ONLY_C15 does re-derive its base from `git archive FREEZE_REV` on every run (verified).
- Votes: 8 PASS, 9 `n/a` with reasons, bound to the tip digest. I could not verify S498/S499 or the receipts
  at the tip (they do not exist there yet), so Q01/Q02/Q09 PASS are conditional on the L1 landing them.

## Not run

- `forge_battery3.py --stage red-v2`: writes into `revenger-r93` scratch, which is off-limits to this seat. The
  committed `controls/battery3-red-v2.log` is cited, not re-observed.
- `forge_battery3.py --stage full`: writes into the shared `revenger-r94/battery3`. My frozen-kill cross-check
  reproduces its V3 loop in my own scratch instead.
- No network use.

## Lane discipline

No lane file edited; no git mutation in the lane (fixture repos live in scratch, objects borrowed read-only
through alternates). Scratch `/fast/scratch/hyaku/revenger-r94/CriticR94` deleted at exit after receipts were
copied into this wave dir.
