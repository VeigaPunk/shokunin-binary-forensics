# CriticR96 — round 96 w1 report (critic: held-out attacks on the v5 counter and the C02 entry)

Scope: fresh forgeries beyond the frozen 31-delta map, run against the frozen
`reports/round-96/c1_k_admit_counter5.py` on fixtures built by its own `_fixture`
generator (`python3 -B` everywhere), plus a direct audit of the C02 candidate entry and
its receipts/records. Full detail with exact bytes/commands/outputs:
`.ufo/waves/round-96/w1/CriticR96/findings.md` (this seat's vote artifact); per-forgery
receipts under `.ufo/waves/round-96/w1/CriticR96/receipts/` (19 log/json pairs + driver +
summary: `BATTERY_DONE forgeries=19 undecided=0 []`).

## Result in one line

13 counter PASSES (F1–F14, findings routed to r97 — none changes the frozen C1/C2
predicate), 6 kills (K1–K6), and the C02 entry's derivation table verifies row by row
with three minor prose observations (E-1..E-3).

## Counter findings (survivors; r97 material)

1. **Shadow-entry union evasion (4 shapes):** `C1_ADMITTED_UNION` misses a shadow
   knowledge file whose admitted line is decorated (F1: `admission-status: admitted
   (…)` — the leg anchors `$` at "admitted"), lives in a nested dir (F2: non-recursive
   glob), has an uppercase `.MD` extension (F3), or is non-UTF-8 (F4: silently skipped).
   All four trees reach `C1_VERDICT=pass`.
2. **Vote-artifact shape gaps:** seat+digest hidden in an HTML comment passes the
   bytes-containment checks (F5); the own-dir rule is a string prefix, so a symlinked
   artifact_path resolves into a sibling's dir and passes (F6).
3. **Sid token blindness:** `S  0999` (two spaces) and `s0888` (lowercase) are
   invisible to `C1_SIDS`/`C1_SOURCES` (F7).
4. **Pycache class gap:** a loose `corpus/*.pyc` without a `__pycache__` dir evades
   `C1_PYCACHE` (F8) — same defect class as r94 M5/r95 M8.
5. **Quote/anchor binding is dead code:** a receipt whose quote+span anchor a
   DIFFERENT real sentence of the same body passes `C1_RECEIPTS`+`C1_QUOTES`
   (F9) — `audit_source_quotes.py` never calls its own `anchor_quote` in verify mode,
   and no leg compares the receipt quote to the SOURCES anchor cell.
6. **Registry URL unguarded:** a SOURCES row URL pointing at an attacker host passes
   every leg (F10); the receipt's fetch_url is checked only against itself.
7. **Derivation tables are outside the counter's reach:** swapped fixture bytes +
   a self-consistent embedded fence pass with a STALE table sha (F11) — admission
   mechanics only; honesty rests on the non-author closure (which today verifies, §C).
8. **Minor:** extra §Q-map rows unguarded (F13); one merged fetch-log line can serve
   both receipts (F14).
9. **Negative result (F12):** the suggested status-line tab trick does NOT fork the
   digest — normalization is whitespace-invariant; the tree passes only as a
   content-equivalent edit.

## Kills (counter held)

K1 status line below the head window → `C1_ADMITTED=fail`; K2 `recheck:` shifted →
`C1_TRIO=fail` + `C1_LINT=fail`; K3 NBSP inside the status line → `C1_ADMITTED=fail`
(no digest fork); K4 used-by alias `./knowledge/…` →
`C1_SOURCES_WHY=S502:usedby-exclusivity:[…]` (the suggested alias class is closed);
K5 any prose mention of `admission-status:` → count=2 → `C1_ADMITTED=fail`;
K6 whitespace/NBSP digest-fork attempts all normalize away (F12/K3).

## C02 entry audit

Binding facts re-derived: candidate digest `2f7d4c1b…` matches the frozen value;
working-tree entry bytes equal freeze commit `ff767436`'s bytes. Every derivation-table
row re-verified against committed bytes: fixture sha `fe060de1…`, entry bytes
`b8 2a 00 00 00 c3` at 0x200, regen byte-identical (`cmp` rc 0), record digests
`d717b491…`/`6ce217fa…`/`2fba7fbf…`/`6a1d18c3…`, `evidence_id ev_cc0b9d88…`,
provider ghidra 12.1.4, `function_count=1`, `FUNC entry @ 140001000`,
`return 0x2a;`, `INFO  REPORT` count 6, doctor `healthy: false` with the ghidra scope
healthy and Hopper absent, `cli_package_version: 6.7.0` grounding Q04's rea 6.7.0.
Non-author re-fetch at the pinned revision: S502 38167 B and S503 35095 B, HTTP 200,
sha256 equal to the committed receipts; receipt spans verify
(`norm(body[span]) == norm(quote)`); installed skill copy differs from the pinned body
exactly as the entry's Unknown discloses. Q-map: PASS rows spot-verified true, all six
n/a rows genuinely n/a. No scope overreach found. Minor: E-1 exit integers are
session-recorded prose, not record lines; E-2 "6.7.0-era" tag vs frontmatter
`version: "42"` (S002 row records "42" honestly); E-3 the ≤25-word located quotes land
with the L1's round lesson — when it lands, its Gate quotes should equal the receipts'
`quote` fields (that equality is otherwise enforced by no instrument — see F9).

## Gate vote

`vote.json` written in this dir and self-checked against the frozen counter's vote
vocabulary (strict JSON, pinned seat/role, digest equality, Q01–Q17 with 12 PASS,
n/a notes ≥6 tokens each with Qxx cross-reference, artifact inside this seat's dir,
sha verified): `VOTE_SELF_CHECK: pass`. Artifact = `findings.md`
(sha256 `ced3ad5a78703bc9aa3f35067fdd66336df1f8d8701571c34e3b9b64db19afed`).

## Bounds

Writes confined to this wave dir + scratch `/fast/scratch/hyaku/revenger-r96/CriticR96/`
(deleted before yield; receipts copied here). Lane reads and read-only `git show`
only; installs: none; spawns: none (leaf); network: only the two receipt URLs under
raw.githubusercontent.com/morluto/rea.
