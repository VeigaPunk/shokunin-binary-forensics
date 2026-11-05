# MutationR96 — v5 counter mutant battery (round 96, wave 1)

Target: `reports/round-96/c1_k_admit_counter5.py` (frozen bytes, sha256
`805ffb8aabbdbd451781dd831afce7ab41258979489d29ae789ae9fc1a23ad19`, byte-equal to
freeze commit `ff767436feed32cf2f4074f05f938f8cea98e69a`). The committed bytes were
never edited; every mutant is a copy under scratch
`/fast/scratch/hyaku/revenger-r96/MutationR96/` (deleted before yield; each mutant's
source as run and all per-delta receipts are preserved in this directory).

Run form (every invocation `python3 -B`, `PYTHONUTF8=1`, `HYAKU_SCRATCH=<scratch>`):

```
python3 -B <mutant> --self-test --receipts-dir <scratch>/receipts-<tag>
```

Every mutant additionally pins `LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")`
in place of `LANE = Path(__file__).resolve().parents[2]` — behavior-preserving: a scratch
copy's `parents[2]` resolves to `/fast/scratch/hyaku`, not the lane. It is the only
change common to all five.

Detector semantics (frozen harness): PASS requires the honest fixture to pass every leg
(rc 0) and each of the 31 frozen deltas to fail with its `EXPECT_FAIL` leg among the
failing legs (`decide=true`); any `decide=false` or POS/do-nothing failure ⇒
`SELFTEST_C1V5=fail`, rc 1. Per-delta receipts: `receipts-<tag>/<delta>.json` with
`{delta, expected_leg, observed_rc, failing_legs, decide}`.

## Baseline (pristine, required for conclusive verdicts)

Pristine committed counter run in place (never copied, never edited):
`SELFTEST_C1V5=pass legs=33`, rc 0 — matches the frozen control
`reports/round-96/controls/selftest-c1v5.log`. Receipts: `receipts-pristine/` (31 ×
`decide=true`). Baseline failure would have made every mutant verdict inconclusive; it
passed, so all verdicts below are conclusive.

## Verdict summary

| mutant | behavior-bearing point weakened | rc | SELFTEST line | verdict | killing delta (expected_leg) |
|---|---|---|---|---|---|
| a-union | `C1_ADMITTED_UNION` leg | 1 | `SELFTEST_C1V5=fail legs=33` | KILLED | `A4-shadow-admitted` (`C1_ADMITTED_UNION`) |
| b-usedby | used-by exclusivity sub-check (`C1_SOURCES`) | 1 | `SELFTEST_C1V5=fail legs=33` | KILLED | `A3-usedby-extra` (`C1_SOURCES`) |
| c-pycache | `C1_PYCACHE` scan set | 1 | `SELFTEST_C1V5=fail legs=33` | KILLED | `M8-pycache-frozen-dir` (`C1_PYCACHE`) |
| d-host | `C1_RECEIPTS` host allowlist | 0 | `SELFTEST_C1V5=pass legs=33` | **SURVIVED — coverage finding** | none |
| e-heldback | `C1_K_HELD_BACKED` leg | 1 | `SELFTEST_C1V5=fail legs=33` | KILLED | `KHELDBACK-broken-cell` (`C1_K_HELD_BACKED`) |

## mutant-a-union — KILLED

- Exact edit in `evaluate()`: `legs["C1_ADMITTED_UNION"] = au_ok` →
  `legs["C1_ADMITTED_UNION"] = True  # MUTANT-A: leg dropped (unconditionally True)`
- rc 1; `SELFTEST_C1V5=fail legs=33`; exactly one harness failure line.
- Killing delta: `A4-shadow-admitted`, expected leg `C1_ADMITTED_UNION`
  (`receipts-a-union/A4-shadow-admitted.json`: `observed_rc=0`, `failing_legs=[]`,
  `decide=false`; pristine same delta: rc 1, `failing_legs=[C1_ADMITTED_UNION, C1_VERDICT]`).
- Analysis: the A4 close is load-bearing and singly discriminated — with the union leg
  forced True the shadow admitted entry is accepted outright (rc 0), so the frozen
  shadow-entry delta is the only thing standing between the mutation and a false pass.

## mutant-b-usedby — KILLED

- Exact edit in `check_sources()`: replaced the three lines
  `ub = [x.strip() for x in r[10].split(",") if x.strip() and x.strip() != "\u2014"]` /
  `if set(ub) != {ENTRY_REL}:` / `fails.append(f"{sid}:usedby-exclusivity:{ub}")` with
  `pass  # MUTANT-B: used-by exclusivity check dropped`.
- rc 1; `SELFTEST_C1V5=fail legs=33`; exactly one harness failure line.
- Killing delta: `A3-usedby-extra`, expected leg `C1_SOURCES`
  (`receipts-b-usedby/A3-usedby-extra.json`: `observed_rc=0`, `failing_legs=[]`,
  `decide=false`).
- Analysis: used-by exclusivity is the sole discriminator for the A3 used-by drift
  vector — under the drift the cite-back, mined status, tier and opened-date sub-checks
 all stay green, so dropping it flips the delta to a full pass.

## mutant-c-pycache — KILLED

- Exact edit in `check_pycache()`: dir tuple
  `("corpus", "reports/round-93", "reports/round-94", "reports/round-95", "reports/round-96", ".ufo/waves/round-95", ".ufo/waves/round-96")`
  → `("corpus", "reports/round-95", ".ufo/waves/round-95")  # MUTANT-C` — exactly the
  frozen v4 set (`reports/round-95/c1_k_admit_counter4.py` line 423).
