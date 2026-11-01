# Round 74 — quote-fidelity audit executed; carried C10 disposed by the frozen kill rule; province reconciled to this host

Fresh-start round on a new Windows host. Base `85db6abefae7b706cf5583ab24eefbcbd28a4f01`
(the inherited r74 freeze; instruments sha-verified unchanged:
`corpus/audit_source_quotes.py` `72c6938a7e27631f0e0c3ba280f8debe58377371e3b3e73b043e4f0dcc58743f`,
`reports/round-74/measure.py` `ff2e52bdd6705bfb3d1a2140451a8ab16416cbb57c9cebeeabb78d75296e4ea6`).
Declared claims: **C1 coverage** (new bounded criterion P — province surface accuracy,
`reports/round-74/province_probe.sh`) and **C2 calibration** (inherited frozen QA criterion —
source-registry quote fidelity over S054–S095 + the nine MANUAL rows, executed per the
unchanged freeze `reports/round-74/claims.md`). The inherited freeze's C1 (carried r73 C10
admission) was **ruled out as a declared claim**: its required 4-seat Q review cannot exist on
this host (no `.ufo/state/` dispatcher, no seat spawn surface — `ls /home/vgpnk` ENOENT), so a
do-nothing control reaches the identical outcome; the frozen kill rule was executed instead
(below), which is disposition, not an axis move.

## Gate

C10 disposition (frozen rule, not a claim): the round-73 counter over an archive of base
`85db6ab` printed `C10_HELD_BACKED=0/1`, `C10_Q_VOTES=0/16`, `C10_CANDIDATE_PIN=1/1`,
`C10_SOURCES=1/1`, exit 0 — the required review is unavailable, so per
`reports/round-73/claims.md` C1(r73) is falsified and the candidate
`corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md` keeps every byte except
`admission-status:` which changed `candidate` → `rejected` (this round, single-line edit).
README C10 stays `partial`. No repair-and-revote under that claim.

C2 (QA, quote fidelity): before (frozen `measure-before.log`, base `c7008577`): 51/51
unresolved, `QA_TARGET=no`. After (this round): 51 receipts + 51 raw bodies committed at
`.ufo/waves/round-74/quote-audit/`; frozen counter over the measured commit prints
`QA_VERIFIED=42/42`, `QA_MANUAL_VERIFIED=9/9`, `QA_VERIFIED_TOTAL=51/51`,
`QA_UNRESOLVED=0/51`, `QA_NEGCTRL=pass`, `QA_TARGET=yes` (output:
`reports/round-74/measure-after.log`). Criterion QA score 0.0 → 10.0. Receipts are
L1-authored and disclosed as such (`seat: revenger-r74-L1 (no seat surface on this host...)`);
the counter re-derives every verdict from committed bytes, and the negative control (S071's
historical drift quote absent from the S427 body) passed. Three bodies are derived texts with
the exact command named in `body_derivation` and the pre-derivation source committed alongside
(`raw/S081.orig.pdf`, `raw/S379.orig`, `raw/S381.orig`); the S442 body derives from a
27,645,192-byte PDF that is NOT committed (fetch URL, HTTP 200, length and metadata recorded in
the receipt; re-derivation is by public refetch + the named command).

C1 (P, province surface accuracy — new bounded coverage criterion, split recorded here):
before `reports/round-74/province-before.log` — exit 1, `PROVINCE_SURFACES_RESOLVED=4/11`,
`UNRECORDED_ABSENT=7`, `P_SCORE=3.6`; after `province-after.log` — exit 0, `11/11`, `0`,
`P_SCORE=10.0`. PROVINCE.md now verifies present (`rea` CLI 6.8.0 `rea --version` exit 0;
npx; bounty-triage MODULE; lane repo) or records dated absence for every surface it names
(REA skill dir; ghidra; ida; jadx; binwalk/unblob; pwntools; ~/Projects/gamez/research), and
the write-scope name is corrected to `fleet/shokunin-binary-forensics`. Boundary: this is
instrument-level coverage (the province record matching the real host); K stays 8/15 (5.3)
and F stays 5/8 — no coverage-map row moved, no admission is claimed.

### Opened sources and corrections (2026-10-31)

