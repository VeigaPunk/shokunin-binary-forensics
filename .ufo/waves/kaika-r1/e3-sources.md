# e3 sources — ExecForensicKnowledge (kaika round-1, 2026-10-19)

Proposed `corpus/SOURCES.md` rows in the frozen 11-column format
(`SOURCES-CONTRACT-v1.md:19-21`), using temp ids `T3-*`; L1 assigns S-ids at
assembly. All URLs opened 2026-10-19 in this session; fetched text treated as
data, no instruction-like content observed. The w1 `revenger-art.md` dossier
named leads S005–S019 but recorded no registry table or URLs, so each lead was
re-located and re-opened from scratch.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| T3-1 | SWGDE Minimum Requirements for Testing Tools Used in Digital and Multimedia Forensics — https://www.swgde.org/wp-content/uploads/2024/04/2024-03-07-SWGDE-Minimum-Requirements-for-Testing-Tools-Used-in-Digital-and-Multimedia-Forensics-18-Q-001-2.1.pdf | spec | A | function-scoped tool testing requirements and test documentation fields | §§2, 4, 5.3, 6, Appendix A; rev 2.1 2024-03-07 | Testing is organized by tool function and category with testing type, frequency and tester per row; results record anomalies and limitations rather than pass/fail. | mined | 2026-10-19 | 180d | corpus/knowledge/tool-validation-by-function-and-version.md |
| T3-2 | NIST CFTT Methodology Overview — https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt/cftt-general-0 | docs | A | CFTT methodology structure as the page states it | "Methodology Overview", page updated 2026-05-01 | CFTT testing is functionality driven; each category gets a requirements/assertions/test-cases specification, public comment, and a steering-committee and vendor reviewed report. | mined | 2026-10-19 | 180d | corpus/knowledge/tool-validation-by-function-and-version.md |
| T3-3 | SWGDE Best Practices for Computer Forensic Acquisitions — https://swgde.org/wp-content/uploads/2025/09/2025-08-05-Best-Practices-for-Computer-Forensic-Acquisitions-17-F-002-2.1.pdf | spec | A | acquisition verification scope and acquisition documentation fields | §8 "Verification and Preview", §9 "Documentation"; rev 2.1 2025-08-05 | Verification compares acquired-data and acquisition-stream hashes but might not cover all source data; documentation lists tool version, hash values and acquisition errors. | mined | 2026-10-19 | 180d | corpus/knowledge/digest-scope-versus-provenance.md |
| T3-4 | NIST FIPS PUB 180-4 Secure Hash Standard — https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf | spec | A | what a message digest computes and the standard's applicability | Announcement §3 Explanation, §6 Applicability, Abstract; August 2015 | A digest is output on the supplied message and detects message change; the standard defines hash behavior, not provenance or completeness. | mined | 2026-10-19 | on-release | corpus/knowledge/digest-scope-versus-provenance.md |
| T3-5 | DHS S&T NIST CFTT test report index — https://www.dhs.gov/science-and-technology/nist-cftt-reports | docs | A | index organization only, as the page states it | "CFTT Reports" body text, opened 2026-10-19 | Reports are organized by tool category and publication date newest to oldest; no individual report was opened so nothing further is claimed. | queued | 2026-10-19 | 180d | — |
| T3-6 | RFC 3227 Guidelines for Evidence Collection and Archiving — https://www.rfc-editor.org/rfc/rfc3227.txt | spec | A | sysadmin-facing incident evidence collection guidance as published | Abstract, §1, §3.2; RFC 3227 February 2002 | REJECTED: 2002 IETF BCP written for system administrators, predates current device- and jurisdiction-specific acquisition guidance (17-F-002 supersedes its role here); flip: cite only for its still-current volatility-ordering concept if a lane entry needs that specific primitive | rejected | 2026-10-19 | — | — |

## Gate

Per contract rule 1: every row's URL, access date, and a ≤25-word quote with
location grounding `teaches`. All opened 2026-10-19.

- T3-1 `https://www.swgde.org/wp-content/uploads/2024/04/2024-03-07-SWGDE-Minimum-Requirements-for-Testing-Tools-Used-in-Digital-and-Multimedia-Forensics-18-Q-001-2.1.pdf` — "This document bases its testing baseline recommendations on the function of the tool, not on the tool origin." (18-Q-001-2.1, §4 General Discussion, p.3)
- T3-2 `https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt/cftt-general-0` — "The testing methodology developed by NIST is functionality driven." ("Methodology Overview", first paragraph)
- T3-3 `https://swgde.org/wp-content/uploads/2025/09/2025-08-05-Best-Practices-for-Computer-Forensic-Acquisitions-17-F-002-2.1.pdf` — "The process of verification might not verify all data as read from the subject media." (§8 Verification and Preview, p.9)
- T3-4 `https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf` — "This Standard specifies secure hash algorithms - SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256 -" (Announcement §3 Explanation, p.iv)
- T3-5 `https://www.dhs.gov/science-and-technology/nist-cftt-reports` — "Reports, organized by tool category, can be accessed and downloaded via the links below." (body text under "CFTT Reports" heading)
- T3-6 `https://www.rfc-editor.org/rfc/rfc3227.txt` — "The purpose of this document is to provide System Administrators with guidelines on the collection and archiving of evidence" (Abstract)

## Search log

- Question: what authoritative guidance scopes tool validation to function/version, and what bounds a digest's claim, for coverage rows C12/C13.
- Where searched: w1 lead dossier `kaika-w1/revenger-art.md` (rows named, no URLs recorded), then direct location of each named source — swgde.org publication pages (which redirected to `documents/published-complete-listing/` and exposed wp-content PDF links), nist.gov CFTT section, nvlpubs.nist.gov, dhs.gov, rfc-editor.org, iso.org.
- Identified 7 candidates (SWGDE 18-Q-001, SWGDE 17-F-002, NIST CFTT landing, NIST CFTT methodology overview, FIPS 180-4, DHS CFTT report index, RFC 3227; plus ISO/IEC 27042 catalog page as an 8th attempt).
- Screened 7 opened, 1 unopenable (iso.org/standard/44118.html returned HTTP 403 — per the assignment it remains a lead, not a row).
- Included as rows 6: four mined by the two entries (T3-1..T3-4), one queued index (T3-5), one rejected (T3-6). Excluded: ISO 27042 catalog (403, could not be opened); the NIST CFTT landing page was read but subsumed by the methodology overview (not a separate row to avoid duplicating scope); individual CFTT test reports (none opened; without opening, scope could not be honestly stated).
- Stop rationale: the four named leads required for C12/C13 claims were opened in full text (PDF) or authoritative page form; additional mining would exceed the two-entry scope of this executor.

## Leads (unopened)

- ISO/IEC 27042:2015 catalog page https://www.iso.org/standard/44118.html — HTTP 403 on 2026-10-19; lead only.
- Individual CFTT test reports and raw test files (index at T3-5; also https://www.nist.gov CFTT "CFTT Raw Test Files" section) — not opened.
- SWGDE 18-F-002-2.0 Best Practices for Digital Evidence Collection — referenced by 17-F-002 §9 for chain-of-custody transfer fields; custody is a separate frontier surface, not mined here.

## Paths

Study order: T3-1 → T3-2 → T3-5 → T3-3 → T3-4 (and T3-6 only as historical context). Start with lab testing requirements organized by function, then the CFTT methodology that instantiates it, the report index for finding version-scoped reports, then acquisition verification scope, and finally the digest specification for the byte-binding boundary.
