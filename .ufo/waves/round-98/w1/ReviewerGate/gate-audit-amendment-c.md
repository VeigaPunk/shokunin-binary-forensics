# ReviewerGate — gate-audit-amendment-c.md (revenger round 98, wave w1)

Seat: **ReviewerGate** (role: reviewer). Candidate re-audited after
**Amendment C** (lane commit `1b76b4d`, diff base `0146c0a`):
`corpus/knowledge/round-98-rea-host-readiness.md`. This is the L1-declared
last amendment.

Normalized vote-binding digest, recomputed by me with the v6 `digest()` rule
(the file's only `admission-status` line reads `admission-status: candidate`):

```
raw sha256 = digest() = 6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f
```

Equal to the Amendment C digest named by the L1. Prior votes (digests
`1ea9260c…`, `73f1d7e0…`) are superseded and kept by the L1.

## What Amendment C changed (verified from `git diff 0146c0a 1b76b4d -- <entry>`)

1. **Derivation-table preamble rescoped.** Old: "Every value above was derived
   from the saved record by the command shown." New: "Every count, identifier
   and digest stated above is derived below from the saved record by the
   command shown", plus three new honest disclosures: (a) `\|` in a table cell
   is the markdown escape of a shell pipe or a regex alternation bar — true:
   the command cells use `\|` both between pipeline stages (`sed … \| grep …`)
   and as the regex alternation in `grep -cE '^(missing\|stale)$'`, which
   unescapes to the command I ran and that printed `9`); (b) version strings
   and exit codes are not derived in the table — each comes from
   `corpus/live/runs/round-98/host-probes-r98.txt`, where every `$ …` line is
   followed by its printed output and an `rc=` line — true (13 probe commands,
   each with output and rc, verified in my first audit and re-confirmed:
   `rea --version` → `6.7.0` rc=0; binwalk 3.1.0, unblob 26.6.4, jadx 1.5.6,
   java 21.0.13 rc=0; `command -v analyzeHeadless`/`idat64`/`hopper` rc=1);
   (c) the doctor exit code (1) and the `rea inspect-artifact` exit code (0)
   were observed in the L1 session and are **not lines of any record** — true
   (grep for exit/rc lines in both records returns nothing), and this is
   exactly the recorded-not-re-derived labeling Q11 requires for a value
   outside its count/identifier/offset/digest classes.
2. **Three count rows added** (CriticR98's Q11 defect: registration counts had
   no deriving rows). All re-run by me from the lane root; every recorded
   output matches:
   - client registration count: `grep -c '^    - client:' …rea-doctor-r98.txt`
     → `14`;
   - registration state split: `awk '/^    - client:/{c=$3} /^      state:/{print $2}' … | sort | uniq -c`
     → `4 aligned` / `1 manual` / `8 missing` / `1 stale` (same order as the
     entry's cell);
   - missing-or-stale registrations ("nine"): `… | grep -cE '^(missing|stale)$'`
     → `9` (supports the Observation's "nine stale or missing client
     registrations", with the stale skill named separately from
     `skill:identity`).
3. **§Q-map Q06 row changed n/a → PASS**: "The ZIP-inventory producer call ran
   on `fixtures/archive-r2/fixture.zip`. Its premise, the archive digest and
   members in round 2's `truth.json`, matches the fixture bytes: `sha256sum`
   gives `857989f5…`, which equals truth.json `archive_sha256`, as the
   derivation table shows. No fixture was authored or edited this round."

No other hunk: the route table, the §Q-map's other 16 rows, headers, S506
anchor material and the rest of the derivation table are byte-identical to my
Amendment B audit.

## My independent verification of the changed surface

- Digest equality re-derived: `sha256sum corpus/fixtures/archive-r2/fixture.zip`
  → `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`;
  `truth.json` `archive_sha256` is the same value; member sizes 84/16160 and
  archive size 2964 match the record's `declared_size` order. Q06's reject
  condition ("stated from intent rather than from the built bytes") does not
  obtain: the premise comes from round 2's committed truth file (`git log`:
  `5c9fb20`), the fixture bytes are unchanged since, and no failed input
  exists. **Q06 PASS** — my own decision, agreeing with the amended map.
- Q11: every count (11/13/24, 10/11/3, 14, 4/8/1/1, 9, 8, 1/1, 3, 6.7.0 as a
  derived record value), identifier (`ev_0ef6c8…`) and digest (fixture, three
  records, S506 body) now has an in-entry deriving command and recorded
  output; I re-ran all rows across Amendments B and C, all byte-equal. Version
  strings and exit codes are correctly excluded from the table's claim and
  sourced to the probe transcript (versions) or labeled session-observed
  (doctor 1, inspect 0). **Q11 PASS.**
- Q16: the preamble no longer credits the table with values it does not
  derive; each sentence that says what a command prints was checked against
  that command's stdout in the records/transcript (rounds 1–3, re-checked on
  the three new rows). The nine-row's unescaped command is what I executed and
  its `9` matches the Observation's claim. **Q16 PASS.**

## Full decision set (Amendment C)

| Q | decision |
|---|---|
| Q01 | PASS |
| Q02 | PASS |
| Q03 | PASS |
| Q04 | PASS |
| Q05 | PASS |
| Q06 | PASS (changed from n/a by Amendment C; independently confirmed) |
| Q07 | n/a |
| Q08 | n/a |
| Q09 | PASS |
| Q10 | PASS |
| Q11 | PASS |
| Q12 | n/a |
| Q13 | n/a |
| Q14 | n/a |
| Q15 | n/a |
| Q16 | PASS |
| Q17 | n/a |

10 PASS / 7 n/a / 0 FAIL. Nothing in Amendment C creates a new unsupported
claim; the two critic defects are repaired with rows I re-derived myself.

## Remaining uncertainties

- Unchanged from prior audits (non-gating, anchor-only): the S507 registry-row
  anchor "1-based bytes 1-41" for the doctor's first two lines measures 42
  bytes 1-based-inclusive (`head -c 41`, as the dispatch recipe uses, matches
  the stated count; same start-1 convention as S505). No Q id governs it; not
  affected by Amendments B or C.

## Tooling

No tools installed or upgraded. Host python3/git/coreutils over committed
bytes only; no network fetches this round (S506 body and receipt unchanged
since my byte-identical re-fetch at Amendment A digest). No writes outside my
wave dir, the vote file, my findings file and scratch
`/fast/scratch/hyaku/revenger-r98/ReviewerGate/` (deleted on exit).
