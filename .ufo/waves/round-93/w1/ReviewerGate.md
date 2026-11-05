# ReviewerGate — Q-gate report on the C08 admission (round 93, wave 1)

Report path relative to lane root. Output files:
- vote: `.ufo/waves/round-93/w1/ReviewerGate/vote.json`
- evidence: `.ufo/waves/round-93/w1/ReviewerGate/evidence.md`
- scratch: `/fast/scratch/hyaku/revenger-r93/ReviewerGate/`

## Vote

`seat=ReviewerGate, role=reviewer`, candidate digest
`1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647` — final
binding, recomputed from the L1's LANDED bytes at
`corpus/knowledge/round-93-browser-cdp-runtime-evidence.md` after two L1
amendments (first: removal of the underived "stdout line count of the oracle
block is 18" sentence and the "(15 words)" parenthetical — `evidence.md` §9;
second: the `verified-at:` byte-identity clause rescoped to `corpus/live` +
`corpus/fixtures`, with the corpus index/registry explicitly excluded —
`evidence.md` §10; both removals/re-scopes re-checked, gates exit 0 re-run on
the landed bytes). Decisions:
Q01–Q04 PASS, Q05 n/a, Q06–Q07 PASS, Q08 n/a (superseded by Q11), Q09–Q11
PASS, Q12 n/a, Q13–Q17 PASS — 14 PASS / 3 reasoned n/a, every `n/a` carries
a nonempty reason naming why the criterion cannot apply. Artifact bound:
`evidence.md` sha256
`420030fb91755bdc04013649576b3974cbe7abab36670263a99e6b200ee41bb9`
(re-hashed after every edit incl. the §9/§10 appends; final vote.json carries
the final artifact sha). Vote validated locally against the frozen counter's
schema: all seven fields present, decisions complete, `n/a` reasons nonempty,
≥1 PASS, registry seat, artifact sha match, candidate digest match against
the LANDED entry bytes.

## Key numbers

- **S495 oracle re-run (mine, from the lane root):** exit 0,
  `ORACLE OK (17/17 checks)`; all 18 stdout lines byte-identical to
  `reports/round-93/controls/oracle-opening.log` (that log adds a
  command/head/digest preamble; the 17 check lines + summary match exactly).
- Independent sha256 re-hashes: `inspection.json`
  `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868` (pin),
  `index.html` `46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45`,
  `app.js` `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`;
  inline script text 46 bytes sha256
  `ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783`.
- **S496 re-fetch (mine):** HTTP 200, 35462 bytes, sha256
  `ba8018bb02f360686cbff23304da8b6e21923a2e012ade273e3f9a2ce1e2fd64`
  — byte-identical to ScoutRecord's receipt and raw body; quote located at
  raw byte 3410 (receipt span 3408, same 108 normalized chars); 15 ≤25 words;
  `landing-hero` second sentence; no `ms.date` on the page; no drift vs the
  scout receipt.
- Embedded blocks re-run: **8 of 8 distinct declared commands** (2 oracle
  `$`-blocks and 7 `transcript —` one-liners) — every embedded output line
  reproduces verbatim, including the item-5 block re-executed exactly via
  shlex with a 9/9 line-by-line diff.
- Gates on final draft: `lint_entry.py` `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0
  LINT_HEADER=0` exit 0; `check_embedded_outputs.py` `checked_blocks=2
  problems=0` exit 0.
- Candidate digest history I observed (all recomputed by me, each matching the
  READY then on disk): `92156369…` (mid-write) → `03fee3ca…` (double-`$`
  revision, gate refused exit 2) → `0db16a56…` (final; fences at lines 38/353
  carry a single `$`, gate replays both oracle blocks clean).

## Defect found and closed (also reported, not smoothed over)

Draft revision 2 had `$ $ python3 …` in both replayable oracle fences; the
frozen-gate consequence was `check_embedded_outputs.py` exit 2
(`could-not-evaluate: no `$ cmd` blocks or unsupported command`) =
`C1_EMBEDDED=fail` → `C1_VERDICT=fail` had that revision landed. Recorded in
`evidence.md` §7 with the mechanical chain; the scribe fixed the two fence
lines its own revision 3 (mtime 12:14:32), which my final gate run confirms:
exit 0, `checked_blocks=2 problems=0`. No lane file outside my seat dir was
edited; the fix lives in ScribeEntry's own draft (their write surface), not in
any file I touched.

## Not checked / remaining verification gaps

- Post-land state of `corpus/README.md` C08 row (my check is the pre-land
  9/15 base; the landing counter re-derives 10/15 itself, C1_K_HELD_BACKED).
- Other seats' `reports/round-93/votes/*.json` (≥2 required for C1_VOTES); my
  vote alone cannot satisfy the quorum leg.
- Landed `corpus/SOURCES.md` rows S495/S496 (I verified the quotes the two
  rows carry, via oracle log + my own S496 fetch; the landed row byte shapes
  are the L1's write surface, not mine).
- `forge_battery.py` / `c2_legend_counter2.py` internals (C2 attack lane is
  CriticR93 + MutationR93's assignment).
- scratch left on disk by me: nothing that needs cleanup (files under
  `/fast/scratch/hyaku/revenger-r93/ReviewerGate/` are read-only artifacts of
  this gate, no fixtures or clones; nothing in `/tmp`).

## Tooling

Nothing installed or upgraded (operator allows it, but curl, python3, git,
sha256sum, sed, diff, wc all preinstalled; pacman is paused host-wide;
`uv`/`npx`/`cargo` unused this session).