- rc 1; `SELFTEST_C1V5=fail legs=33`; exactly one harness failure line.
- Killing delta: `M8-pycache-frozen-dir`, expected leg `C1_PYCACHE` (plants
  `reports/round-94/__pycache__`) — `receipts-c-pycache/M8-pycache-frozen-dir.json`:
  `observed_rc=0`, `failing_legs=[]`, `decide=false`.
- Analysis: the widened scan is precisely what closes M8 — narrowing reproduces the v4
  hole the r95 spot-check routed here, while `M5-pycache-planted` (corpus/, in both
  sets) still dies, so the kill is M8-specific rather than a general pycache breakage.

## mutant-d-host — SURVIVED (coverage finding; reported, not fixed)

- Exact edit in `check_receipts()`: removed the two allowlist lines
  `if host not in HOST_ALLOWLIST:` / `fails.append(f"{sid}:host:{host!r}")`, keeping the
  `host = urlparse(str(r.get("fetch_url", ""))).hostname or ""` assignment (line
  annotated `# MUTANT-D: allowlist accepts any host`). Net effect: any fetch host is
  accepted.
- rc 0; `SELFTEST_C1V5=pass legs=33`; all 31 per-delta receipts `decide=true`
  (`grep -c '"decide": false' receipts-d-host/*.json` → 0 matches).
- The delta that was expected to kill it did not: `V27-fabricated-body-foreign-host`
  (expected leg `C1_RECEIPTS`) still fails on `C1_RECEIPTS` exactly as under pristine
  (`receipts-d-host/V27-fabricated-body-foreign-host.json`: `observed_rc=1`,
  `failing_legs=[C1_RECEIPTS, C1_VERDICT]`, `decide=true`).
- Mechanism (derived from the frozen delta bytes, confirmed by the identical receipt):
  the V27 fabrication is self-consistent (fetched_at = round date, http 200, body sha
  equals receipt `fetch_sha256`) but its fabricated `fetch_sha256` appears in no
  fetch-log line, so the fetch-log sha cross-check (`S502:fetch-log-line-missing`)
  kills it with the host check gone. Within the frozen self-test the host-allowlist
  sub-check therefore has no independently discriminating delta — its coverage is only
  joint with the log cross-check.
- Scope of the finding: this does NOT falsify the frozen C2 predicate — `C1_RECEIPTS`
  the leg keeps two discriminating deltas (`V10`, `V27`), and the claims' coverage
  accounting is per leg, not per sub-check. It means a receipt forged to be
  fully self-consistent (fabricated body + matching receipt + matching fetch-log line)
  under a foreign host would pass the whole leg today. Candidate r97-routable vector
  design: self-consistent receipt+body+fetch-log line under a non-allowlisted host
  (only the allowlist sub-check fails). Per the kill rule and my role: a surviving
  mutant is a coverage finding, never permission to change the frozen contract.

## mutant-e-heldback — KILLED

- Exact edit in `evaluate()`: `legs["C1_K_HELD_BACKED"] = held_backed == HELD_TARGET` →
  `legs["C1_K_HELD_BACKED"] = True  # MUTANT-E: leg dropped (unconditionally True)`
- rc 1; `SELFTEST_C1V5=fail legs=33`; exactly one harness failure line.
- Killing delta: `KHELDBACK-broken-cell`, expected leg `C1_K_HELD_BACKED`
  (`receipts-e-heldback/KHELDBACK-broken-cell.json`: `decide=false`; the delta still
  exits rc 1 but on `C1_ONLY_C02` — a broken backing cell in another row is also row
  drift — and the harness requires the EXPECTED leg among `failing_legs`).
- Analysis: the dedicated held-backed count leg is the discriminator; the incidental
  `C1_ONLY_C02` failure is an artifact of this delta's shape, not a general substitute
  for the K-count check, which is why the expected-leg-strict harness still kills it.

## Restoration evidence

- Committed bytes identical before and after the whole battery:
  `reports/round-96/c1_k_admit_counter5.py` `805ffb8a…a23ad19`,
  `corpus/knowledge/round-96-native-analysis-sessions.md` `2f7d4c1b…6d923`,
  `reports/round-96/claims.md` `89fa1281…9a7a98`; all three byte-equal to
  `git show ff767436feed32cf2f4074f05f938f8cea98e69a:…`; `git status --porcelain` over
  those paths: empty.
- Mutants ran only on scratch copies; scratch deleted after copying receipts and mutant
  sources here. No `__pycache__` or `*.pyc` under `corpus`, `reports/round-93..96`,
  `.ufo/waves/round-95..96` (find: 0 hits); every Python invocation used `python3 -B`.
- Candidate digest re-derived at session start from the lane root:
  `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` (equals the frozen
  vote-binding value; the working-tree entry's status line is `candidate`, so the
  normalizer is identity over current bytes).
- Mutant files as run (sha256): a `9800922596f9ecd0e5386e1aafacb78a11197d085836f717f506dfd15862813b`,
  b `913c673cdf1de2869511ebd449915e8e64d9ec73d94021fd581cf29a3256636a`,
  c `d77ad4861f0caa3f69463fa86eda1057b5b667e95e33e047eb681a09c9d2fc68`,
  d `be7a586c9f1ee6a3823ffa7ffec9dfc31517690989e06668ef83360c0d6a13f7`,
  e `480f5700fb42359c36d73bd4c563cb8df05de86f561b05ddc584746f1800f579`.
