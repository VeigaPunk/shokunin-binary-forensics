# Scout — SOURCES contract v1 + sources-census: what a new row S016+ must satisfy
Read-only seat: no production edits, no clone, no installs. Bases: `/home/vgpnk/Projects/shokunin/CORPUS.md`
(contract v1, frozen 2026-10-19) and `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (maintained parser).

Observed lane state (commands run 2026-10-21, read-only, lane untouched):
- `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `15`; max id `S015`.
- `bash scripts/sources-census.sh validate --file …/revenger-shokunin/corpus/SOURCES.md --today 2026-10-21`
  → `file<TAB>ok<TAB>/home/…/corpus/SOURCES.md`, `rc=0`.
- recheck histogram (awk on column 11) → `on-release=6 180d=6 90d=3`.
⇒ Next free ids are **S016** and **S017**; both rows append inside the single `## Registry` after S015.

## A. Every rule a new row must satisfy (contract line → machine check)
| # | rule | contract | machine check |
|---|---|---|---|
| 1 | id = `S` + 3 or more digits, next unused, never reused | CORPUS.md:89 | E02 :640; E03 :641 |
| 2 | no pipe character inside any cell | CORPUS.md:89 | E01 :634-636 (11 cells ⇒ NF=13; a stray pipe yields fields>11) |
| 3 | source = title — canonical URL or DOI; `own-work` = repo path or command | CORPUS.md:90 | none (URL only harvested :600-606 for E04/W04/shared) |
| 4 | kind ∈ spec·docs·paper·code·tool·dataset·talk·book·community·own-work | CORPUS.md:91-92 | E05 :655-656 |
| 5 | tier ∈ A·B·C, **scoped to `scope`**, never global; C never sole support | CORPUS.md:93-97 | E06 :657; W01 :669-670; scope-fit NOT checked |
| 6 | `community` is never tier A | CORPUS.md:97 | E10 :668 |
| 7 | scope = the claim or topic the tier applies to | CORPUS.md:98 | only as the E04/W04 key :643 |
| 8 | anchor = section/heading/page/line **plus revision**; never a bare homepage | CORPUS.md:99-100 | none — anchor parsed :627, never inspected |
| 9 | teaches = one grounded benefit; rejected rows read `REJECTED: <reason>; flip: <what would change the verdict>` | CORPUS.md:101-102 | W02 only (length<8) :671-672; format unchecked |
| 10 | status ∈ queued·mined·rejected | CORPUS.md:103-104 | E07 :658-659 |
| 11 | `mined` ⇒ used-by names ≥1 repo-relative path that exists on disk | CORPUS.md:103,107-108 | E11 :566-567 (called :721); W03 :673-674 for `—` |
| 12 | used-by is comma-separated (or `—`) | CORPUS.md:108 | E11 splits on `,` only :562 — a `;` rides into the path and fails |
| 13 | opened = ISO date the author opened it; not future | CORPUS.md:105 | E08 :660-662 vs UTC today :90 |
| 14 | recheck = ISO date, `NNd`, or symbolic cadence (`on-release`) | CORPUS.md:105-106 | E09 :663-666; symbolic regex :582 (`90 days` fails) |
| 15 | row sits in `## Registry`, heading text exact | CORPUS.md:76-86 | E12 :618-623; exact match :609-611 |
| 16 | no duplicate URL+scope unless a rejected pair or teaches contains `supersedes S###` | CORPUS.md:116-118 | E04 :643-649 |
| 17 | same URL under a different scope is allowed (warning only) | CORPUS.md:116-118 | W04 :644-645 |
| 18 | append-only: only status/recheck/used-by change in place, each logged old→new in the round lesson | CORPUS.md:116-117 | none |
| 19 | row written only after opening the source that round; Gate records URL, access date, ≤25-word quote + location | CORPUS.md:112-115 | none beyond E08 |
| 20 | no credential material, session/private URLs, `op://` | CORPUS.md:129 | none |
| 21 | 0-3 leading spaces on table rows; 4+ is indented code and ignored | CORPUS.md:152-156 | :540-541, :615-616 |
| 22 | one search-log note per bounded search; a lead is never a row | CORPUS.md:83, 126-128 | none |

## B. Validator check codes (all sites in scripts/sources-census.sh)
- **E01** malformed row, NF≠13, prints `fields=NF-2`, then `next` skips E05-E10 — :634-639.
- **E02** id not matching `^S[0-9]{3,}$` — :637 (inside E01 branch) and :640.
- **E03** duplicate id — :641.
- **E04** duplicate URL within the same scope absent `supersedes S[0-9]{3}`; a `rejected` row never arms the check — :643-649.
- **E05** kind enum violation — :655-656. **E06** tier not A/B/C — :657.
- **E07** status not queued/mined/rejected — :658-659.
- **E08** opened not a real calendar ISO date or later than UTC today — :660-662.
- **E09** recheck neither valid ISO date, nor `^[0-9]+d$`, nor symbolic — :663-666.
- **E10** tier A on a `community` row — :668.
- **E11** `mined` row's used-by path absent under lane root (`--file`: dir is `dirname/..`, :501-502), checked :566-567, invoked :721; `—` skipped.
- **E12** `S###`-shaped row outside `## Registry`; detector needs an `S`+3-digit id — :618-623, :619.
- **W01** tier C + mined + a real used-by — :669-670. **W02** rejected with teaches <8 chars — :671-672.
- **W03** mined with used-by `—` — :673-674. **W04** same URL in another scope — :644-645.
- Exit: any E finding ⇒ 1; W only ⇒ 0; missing registry/unlisted-lane warning does not fail; bad gawk ⇒ 2 (header :16-18, selftest :157-161).

## C. Landing constraints for the C04/C09 rows
1. E11 makes `mined` unrepresentable before its evidence exists — land the knowledge entry first, or land the row
   `queued` and flip it to `mined` with used-by in the same round, logging old→new (CORPUS.md:116-117).
2. `used-by` stays lane-relative even under `--file` (:501-502); list every citing entry, comma-separated.
3. E01 short-circuits E05-E10 for the same row, so fix column count before chasing enum errors.
4. `opened` is judged against **UTC** (:90): a local-date write past local midnight in a negative-offset zone trips E08.
5. A clean `validate` is necessary, not sufficient: anchor quality, the ≤25-word Gate quote, the credential ban, and
   tier-fit for the claim's own scope (QUALITY.md:13 Q01) are review-only.

## D. Unknowns / not exercised
- Read-only seat, no mutant run: the E01 short-circuit, `;`-in-used-by and cross-scope W04 behaviour are code-derived,
  not executed (inference, high confidence from awk control flow :634-676 and the selftest assertions :130-160).
- The 0-3 space indentation path was not executed here (asserted by the script's own indent selftest :286-345), and
  whether round 61 writes each row `mined` or `queued` is the writers' call.

VERDICT: Contract v1 imposes 22 row rules and the validator machine-checks 12 E + 4 W codes at the cited lines; 8 rules are review-only (source shape, anchor quality, teaches format/quote, append-only logging, opened-in-round Gate quote, credential ban, search-log/leads, and tier scope-fit beyond the A/B/C enum); next ids are S016 and S017 and the live registry validates clean at 15 rows.
Installs: none.
