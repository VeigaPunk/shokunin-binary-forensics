# ConnectorR99 — revenger round 99, wave w1 (findings, read-only)

**Seat:** `ConnectorR99` (UFO-FSD connector, leaf member, no subagents)
**Lane:** `revenger` (`/home/vgpnk/Projects/shokunin/revenger-shokunin`)
**Claims frozen at:** `7e6edd4db649f99c425daa46a91edbbd18a6e27c` (`reports/round-99/claims.md`)
**Candidate read:** `corpus/knowledge/round-98-rea-host-readiness.md` (`admission-status: candidate`, C14)
**Judged on:** coverage
**Milestone:** Sibling-overlap scan for host-readiness / doctor knowledge and counter-leg patterns
**Write scope:** this file only. No sibling, fleet or lane-tracked file was written. No counter was run on any landing tree; no vote, freeze or corpus byte was touched.

---

## 0. Bottom line

1. **Host-readiness / doctor knowledge.** Sibling lanes hold REA doctor and host facts (kaidoku, game-dev-3d). None contradicts a current route verdict in the candidate. Real gaps and version-scoped disagreements exist (§2, §3). The most important is an **unacknowledged second Ghidra on PATH** (`/usr/bin/ghidra` → `/opt/ghidra`, 12.1.2) that the candidate never mentions, and the candidate's "configured" Ghidra verdict depends on an env var it does not name.
2. **Counter legs.** No sibling admission counter was found that implements any of the nine r98 holdout-class refusals. The lane's own v7 counter is the instrument that holds these legs. §4 maps each r98 vector to the v7 line that decides it (accepted or refused, per the lane brief's 9/12), with sibling analogues where they exist. Reusable rules R-a…R-i were sent to `ExecCounterV8`.
3. **PROVINCE fit.** The candidate's scope is inside `PROVINCE.md` (engine and route readiness is the lane's domain, `PROVINCE.md:17-18`). Sibling-domain overlap (kaidoku owns the Ghidra/JDK provider and archive inspection) is adjacency, reported not absorbed. The lane's own dated host census (`PROVINCE.md:22-40`) contradicts the candidate's host facts and the candidate does not supersede it (§5).
4. **Correction to my prior scan.** `ConnectorOverlap.md` (round 98) reported "ZERO sibling knowledge contradicts the candidate", comparing only against kaidoku. This wider scan finds the game-dev-3d, lane-PROVINCE and PATH-Ghidra items in §2–§3 that the round-98 scan did not reach.

---

## 1. Method and bounds

- **Sibling host-readiness search.** Grep over every `corpus/knowledge/*.md` of the 19 sibling lanes for `rea doctor|readiness|analyzeHeadless|jadx|doctor`. Output was paginated (121 files matched in kaidoku alone). §2 lists the entries bearing on a candidate row, not every hit.
- **Counter-leg search.** Grep over sibling `*.py` for the holdout-class tokens (`admission-status|VERDICT=|coverage-map|fetched_at|fetch-log|recheck:|Q14|C1_VERDICT|C2_ACCEPTED|holdout|forge_reach`) gave 1,863+ hits, dominated by lane-specific fixtures. **This was a paginated pattern scan, not an exhaustive census.** §4.3 lists the sibling counter-like scripts that were actually opened or grepped.
- **Host facts, read-only.** `command -v ghidra analyzeHeadless rea hopper`; `ls -l /usr/bin/ghidra`; `head /usr/bin/ghidra`; `cat /opt/ghidra/Ghidra/application.properties`; `echo $GHIDRA_INSTALL_DIR $JAVA_HOME`; `ls /usr/bin/analyzeHeadless`.
- **Vacuous test, disclosed.** `kake-shokunin/.ufo/waves/round-37/criteria/bare_id_check.py` was run on a scratch file with no S-id. It exited 0 (`PASS … cites no S-id`). The rule only inspects blocks that carry an S-id, so this is not evidence for or against any leg.
- **Installs.** None. No tool was installed, upgraded or removed; no `pacman` transaction was attempted.
- **Development-set status.** Nothing here scores a landing tree or the r98 holdout. The counter maps in §4 are code reading plus the lane brief's accept/refuse list; the builder results were not re-run.

---

## 2. Overlap table — host-readiness / doctor knowledge

Verdict key: **agree** = same current fact; **version-scoped** = both true at their own date or version; **gap** = candidate silent on a fact another record establishes for this host; **contradiction** = incompatible fact.

