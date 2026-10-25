# Bounty-triage training module — authorized, artifact-first, report-bounded

Status: **instruction**, not a knowledge entry. It fills no coverage-map row, carries no
Evidence ID and claims no capability. It trains one bounded workflow inside this province:
bounty/coordinated-disclosure triage of a **shipped artifact**, using the lane's existing
REA and evidence-ledger discipline.

- `source:` `PROVINCE.md` (owned/refused surfaces); `SKILL.md` §1–§6 (verifier credit,
  fixture authoring, SOURCES rows, error patterns, Q01–Q16, census); `corpus/QUALITY.md`;
  `corpus/SOURCES.md` S050 (Claude-Red SECURITY.md, maintainer statement) and S051
  (Claude-Red `offensive-reporting` skill, tier C corroboration); `PROTOCOL.md` (round and
  report contract, read-only at the fleet root).
- `verified-at:` 2026-10-27, written in the lane tree; source snapshots
  `corpus/snapshots/claude-red-security.md` (sha256 `b153d16a…`) and
  `corpus/snapshots/claude-red-offensive-reporting.md` (sha256 `b9a8bf71…`), fetched the
  same day. The X thread named in the demand (`x.com/sammy_capital/status/2113733817596834151`)
  was **not readable**: the fetch failed (`x-unavailable`, provider refused the endpoint).
  No claim in this module rests on it; the attempt is recorded in
  `corpus/lessons/2026-10-27-bounty-triage-module.md`.
- `recheck:` `python3 -B corpus/training/bounty-triage/check_package.py --self-test`; the
  two exercise runs in §6; `python3 -B corpus/training/bounty-triage/fixtures/build_exercise.py --verify`.

## 0. What this module trains, and what it refuses

Five competencies, each with an artifact that shows it:

| # | competency | pass artifact |
|---|---|---|
| 1 | read an authorized scope before touching an artifact | `scope.json` with a written authorization, a non-bare policy anchor, dates, allowed methods, artifact digests |
| 2 | artifact-first REA triage | digest-bound artifact + evidence rows whose observations carry their deriving command |
| 3 | evidence preservation | ledger rows bound to the declared digest; saved records byte-preserved (Q09) |
| 4 | report-quality validation | nine-section report whose every impact line is evidence-bound or explicitly unknown |
| 5 | stop/escalation boundaries | `## Stop conditions` section recording a decision, or a `STOP:` with an escalation target |

Refused outright, and **not trained here**:

- live-target exploitation, payload/exploit development, C2 or persistence;
- testing any host, account, endpoint or third-party component not in the written scope;
- using credential material, session tokens or personal data found in an artifact;
- disclosure outside the program's stated channel;
- importing offensive procedures from an external skill library. Claude-Red is used in this
  module **only** as a located corroborating statement of intended use and reporting
  discipline (S050/S051), never as a procedure source.

`PROVINCE.md` still governs: shipped-artifact reverse engineering, no live-target execution
beyond the declared target and lifecycle. A bounty program's written scope **narrows** what
this province may read; it never widens it.

## 1. Stage 1 — authorized scope (decision table)

Everything downstream is void without a scope record. Read the program's own policy text,
not a summary of it.

| condition | decision | record |
|---|---|---|
| written authorization + exact policy anchor (path or fragment, never a bare homepage) | proceed | `scope.json` |
| authorization is verbal, implied by program listing, or absent | **STOP** | `STOP: no written authorization`; do not acquire or read the artifact |
| policy anchor is a homepage or moves during the engagement | **STOP** | re-read the policy; record the old and new anchor |
| `expires_at < as_of` or `authorized_at > as_of` | **STOP** | expired/future authorization is not authorization |
| the artifact was not program-provided and not authored by you | **STOP** | unprovenanced bytes are not in scope |
| the program forbids static analysis, or the artifact is a third-party component under a different policy | **STOP** | escalate to the program; do not absorb the third party into scope |
| confirming a finding would need a live request | **STOP** | report the observation and the unresolved unknown; do not test |
| credential, token, personal data or private key appears in the artifact | **STOP** | record shape only (type/location), never value; escalate to the program |
| two scope clauses conflict | **STOP** | escalate; the stricter clause governs until answered |

Scope record fields (all required; `check_package.py` codes B01–B09):

| field | rule |
|---|---|
| `program` | the program's own name, as written |
| `policy_url` | http(s) URL with a path or fragment naming the clause |
| `authorization` | exactly `"written"` |
| `authorized_by` | who/what accepted the written policy (acceptance ID where one exists) |
| `authorized_at`, `expires_at` | ISO `YYYY-MM-DD`; expiry must not precede the triage date |
| `methods` | allow-list; any `live`, `exploit`, `dynamic` or `network-scan` term is refused |
| `live_target_activity` | must be `false` for this province |
| `artifacts[]` | `path` inside the package, `sha256` of the exact bytes, `provenance` in `program-provided` / `authored` |
| `disclosure` | program `contact` and `window_days` |

A scope is a **stop gate, not a formality**: an expired or unprovenanced scope ends the
exercise. The validator reports it; it cannot grant permission.

## 2. Stage 2 — artifact-first REA triage

Order of operations. Each step produces evidence before the next begins.

| step | do | never |
|---|---|---|
| 1 acquire | copy the program-provided bytes into the package; record provenance | edit, repack or "clean" the artifact |
| 2 freeze | `sha256sum` the copy **before** the first read; write the digest into the ledger and `scope.json` | read first and hash later, or hash an extracted view |
| 3 inventory | name each member and its declared properties from the bytes (`python3 -m zipfile -l`) | describe members from the file name or from intent (Q06) |
| 4 route | if an REA route applies, name tool, version and function and score only its own output (Q04); save the output record byte-preserved | credit a tool with a result it did not print |
| 5 oracle | any parser/layout claim gets an authored known-truth fixture per `SKILL.md` §2, built in a scratch directory | state an offset, size or count from intention |
| 6 ledger | one row per statement with layer `observation` / `inference` / `unknown` | merge layers to make a claim look observed |
| 7 report | write the nine-section report from the ledger | write a finding the ledger cannot support |

