# Claim-set critique — C1–C3

## Axes and admission boundary

The distinct-axis assignment is viable, not automatic: C1 is **calibration**; C2 is **coverage** (with `sources-curation` as a possible separate capability, not an axis); C3 is **freshness**. `MISSION.md:40-51` allows a lane to add an axis on evidence, and `AXES.md:25-41,57-64` permits 1–3 distinct-axis claims and capability claims with an axis verdict. Therefore freshness is not forbidden, but it must be explicitly added in `SCORECARD.md` as a falsifiable move; its existing “not an assigned scoring axis” row (`SCORECARD.md:85`) cannot remain the final declaration.

C2 and C3 are causally separable only if C2 counts **new** knowledge files against coverage-map statuses frozen at base `8bbcb4e`, while C3 rechecks only the two pre-existing entries (`seed.md` and the readiness checklist). Do not make C3 depend on C2's new SOURCES rows, and do not include C3's edits to old entries in C2's expansion count. If either workstream adds/depends on the other's entries or mined status, the claims are not separately verifiable (`AXES.md:30-35`).

## HIGH — C1 is one calibration claim; do not replay the predecessor's gain

**Counterexample/evidence.** `verify_icon_languages.py` and `verify_multi_icon_states.py` are two failing verifiers for the same saved-ledger runnability criterion, not two distinct axes or independent claims. `AXES.md:27-35` says same-axis moves count as one claim. The predecessor already reported calibration `1/4 → 2/4` (`SCORECARD.md:9,17-20`); its C command is at `SCORECARD.md:34-42`. The current 2/4 baseline and failures are the provided C1 observation, consistent with that existing rubric. Counting from 1/4 again would double-count the predecessor; counting `REPLAY 8/10` as an extra gain would also mix the broader census with the selected calibration criterion (`SCORECARD.md:17-30`).

**Smallest safe correction.** Report one C1 calibration movement, **2/4 → 4/4**, with the unchanged four-script C command and both failing scripts fixed by the independent `ROOT`-for-bytes / `HIST`-for-expected-identity pattern (lesson `round-1.md:8,51`; `QUALITY.md:15`). Do not mutate fixtures or saved records. A claim is harmed if either verifier still fails, historical identity is rewritten to the current locator, or a previously rejected forgery starts passing. Any broader replay total remains descriptive, not another claim.

## HIGH — C2's new zero-base proxy is incremental expansion, not a new absolute coverage score

**Counterexample/evidence.** The current coverage score is the selected-family record-presence proxy, 4/8 = 5.0, and is explicitly bounded (`SCORECARD.md:10,21-24,45-56`). The SOURCES contract defines expansion as admitted knowledge entries citing mined rows on uncovered ground, not a SOURCES row count (`SOURCES-CONTRACT-v1.md:56-58`); `LEARNING.md:30-35` likewise requires net admitted entries on ground not held. A metric that filters to “entries added after base” necessarily has zero such entries at base. Calling that `coverage score 0 → N`, or replacing the existing 5.0 with it, manufactures a baseline rather than comparing like with like.

**Smallest safe correction.** Keep the existing selected-family coverage result unchanged; state C2 separately as an **incremental admitted-entry count**, `0 → N`, with the frozen base, eligible base-map rows, and SOURCES row identity in its command. Do not credit SOURCES.md's existence alone as coverage. The `sources-curation` capability may enter the capability table only if source opening/curation is demonstrated and evidenced in the round (`AXES.md:57-64`; `SOURCES-CONTRACT-v1.md:45-48`). If a newly admitted entry fails its admission bar, expansion with quality harmed is a trade, not a passing round (`LEARNING.md:30-35`).

**Contract ambiguity to resolve before scoring.** The requested count includes rows `uncovered` **or** `partial` at base, but the frozen SOURCES rule says `uncovered` without defining `partial` as equivalent (`SOURCES-CONTRACT-v1.md:56-58`; map definitions `corpus/README.md:18-22`). Report those two base-status buckets separately. The requested broader total is defensible only if `partial` is explicitly treated as ground the map did not yet hold; otherwise score only `uncovered` and list `partial` separately. Never decide eligibility from the post-C2 map.

## MEDIUM — base-map statuses understate pre-contract coverage

**Counterexample/evidence.** C06 is marked `uncovered` (`corpus/README.md:31`), but the pre-contract readiness entry states that ZIP/APK member inventory is available through `open_binary` (`knowledge/2026-10-12-rea-readiness-checklist.md:13`). Under the map's own definition, that is at least partial coverage by pre-contract text, even if it is only route/readiness knowledge. C13 is also `uncovered` (`README.md:38`), while `seed.md:31` already records fixture provenance fields including source, compiler, flags and SHA-256; that is partial provenance coverage, not coverage of the whole digest/receipt-vs-origin surface. These are concrete reasons not to treat the base status as an objective zero.

**Smallest safe correction.** Treat C06 and the provenance sub-surface of C13 as `partial` in the base-status audit (or document the narrower surface boundary that excludes those statements). Keep C04 uncovered: `seed.md:34-39` mentions JS/Electron only as a candidate investigation, not as established package-analysis knowledge. The frontier rows C03/C05/C07/C08 similarly should not be promoted merely because readiness/planning text names unavailable tools; those notes are not demonstrated surface knowledge (`README.md:28,30,32-33`; checklist `:11-12`). Pin the corrected interpretation without rewriting the base used by the count.

