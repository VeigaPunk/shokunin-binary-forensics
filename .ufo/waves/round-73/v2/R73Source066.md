# R73Source066 — S066 mitmproxy source audit

Seat: R73Source066 (reviewer, lane-internal). Assigned row: **S066 only**. No source admission or
registry edit performed; this report is the only write.

## Located quote (verbatim, ≤25 words)

> "mitmproxy is an interactive, SSL/TLS-capable intercepting proxy with a console interface for HTTP/1, HTTP/2, and WebSockets."

- Word count: **16** (within the ≤25 limit).
- Access date: **2026-10-30** (this seat's re-open).
- URL (exact cited pin): https://raw.githubusercontent.com/mitmproxy/mitmproxy/7458ea26ccec7d06ffdc434f878e8d92973aec7e/README.md

## Verbatim comparison (observation)

- The pinned raw README at commit `7458ea26ccec7d06ffdc434f878e8d92973aec7e` reads at its
  introduction (immediately after the title/badge block):
  ````mitmproxy`` is an interactive, SSL/TLS-capable intercepting proxy with a console
  interface for HTTP/1, HTTP/2, and WebSockets.````
- Normalizing markup only (RST-style double backticks around ``mitmproxy`` removed; the
  soft-wrapped line joined), the registry/lesson quote is an **exact verbatim substring** of the
  pinned source. No paraphrase, no drift.
- The same sentence is present in current `main`'s README (re-checked 2026-10-30), so the quote
  is stable across the pin and HEAD.
- The pin itself resolves: GitHub API reports commit `7458ea2…` (author Maximilian Hils,
  2026-04-12, "remove codacy badge"; commit page HTTP 200). This round-72 seat's earlier note
  that commit metadata was unchecked due to rate limiting is now closed for S066.

## Registry row, lesson, entry wording (observation)

- `corpus/SOURCES.md` line 80, S066: 11 cells; kind `tool`, tier `A`; scope "The project's own
  declared HTTP/TLS/WebSocket interception purpose; not authority to inspect any live
  traffic"; anchor cites README introduction, commit `7458ea2…`, accessed 2026-10-27, with the
  quote above; status `mined`, opened `2026-10-27`, recheck `on-release`,
  used-by `corpus/knowledge/round-72-tool-landscape.md`.
- Lesson `corpus/lessons/round-72.md` line 25 (S066): quote matches the registry verbatim;
  decision "ADMIT, tier A for documented network-interception role only; no traffic was
  intercepted." The lesson quote is verbatim-correct — unlike the routed defects below.
- Entry `corpus/knowledge/round-72-tool-landscape.md` line 29 cites "mitmproxy S066" and
  paraphrases ("interactive TLS-capable proxy for HTTP/1, HTTP/2 and WebSockets") with boundary
  "This is a live interception surface, not a passive claim about saved records. Do not point
  it at an undeclared or third-party target." Entry Scope states dynamic/traffic tools "none
  was run"; header states "No tool was installed or executed."

## Scope / tier / used-by / rejection-flip assessment

- **Scope:** observation — agrees with the source. The README's own words establish exactly the
  declared interception purpose and nothing more; the row's "not authority to inspect any live
  traffic" correctly fences it.
- **Tier A:** observation — correct; this is the project's own primary README.
- **Used-by:** observation — matches; the C15 entry names S066 and stays inside the row's scope.
- **Rejection flip:** S066 was ADMITTED with no flip condition in the lesson Gate. No flip to
  evaluate for this row. S071/S082 carry the round-72 routed quote defects
  (`corpus/lessons/round-72-verifier-spotcheck.md`): S071 registry quote is a paraphrase
  ("Each repo is read and security-graded" vs pinned "each one read and security-graded"), and
  S082's located quote is misattributed (it is S083/AutoDecompiler's text). Per seat bounds I
  report only S066 and propose no superseding rows here; those defects belong to their assigned
  seats (R73Source071, R73Source082), which must append NEW superseding rows and never edit the
  old ones.

## Disposition

**Agree** with the source disposition: ADMIT, tier A, documented network-interception role only.
The quote is verbatim at the cited pin, the pin exists, the row/lesson/entry are mutually
consistent, and the scope fence is honest.

## Residual risk / unknowns

- [OBSERVATION] All quote, pin, and cross-reference checks above were re-executed by this seat
  on 2026-10-30.
- [INFERENCE] The entry's compression "TLS-capable" for "SSL/TLS-capable" is harmless given the
  boundary cell; same judgment as the round-72 review, now reconfirmed against the pin.
- [UNKNOWN] None remaining for S066. (Round-72's open item — commit author date unchecked due
  to rate limiting — is resolved above.)

## Network / source failures

None. raw.githubusercontent.com and api.github.com both responded (HTTP 200). No rate limiting
encountered this seat.

## Tooling

No installs or updates. Used system `curl` and `python3` only (pacman pause honored; nothing
installed via any channel).

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source066/` cleaned after this report was written.

Report: .ufo/waves/round-73/v2/R73Source066.md