Layer discipline (the province rule, made checkable):

| you have | layer | may write |
|---|---|---|
| bytes, a digest, a command's own stdout | `observation` | the fact plus its deriving command |
| a plausible mechanism that the bytes do not demonstrate | `inference` | "may", "consistent with", with its basis row |
| runtime behavior, reachability, authentication, vendor intent, exploitability | `unknown` | the question and what would answer it; never an answer |

Static-only is the default: reading an artifact is not executing it. If a claim needs
execution, it is not triage — it is a stop condition (§1, §5).

## 3. Stage 3 — evidence preservation

Ledger row shape (`ledger.md`; the validator parses exactly this):

```
| id | artifact_sha256 | layer | statement | command |
| E1 | <64 hex>        | observation | ... | `sha256sum artifacts/client.zip` |
```

| rule | check |
|---|---|
| a row's digest is one declared in `scope.json` | L04 |
| `observation` rows carry the command that derives the value | L05 |
| at least one `observation` row exists | L06 |
| layer is one of the three | L03 |
| the ledger has five cells per row | L02 |
| saved records and receipts keep their original bytes; a digest is claimed only for the bytes it hashed | Q09; never "proves origin" |
| credential/session material is recorded as **shape only** | never value, never a copy |

Evidence IDs are the report's citation currency: a report sentence that cites `E4` is
bound to a statement that was itself bound to bytes. Break either link and the sentence is
not evidence.

## 4. Stage 4 — report quality validation

Required sections; `check_package.py --package <dir>` maps each to a code (presence only —
the validator does not check order).

| section | must contain | code |
|---|---|---|
| Scope | `program` and `policy_url` | R02 |
| Artifact identity | each declared artifact's path and digest | R09 |
| Method | at least one method declared in scope | R10 |
| Evidence | at least one ledger ID; every cited ID must exist | R03, R11 |
| Reproduction | commands a reader can run against the package copy | — |
| Impact | every non-empty line cites an `E#` or says `unknown` / `not assessed` | R04 |
| Limitations | at least one concrete limitation | R06 |
| Stop conditions | `none triggered`, `no stop condition`, or `STOP:` + escalation target | R08 |
| Disclosure | program contact and disclosure window | R07 |

Rejected outright as overclaims (R05): `confirmed exploitable`, `confirmed exploit`,
`proven exploitable`, `full compromise`, `guaranteed`, `affects all users/accounts`,
`remote code execution confirmed`. A finding is written as what was observed, against which
bytes, with what remains unknown. Severity language may only restate the program's own
rating or an explicitly quoted rubric; this module does not teach CVSS scoring.

The report is the durable artifact. It names bytes and commands, not a narrative:
a reader must be able to re-hash the artifact, re-run each observation command and reach
the same ledger row without the author present (Q11/Q16 shape).

## 5. Stage 5 — stop and escalation matrix

| trigger | action | escalation target | record |
|---|---|---|---|
| scope absent, verbal, expired, or contradictory | stop before acquisition | program triage channel | `STOP: scope` |
| artifact lacks provenance | stop | program | `STOP: provenance` |
| confirming requires a live request or execution | stop; report observation + unknown | program | `STOP: live confirmation out of scope` |
| credential/session/PII encountered | stop reading that member; record type and location only | program security contact | `STOP: sensitive material` |
| third-party component under another policy | stop; do not absorb it | program | `STOP: third party` |
| finding is outside this province (harness, game mechanics, narrative) | hand off, do not analyse | owning lane / operator | `STOP: cross-domain` |
| disclosure clock or channel unclear | stop | program contact; the lane's operator | `STOP: disclosure` |

Escalation is a recorded act, not a silence: the stop reason, the scope clause it rests on
and the artifact digest stay in the ledger and the report. Stopping is a passing outcome
when a gate fires.

## 6. Offline exercise — run and expected output

Fixture: `corpus/training/bounty-triage/fixtures/` — one authored 866-byte ZIP
(`truth.json`, deterministic builder) and two packages that use the same bytes.

```sh
python3 -B corpus/training/bounty-triage/fixtures/build_exercise.py --verify
python3 -B corpus/training/bounty-triage/check_package.py --self-test
python3 -B corpus/training/bounty-triage/check_package.py \
  --package corpus/training/bounty-triage/fixtures/exercise-r1/package --as-of 2026-10-27
python3 -B corpus/training/bounty-triage/check_package.py \
  --package corpus/training/bounty-triage/fixtures/exercise-r1-defective/package --as-of 2026-10-27
```

Expected: the builder verifies two packages against one digest; the self-test fires all 26
detectors, one case per code, and passes its clean control; the first package prints
`VERDICT=PASS` and exits 0; the defective package prints exactly `B05`, `R04`, `R05`, `R08`
and exits 1.

What a green run does **not** establish: that any statement is true, that the scope was
genuinely authorized, that the artifact is safe, or that the report is publishable. It
checks structure, binding and the stop record — nothing else.

## 7. Failure modes of this module

- Reading the artifact before the scope gate — an expired scope never becomes valid by
  finding something interesting.
- Treating `sha256` as provenance: it binds bytes to a digest, not to the vendor (Q09).
- Letting an inference enter the impact section without the word `unknown`.
- Escalating by staying silent: a stop that is not recorded did not happen.
- Using this module as a knowledge entry or a capability claim: it is instruction.