| # | Source (file:line) | What it says | Vs. candidate `round-98-rea-host-readiness.md` (line) | Verdict |
|---|---|---|---|---|
| 1 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-doctor-taxonomy.md:3,5,9-18` | `rea` 6.4.0; `rea` absent from PATH on 2026-10-13; doctor 18 checks | Candidate: `rea` 6.7.0, 24 scope checks (`corpus/live/runs/round-98/rea-doctor-r98.txt:9` `scope_checks[24]`). Per-shell PATH fact agrees (candidate :59) | version-scoped |
| 2 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-doctor-taxonomy.md:41-50` | 8/8 Ghidra deep checks ok under `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC` | Candidate row 2 (:54) and derivation rows (:86-87); record `rea-doctor-r98.txt:28,40,48,52` same path | agree |
| 3 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-asar-surface.md:49-54` | `healthy: false` does not blind the JS/Electron surface | Candidate :108-111 "a failing overall doctor verdict is therefore not a readiness verdict for a given route" | agree |
| 4 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-java-runtime.md:8-14` | JDK `21.0.12.1` at `/usr/lib/jvm/java-21-openjdk` (10-13) | Candidate `21.0.13` (`rea-doctor-r98.txt:56`), same path | version-scoped (JDK drift) |
| 5 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-ghidra-install.md:21-26` | `support/analyzeHeadless` under the install dir, not PATH-exposed | Candidate :54 "`command -v analyzeHeadless` exited 1 … doctor finds it under the install directory" | agree |
| 6 | `kaidoku-shokunin/PROVINCE.md:27` | Reverified 2026-11-04: `GHIDRA_INSTALL_DIR=/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`, JDK 21 | Candidate row 2 "configured" depends on that env var; candidate does not name the dependency | agree on value; **gap** (§3.1) |
| 7 | `kaidoku-shokunin/PROVINCE.md:28` (provider-key inventory, `.bashrc:63-69`) and `:135-136` | Names `REA_BINWALK_COMMAND`, `REA_UNBLOB_COMMAND`, `REA_PWNTOOLS_PYTHON`, `REA_JADX_MCP_JAR` (names only) | Candidate rows 4, 5, 8 (:56-57, :60) say "configuration" with no env keys | **gap** (§3.2) |
| 8 | `kaidoku-shokunin/PROVINCE.md:15-19` ("Drift-prone values"; operator `disabledServers: ["rea"]` for OMP, re-read 2026-11-04) | The operator **disabled** the OMP `rea` entry | Candidate row 6 (:58) "1 stale (omp)" with no mention of the disable; "stale" and "disabled" are different states | **gap** |
| 9 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4u-01-firmware-deep.md:79` (quoted by round-98 `ConnectorOverlap.md:196`; not re-opened this round) | Doctor inspects only ghidra+ida; binwalk/unblob never checked | Candidate row 5 (:57) "Doctor has no binwalk or unblob check" | agree |
| 10 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-13-pwntools-persist.md:14,178` (quoted by round-98 `ConnectorOverlap.md:199`) | Doctor blind to pwntools | Candidate row 8 (:60) | agree |
| 11 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-rea-live-jq-e2e.md:117,120` (quoted by round-98 `ConnectorOverlap.md:92`) | `healthy: false` coexists with working native decompilation | Candidate :102-111 | agree |
| 12 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-mcp-registrations.md:72-73` | Repair path `rea doctor --client <id>`, then `rea setup --dry-run` | Candidate is read-only and does not reference it | agree (no conflict) |
| 13 | `game-dev-3d-shokunin/corpus/knowledge/rea.md:6-9` | "no `rea` CLI installed fleet-wide"; `npx rea-agents@6.4.0`; no Ghidra, JADX, Binwalk/Unblob, pwntools | Mint-time state; candidate :54-60 says present/configured on 2026-11-05 | version-scoped (stale at mint) |
| 14 | `game-dev-3d-shokunin/corpus/knowledge/rea.md:36-40` | JADX 1.5.6, binwalk 3.1.0, unblob 26.6.4 present, exit 0 | Candidate :56-57 | agree |
| 15 | `game-dev-3d-shokunin/corpus/knowledge/rea.md:46-49` (and `:48`) | "`JAVA_HOME` is OpenJDK 21, above the **required Java 17**" | Candidate doctor detail `rea-doctor-r98.txt:56`: "accepted a 64-bit full JDK 21 or newer" | **contradiction** on the JDK floor (17 vs 21). Version-scoped: game-dev-3d text predates REA 6.7.0; the doctor record is the current source. Flag only |
| 16 | `game-dev-3d-shokunin/corpus/knowledge/rea.md:50` and `:67` ("Ghidra absent"; "r102 probe (`which`)") | Ghidra absent on PATH at r102 (2026-10-18) | Candidate: Ghidra present under `~/.local/opt`; a `/usr/bin/ghidra` launcher is on PATH now (§3.1) | version-scoped |
| 17 | `revenger-shokunin/corpus/knowledge/2026-10-12-rea-readiness-checklist.md:48-62` (**Re-verification 2026-11-04**, K01–K06; K04 at :60, K05 at :61) | K04: "ghidra present at /usr/bin/ghidra"; K05: jadx/binwalk/unblob/pwntools present; K03: omp `rea` registered `rea-agents@6.7.0` | Candidate supersession sentence (:13-16) names only the 2026-10-19 re-probe, not the 11-04 section. K05 agrees with candidate rows 4, 5, 8; K04's PATH-Ghidra fact is absent from the candidate (§3.1) | agree on rows; **gap** on supersession (§3.3) |
| 18 | `revenger-shokunin/corpus/knowledge/round-96-native-analysis-sessions.md:44-50` | Doctor ghidra 8/8 healthy, `analyzeHeadless` under `~/.local/opt`, Hopper missing | Candidate :54-55 | agree |
| 19 | `revenger-shokunin/corpus/knowledge/seed.md:63` (mint) and `:92` (F08 re-verification) | `:92`: "ghidra present at /usr/bin/ghidra" | Same as row 17 | **gap** (§3.1) |
| 20 | `revenger-shokunin/PROVINCE.md:22,25-27,38-40` (host census, dated 2026-10-31 / 2026-11-01) | rea **6.8.0**; ghidra 12.1.4 at **`C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC`**; **jadx absent**; **binwalk/unblob absent**; **pwntools import fails** | Candidate (2026-11-05, Linux host): rea **6.7.0**; Linux Ghidra path; jadx 1.5.6 present; binwalk 3.1.0 and unblob 26.6.4 present; pwntools imports | **contradiction** (version-scoped by date; the candidate does not supersede the census, §5) |

No sibling knowledge entry contradicts a current route verdict in the candidate. The contradictions are version-scoped (rows 1, 4, 13, 15, 16, 20) or sit in the lane's own PROVINCE census (row 20, §5).

---

## 3. Gaps the candidate leaves open (for L1 / CriticR99; nothing edited)

### 3.1 Second Ghidra on PATH — not mentioned by the candidate

Read-only probes, 2026-11-05:

- `command -v ghidra` → `/usr/bin/ghidra` (exit 0). `ls -l /usr/bin/ghidra` → `/usr/bin/ghidra -> /opt/ghidra/ghidraRun`.
- `/opt/ghidra/Ghidra/application.properties` → `application.version=12.1.2`.
- `echo $GHIDRA_INSTALL_DIR` → `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`; `echo $JAVA_HOME` → `/usr/lib/jvm/java-21-openjdk`.
- `command -v analyzeHeadless` → exit 1; `ls /usr/bin/analyzeHeadless` → exit 2 (absent). Candidate :54 is correct on that point.

Consequences:

- The doctor's ghidra checks run against `GHIDRA_INSTALL_DIR` (12.1.4; `rea-doctor-r98.txt:28,40,48,52`), not against the PATH launcher (12.1.2). The candidate's row 2 "configured" therefore holds **only with that env var set**. The candidate states the install path (:54) but not the env dependency. A shell without `GHIDRA_INSTALL_DIR` would classify the same route differently. [INFERENCE from doctor detail strings; the env-less doctor run was not performed.]
- The candidate's "one host" framing (:12-18) and derivation table omit the 12.1.2 launcher, though `2026-10-12-rea-readiness-checklist.md:60` (K04, 2026-11-04) and `seed.md:92` already record `/usr/bin/ghidra`.
- This is an unstated fact, not a contradicted derived value. Whether it requires an amendment is an L1 decision; the C1 amendment budget allows one, before the v8 freeze.

### 3.2 Env-dependent routes — keys not recorded

`kaidoku-shokunin/PROVINCE.md:28` lists REA provider keys exported in `.bashrc:63-69` (names only): `REA_PWNTOOLS_PYTHON`, `REA_BINWALK_COMMAND`, `REA_UNBLOB_COMMAND`, `REA_APKTOOL_COMMAND`, and others; `:136` shows `REA_JADX_MCP_JAR`. The candidate's "configuration" verdicts for JADX, binwalk/unblob and pwntools (rows :56-57, :60) do not say which key each relies on. Recording key **names** (no values) per row would make the classification reproducible. Not a count; it touches no derivation row.

### 3.3 Supersession sentence is incomplete

Candidate :13-16 supersedes "the pre-contract 2026-10-12 checklist (…, re-probed 2026-10-19)". The same file has a **2026-11-04 Re-verification** section (`2026-10-12-rea-readiness-checklist.md:48-62`), newer and covering the same host. It agrees with the candidate on JADX/binwalk/unblob/pwntools (K05) and MCP count (K03), and differs on the PATH Ghidra location only by omission (K04, §3.1). The candidate should name that section when it supersedes the checklist.

---

## 4. Counter-leg overlap (r98 holdout classes vs. v7 and siblings)

### 4.1 The twelve r98 vectors and the v7 line that decides each

Vector list: `.ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py:298-339`. Accepted/refused status is taken from the lane brief (v7: c02 accepts V01, V02, E01, E02, E03 and refuses R01; c14 accepts R01, V02, O01, L01 and refuses V01, Q01). The builder results were not re-run.

| Vector | v7 status | Deciding line (v7 `reports/round-98/c1_k_admit_counter7.py`) and mechanism | Sibling analogue (path:line) |
|---|---|---|---|
| c02 V01 hidden dissent, upper-case `ReviewerBlind.JSON` | accepted | `:231` and `:587` `glob("*.json")` — case-sensitive; the upper-case file is never read | none. Lane's own knowledge scan lowercases the suffix at `:503` (`x.suffix.lower() == ".md"`), so the votes scan is inconsistent with it |
| c02 V02 n/a reason = criterion ids only | accepted | `:220-222` `na_reason_ok`: `len(tokens) >= 6 and re.search(r"Q\d{2}")` — Q-id tokens count as words | `kake-shokunin/.ufo/waves/round-37/criteria/bare_id_check.py:37-41` (`LABELS` includes `see`; `MIN_CLAIM_WORDS = 3`). **As written it still passes V02**: the note reduces to `for the reason`, three claim words. Usable only with a stopword list that includes `for` and `the` (R-b) |
| c02 E01 recheck names no command (`recheck: none`) | accepted | `:813-814` `C1_TRIO` tests `l.startswith("recheck:")` only | `chousa-shokunin/corpus/evidence/round53/c1-count.py:10-13` requires the recheck to begin with a calendar-valid date or `NNd`; this does not transfer to command-led rechecks. `kaidoku-shokunin/.ufo/waves/arc3-loop1-round12/claims/c3/RV-3/evidence/seeded-fault.py:33,41` pins a per-entry `must_match` regex on the recheck line — a regex precedent (R-c) |
| c02 E02 two hex runs in one clause, wrong count | accepted | `revenger-shokunin/corpus/lint_entry.py:14-16`: the Q14 rule fires only on a line with **exactly one** hex run and **exactly one** count | none (lane-internal leg) |
| c02 E03 coverage-map header names another row | accepted | `:519` `HEADER_KEYS`, `:539-566` `check_header_position`: presence and position only; no binding between the header id and the citing row | `kaidoku-shokunin/.ufo/waves/arc3-loop1-round3/claims/c1/RV-4/verify_map_token.py:170-172` scopes edits to the coverage-map section; section scope, not header binding. No direct analogue |
| c02 R01 held C06 row backed by an unadmitted candidate | refused | Not traced to a line in this seat. Candidate sits in the C06 row; the `C1_ONLY_TARGET` diff (`:787-797`) is the likely refusal. Not verified | none |
| c14 R01 suffix row `C14a` outside the count | accepted | `:776` `re.match(r"^\|[ \t]*C[0-9]+ ", l)` — `C14a` fails the match, so the row is outside `cov`, `C1_ROWS_TOTAL` and the `C1_ONLY_TARGET` diff; `:178` and `:496` `re.fullmatch(r"C\d{2}", …)` likewise skip it | `kaidoku-shokunin/.ufo/waves/arc3-loop1-round3/claims/c1/RV-4/verify_map_token.py:119-123` (whole-section token multiset vs. base: an added `C14a` token changes the multiset) |
| c14 V01 one-word placeholder PASS note (`ok`) | refused | `:585-621` `check_vote_notes`, run for the c14 profile (`:607`): PASS notes under 6 tokens fail | none (the lane's own rule works here) |
| c14 V02 FAIL under out-of-range key `Q18` | accepted | `:253` `set(ds) >= set(QS)` — superset allowed; `:255-260` loops only over `QS`, so `Q18` is never read | none |
| c14 Q01 S506 receipt span shifted by one byte | refused | Not traced to a line in this seat; plausibly the quote-byte leg (`:674` `check_quote_bytes`) | none |
| c14 O01 own-work pointer re-pointed to a round-96 record | accepted | `:644-672` `check_ownwork_paths`: `path_nonempty` only (existence) | none. Closest: `kake-shokunin/.ufo/waves/round-28/c2_source_count.py:94-95` (header `verified-at` must equal the opened date) — date binding, not path binding |
| c14 L01 fetch-log header date ≠ receipt `fetched_at` | accepted | `:334-335` compares receipt `fetched_at` to `ROUND_DATE`; `:347-351` checks only that a fetch-log line carries the sid and sha. **The fetch-log header date is never parsed** | `kake-shokunin/.ufo/waves/round-27/count_c1.py:79-82` parses per-fetch `fetchedAt` with `datetime.fromisoformat` and bounds it against the declaration time (`fetch_status_or_time`) |

Summary of accepting legs: c02 V01 `:231/:587`; c02 V02 `:220-222`; c02 E01 `:813-814`; c02 E02 `lint_entry.py:14-16`; c02 E03 `:539-566`; c14 R01 `:776`; c14 V02 `:253`; c14 O01 `:644-672`; c14 L01 `:334-335` and `:347-351`.

### 4.2 Reusable rules (sent to `ExecCounterV8` by message)

- **R-a (V01).** Enumerate every entry of the votes dir; fail on any name not matching `^[A-Za-z0-9_-]+\.json$` exactly. Replace the glob at `:231` and `:587`. Pattern source: the lane's own `:503` lowercasing scan.
- **R-b (V02).** Add a content-word leg to `na_reason_ok` (`:220-222`): strip `Q\d{2}` tokens, drop stopwords `{see, for, the, a, an, of, to, in, on, by, this, that, is, and, or, with, no, not}` and labels; require ≥3 remaining words of ≥2 letters. For V02 this leaves `reason` (one word). **Verify against every legitimate r98 n/a note before adoption** — not done here.
- **R-c (E01).** Require the `recheck:` value to contain a backticked command or a path-bearing command, not only the prefix at `:813-814`. The chousa date-or-`NNd` form does not transfer to command-led rechecks.
- **R-d (E02).** Pair each `N-byte` count with its nearest hex run in the same clause (`corpus/lint_entry.py:14-16` currently requires exactly one of each); reject a clause whose counts and runs differ in number.
- **R-e (E03).** Bind the entry's `coverage-map:` id to the README row(s) whose knowledge cell names this entry path. `:539-566` checks presence and position only.
- **R-f (R01).** Parse every README line starting with `|` whose first cell matches `^C\w+$`; require the id set to equal `C01..C15` exactly; diff the raw lines of every such row against base (`:178`, `:496`, `:776`, `:787-797` currently use `C\d{2}` / `C[0-9]+ `). The token-multiset approach at `verify_map_token.py:119-123` is the second option.
- **R-g (O01).** For each own-work pointer, require the `round-\d+` segment to equal the round named in the entry's own `source:`/`verified-at:` header or the SOURCES row's opened date. Existence-only (`:644-672`) is the gap.
- **R-h (L01).** Parse the fetch-log header date (`reports/round-98/quote-receipts/fetch-log.md`, first line) and require it to equal each receipt's `fetched_at` date. Model the parse on `kake-shokunin/.ufo/waves/round-27/count_c1.py:79-82`.
- **R-i (V02 c14).** Change `:253` `set(ds) >= set(QS)` to `set(ds) == set(QS)`; any decision outside `QS` fails.

### 4.3 Sibling counter-like scripts examined

- `chousa-shokunin/corpus/evidence/round29`–`round53/*.py` (c1/c2 counters; quote-reopen; line-binding; recheck and staged-row legs). Lane-specific. Recheck and fetch-date legs are the only analogues (listed above).
- `kake-shokunin/.ufo/waves/round-27/count_c1.py`, `round-28/c2_source_count.py`, `round-37/criteria/bare_id_check.py` — fetch-time, header-date and bare-id analogues (listed above).
- `kaidoku-shokunin/.ufo/waves/arc3-loop1-round3/claims/c1/RV-4/verify_map_token.py`, `arc3-loop1-round12/claims/c3/RV-3/evidence/seeded-fault.py` — coverage-map token diff and recheck regex (listed above).
- `kotodama-shokunin/reports/round-83/counterlib.py`, `round-84/counterlib.py`; `kengaku-shokunin/plans/round84_c2_admission.py` (cited by round-98 `ConnectorOverlap.md:164`); `mori-shokunin/tools/mori-pin-check.py`; `tsukuroi-shokunin` counters — **not opened in full this round**; the pattern scan did not surface any of the nine legs in the lines it showed. Not a negative proof.

---

## 5. PROVINCE fit

- **Inside the province.** `PROVINCE.md:3-7` owns reverse engineering of shipped artifacts including "Android APKs, archives, firmware", under an evidence-ledger discipline. `PROVINCE.md:17-18` states "server registration and engines are the lane's readiness domain". The candidate's eight route rows (ZIP, Ghidra, native-engine absence, JADX, firmware, MCP registration, CLI launcher, pwntools) are that readiness domain. No refusal at `PROVINCE.md:44-48` is touched.
- **Sibling-domain bleed (reported, not absorbed, Q10).**
  - `kaidoku-shokunin/PROVINCE.md` claims "native ELF through the Ghidra 12.1.4 provider" (`:3`), the Ghidra/JDK reverification (`:27`) and "archives and packages". The candidate's Ghidra and ZIP-inventory rows use the same provider and the same `inspect-artifact` verb on a revenger fixture. The candidate cites its own S507 records, not any kaidoku entry, so no kaidoku fact is absorbed.
  - kaidoku's drift-prone paragraph (`:15-19`) records an operator **disable** of the OMP `rea` entry; the candidate reports the same entry only as "stale" (§2 row 8).
- **Lane-own census the candidate does not supersede.** `PROVINCE.md:17-40` is the lane's host census (2026-10-31 / 11-01). It disagrees with the candidate on rea version (6.8.0), Ghidra location (a Windows path) and jadx/binwalk/unblob/pwntools presence (§2 row 20). `PROVINCE.md` is a frozen byte this round, so this seat does not recommend editing it; L1 should decide whether the census is superseded by the landing or kept as dated history. The census points to `corpus/knowledge/seed.md`, whose F08/F09 re-verification rows (`seed.md:92-93`) carry the same 11-04 facts as the candidate.

---

## 6. Recommendations for L1 / CriticR99 (nothing edited)

1. Decide whether §3.1 (PATH `ghidra` 12.1.2 and the `GHIDRA_INSTALL_DIR` dependency) requires an amendment before the v8 freeze. If not, record it as an open item in the entry body so the route verdict is read with its env dependency.
2. Name the 2026-11-04 section of `2026-10-12-rea-readiness-checklist.md` in the candidate's supersession sentence (§3.3).
3. Record the env-key **names** behind each "configuration" verdict (§3.2), no values.
4. Confirm rules R-a…R-i against legitimate r98 notes and the r98 holdout before any use. This seat did not run them.
5. The PROVINCE census (§5) is a dated-history question for L1.

---

## 7. Messages sent

- `ExecCounterV8`: reusable rules R-a to R-i with path:line (summary in §4.2). No other seat was messaged. No `agent://all` broadcast.

---

## 8. Verification record

- No counter, builder or harness was run on any landing tree, vote or corpus file of this lane.
- Exit codes observed: `command -v analyzeHeadless` → 1; `command -v hopper` → 1; `command -v ghidra` → 0; `command -v rea` → 0; `ls -l /usr/bin/ghidra` → 0; `ls /usr/bin/analyzeHeadless` → 2; `bare_id_check.py` on an S-id-less scratch file → 0 (vacuous, §1).
- Scratch `/fast/scratch/hyaku/revenger-r99/ConnectorR99/` was created for the vacuous test and removed (`rm -rf`) before this yield.

## 9. Open questions

1. Is the PATH `/usr/bin/ghidra` (12.1.2) meant to be in scope for the candidate's "one host" claim, or is it a host-config artefact outside C14?
2. Does L1 want the env-key names (§3.2) in the entry, given the candidate is frozen except for the admission-status line?
3. Is the `PROVINCE.md` census (§5) to be superseded by this round's landing or kept as history?