## MEDIUM — C3 may add freshness, but “unscored” is not score zero

**Counterexample/evidence.** The prior scorecard explicitly leaves freshness unassigned (`SCORECARD.md:85`); both pre-contract knowledge files lack the required `source:`, `verified-at:` and `recheck:` headers at the base (`README.md:47-48`; `QUALITY.md:14`). A dated probe can add a freshness move, because freshness is an axis and the mission permits evidence-backed axis changes (`AXES.md:14,25-35`; `MISSION.md:49-51`). It does not justify claiming the whole axis went from score 0 to a higher mastery score.

**Smallest safe correction.** Define the bounded measure as “pre-existing entries live-rechecked this round”: `0/2 at frozen base → N/2`, with the dated command/citation and observed result recorded for each entry; report the axis as previously unscored, not as a global zero. Mark stale facts and correct or explicitly flag them. A header-only date is not a probe. If any fact is found stale and left unmarked, quality is harmed (`LEARNING.md:31`); that can trade against C2's expansion.

**Causal-separation check.** C3 stays independent if it re-verifies the old entries from direct commands/citations and C2 only adds the new entries and their sources. If C3 needs a C2-created S-row, or C2's count includes the old files C3 edits, fix the boundary before claiming both. The C3 header census command below is only a census: the per-entry live results remain the evidence, not the date string.

## MEDIUM — QUALITY is grounded; preserve the exclusions and outside-check rule

Every Q row in `corpus/QUALITY.md:11-22` points to an existing mistake class in `corpus/lessons/round-1.md:38-56`: Q01/M17, Q02/M18, Q03/M06+M14, Q04/M02, Q05/M01+M19, Q06/M04+M05, Q07/M07+M12, Q08/M08–M10, Q09/M11+M13, Q10/M15. No criterion is lesson-less. M03 and M16 are explicitly `none` because they are process/admission rules, not padding (`round-1.md:40,53`); the stated census and command are at `round-1.md:58-59`. No Q-to-lesson correction is indicated.

Criterion census command (run from the lane root): `awk -F'|' '/^\| Q[0-9][0-9] /{n++} END{print n+0}' corpus/QUALITY.md`.

However, C2's gate still needs the learning-path outside sample: at least one admit and one reject with reasons (`LEARNING.md:39-45`). The dispatched `RevReviewer` is part of this lane (`.ufo/waves/kaika-r1/dispatch.md:17-20`), so its report is not the required non-author spot-check. Use an operator or genuinely external reviewer, or leave discernment unchanged; do not present the L2 review as independent.

## Proposed counting commands

Run both from the lane root. C2 pins the base map, counts only knowledge paths absent at base, and requires a source row marked `mined` whose `used-by` names that entry. It returns paths as well as the count so admission and status errors are auditable. The `partial` inclusion is the requested broader interpretation; report it separately from `uncovered` until the frozen-contract ambiguity above is resolved.

```sh
python3 -B -c 'import pathlib,re,subprocess
base="8bbcb4e"
readme=subprocess.run(["git","show",base+":corpus/README.md"],check=True,capture_output=True,text=True).stdout
base_status={}
for line in readme.splitlines():
 c=[x.strip() for x in line.split("|")]
 if len(c)==7 and re.fullmatch(r"C[0-9]+",c[1]) and c[-2] in {"uncovered","partial","held","frontier"}: base_status[c[1]]=c[-2]
rows={}
for line in pathlib.Path("corpus/SOURCES.md").read_text().splitlines():
 c=[x.strip() for x in line.split("|")]
 if len(c)==13 and re.fullmatch(r"S[0-9]{3,}",c[1]): rows[c[1]]=(c[8],{x.strip() for x in c[11].split(",") if x.strip() and x.strip()!="—"})
counted=[]
for p in sorted(pathlib.Path("corpus/knowledge").glob("*.md")):
 rel=p.as_posix()
 if subprocess.run(["git","cat-file","-e",base+":"+rel],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0: continue
 text=p.read_text()
 m=re.search(r"(?m)^coverage-map:\s*(C[0-9]+)\s*$",text)
 s=re.search(r"(?m)^source:\s*(.*)$",text)
 if not m or base_status.get(m.group(1)) not in {"uncovered","partial"} or not s: continue
 ids=set(re.findall(r"\bS[0-9]{3,}\b",s.group(1)))
 if any(i in rows and rows[i][0]=="mined" and rel in rows[i][1] for i in ids): counted.append((base_status[m.group(1)],rel))
print("C2 eligible new entries",len(counted))
for status,rel in counted: print(status,rel)'
```

C3 counts the dated metadata on the exact pre-existing entries; independently confirm each live recheck command/citation and its result in the round evidence before assigning the verdict. `0/2` is a round-level recheck baseline, not the freshness-axis score.

```sh
python3 -B -c 'import re
from pathlib import Path
entries=("corpus/knowledge/seed.md","corpus/knowledge/2026-10-12-rea-readiness-checklist.md")
checked=0
for name in entries:
 text=Path(name).read_text()
 ok=bool(re.search(r"(?m)^source:\s*\S",text) and re.search(r"(?m)^verified-at:\s*2026-10-19\s*$",text) and re.search(r"(?m)^recheck:\s*\S",text))
 print(name,"dated-recheck-metadata" if ok else "missing-dated-recheck-metadata")
 checked+=ok
print("C3 dated-recheck metadata",checked,"/",len(entries))'
```