Every row below was opened this round by the audit fetch (curl, status evidence in the
row's receipt). Located quotes ≤25 words; full quote fidelity is mechanically re-derivable
from the committed receipt + body.

| row | URL/path/command and representation | located quote (≤25 words) | decision |
|---|---|---|---|
| S429 | raw.githubusercontent.com/mrexodia/ida-pro-mcp@c133c385/README.md | "I recommend using the [Official Hex-Rays IDA MCP Server](https://github.com/HexRaysSA/ida-mcp) instead!" | ADMIT correction; supersedes S057 (rendered-form quote not verbatim in raw bytes) |
| S430 | raw.githubusercontent.com/skylot/jadx@f2d8496/README.md | "Please note that in most cases **jadx** can't decompile 100% of the code, so errors will occur." | ADMIT correction; supersedes S058 (bold markers dropped) |
| S431 | raw.githubusercontent.com/radareorg/radare2@6ac96f5/README.md | "Today, r2 is a full-featured low-level command-line tool with support for scripting with the embedded Javascript interpreter or via r2pipe." | ADMIT correction; supersedes S062 — real misquote: "hexadecimal editor" belongs to the preceding sentence |
| S432 | raw.githubusercontent.com/x64dbg/x64dbg@ac4db12/README.md | "An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering of executables you do not have the source code for." | ADMIT correction; supersedes S063 (sentence ended early) |
| S433 | raw.githubusercontent.com/mitmproxy/mitmproxy@7458ea2/README.md | "``mitmproxy`` is an interactive, SSL/TLS-capable intercepting proxy with a console interface for HTTP/1, HTTP/2, and WebSockets." | ADMIT correction; supersedes S066 (backtick markers dropped) |
| S434 | raw.githubusercontent.com/dnSpyEx/dnSpy@de5a830/README.md | "dnSpyEx is an unofficial continuation of the [dnSpy](https://github.com/dnSpy/dnSpy) project which is a debugger and .NET assembly editor." | ADMIT correction; supersedes S068 — real misquote: reordered wording the source does not carry |
| S435 | usenix.org/conference/usenixsecurity22/presentation/burk (HTTP 200) | "Over 150 people participated, and we collected more than 35,000 code submissions, the largest manual reverse engineering dataset to date." | ADMIT correction; supersedes S080 (quote ended at a comma) |
| S436 | arxiv.org/abs/2509.14646v2 (HTTP 200) | "we construct a C-aligned \underline{\textbf{A}}bstract \underline{\textbf{L}}oop \underline{\textbf{T}}ree (ALT)" | ADMIT correction; supersedes S084 (TeX markup in the abstract source) |
| S437 | raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered@0220fbd/README.md | "**Search first.** Use the [website](...) or the [agent skill](...)." | ADMIT correction; supersedes S088 (bold/link markers dropped) |
| S438 | raw.githubusercontent.com/OWASP/mastg@41c6b74/README.md | "is a comprehensive manual for mobile app security testing and reverse engineering." | ADMIT correction; supersedes S094 — misquote: inserted leading "The"; title is bold |
| S439 | raw.githubusercontent.com/morluto/rea@447907f/docs/specs/agent-environments/README.md | "Start with the [quickstart](...) for a user workflow or the [reference](...) for current contracts." | ADMIT correction; supersedes S095 (markdown links dropped) |
| S440 | usenix.org/conference/usenixsecurity13/technical-sessions/presentation/schwartz (HTTP 200) | "existing structuring algorithms are not <em>semantics-preserving</em>, which means that they cannot safely be used for decompilation without modification" | ADMIT correction; supersedes S115 (<em> markup inside the sentence) |
| S441 | raw.githubusercontent.com/NationalSecurityAgency/ghidra@1b9e58a/GhidraDocs/languages/html/sleigh.html | "The main addition of SLEIGH is the ability to provide semantic descriptions of instructions for data-flow and decompilation analysis." | ADMIT correction; supersedes S131 (prior sentence interrupted by span markup; re-located markup-free) |
| S442 | docs.amd.com khub content API, document SLs_hsYJwsu9rrIjE0rGxA (HTTP 200, 27,645,192 B; pdftotext -f 1 -l 8) | "Reverse engineering or disassembly is prohibited." | ADMIT correction; supersedes S380 — revision drift: portal replaced rev 4.10 with rev 4.11 (Release_Date 2026-10-29) |
| S343 re-open | repositum.tuwien.at/handle/20.500.12708/150118 (HTTP 200; the record the row's own anchor names; doi.org and dl.acm.org both HTTP 403) | "many forms of lightweight static analysis have difficulties with even basic obfuscation schemes" | existing row's quote verifies at its registered location; no correction |
| S379 re-open | web.archive.org/web/20261023032601/https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html (live page HTTP 403 Akamai) | "The downloadable PDFs of all IA-32 Architectures Software Developer's Manual volumes are at version 093." | existing row's quote verifies after html.unescape derivation; no correction |
| S381 re-open | documentation-service.arm.com/documentation/ddi0487/latest (HTTP 200; developer.arm.com HTTP 403) | "In the event of any differences between the PDF and HTML versions, the PDF version shall be considered the authoritative reference." | existing row's quote verifies after base64 topic decode; no correction |
| S400 re-open | web.archive.org snapshot 20251231045737 (live page HTTP 403 Cloudflare) | "Reverse Engineering Stack Exchange is for researchers and developers who explore the principles of a system through analysis of its structure, function, and operation." | existing row's quote verifies at the snapshot the row names; no correction |

Registry touches beyond the appended rows (old → new, none else changed): S062 status
`mined` → `rejected`, teaches prefixed with the r74 reject reason naming S431; S068 status
`mined` → `rejected`, teaches prefixed, naming S434; S094 status `mined` → `rejected`,
teaches prefixed, naming S438. All three flips carry a located-quote-grounded reason and a
named successor (Q12). The three rejected rows' prior `used-by`
(corpus/knowledge/round-72-tool-landscape.md, a candidate entry, not admitted) is unchanged;
that candidate's source support degrades accordingly and its C15 disposition stays
`uncovered`/candidate as before.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| environment-drift freeze defect (inherited) | `reports/round-74/claims.md` names `/home/vgpnk/...` counter paths and `/fast/scratch/...`; `ls /home/vgpnk` → ENOENT on this host; no `.ufo/state/` dispatcher | this round's §7 fresh-start spot-check of the inherited freeze | Freeze-time reachability probe: a frozen counting command must run, or the freeze must pin a host-neutral invocation; this round documents the adapted invocations (`PYTHONUTF8=1 python -B ...`, workspace scratch) without changing any frozen byte (sha pins above) |
| locale-dependent text decode (inherited instruments) | first instrument run: `UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d` reading UTF-8 SOURCES.md (cp1252 default on this host) | first execution of the frozen instrument on this host | Interpreter UTF-8 mode (`PYTHONUTF8=1` / `-X utf8`) is the documented host invocation; instrument bytes unchanged and sha-verified; future instruments should pass `encoding="utf-8"` explicitly |
| rendered-vs-fetchable quote drift (registry-wide) | audit: 10 of 42 range quotes not verbatim in fetchable bytes — 2 real misquotes (S062, S068), 1 word insertion (S094), 2 early-period ends (S063, S080), 5 representation-only (S057, S058, S066, S084, S088, S095 class), plus markup-interrupted S115/S131 | the frozen QA criterion executed this round (the r73-verifier-spotcheck carry-forward) | Superseding rows S429–S442 with quotes recorded from the representation that is re-fetchable; row writers should record the quote from the bytes they can commit, not from a rendering |
| summary-line arithmetic drift (this round, self-caught) | first `province_probe.sh` red-before printed `RESOLVED=10/11` while listing 7 UNRECORDED-ABSENT lines (binary fail flag printed as a count) | inspection of the red-before before any after-run | per-surface `unresolved` counter; red-before re-taken after the fix (`province-before.log` shows 4/11, UNRECORDED_ABSENT=7) |

## Honest disclosures

- Receipts are L1-authored: this host has no seat/dispatch surface (`.ufo/state/` absent),
  so the declared 32-seat wave shape of the inherited freeze cannot run. The mechanical work
  (fetch, span, receipt) was done by the L1; every verdict is re-derivable from committed
  bytes via the unchanged frozen counter, and the counter's negative control passed. Outside
  re-derivation is the closure judge's.
- MISSION's L2 floor (≥8 subagents in one batched call) is not executable on this host; filed
  to `.ufo/l0-questions.md` and routed around, never treated as answered.
- Tool installs: none (curl/pdftotext/python only; pdftotext and curl preinstalled).
- pacman pause binds; no pacman transaction was touched.
