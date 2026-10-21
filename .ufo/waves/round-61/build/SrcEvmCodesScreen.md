# SrcEvmCodesScreen — C09 source screen (read-only)

Seat `CloseChousa26.SrcEvmCodesScreen-10` · lane base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` · 2026-10-21 · no lane writes, no clone, no installs.

## Fetch

- URL opened: `https://www.evm.codes/` (homepage opcode table) plus `/#63`, `/#14`, `/#57`, `/#5B` and `/about`.
- `curl -sS -o /tmp/evmcodes.html -w 'HTTP:%{http_code} SIZE:%{size_download} CT:%{content_type} URL:%{url_effective}\n' -L --max-time 45 https://www.evm.codes/` → `HTTP:200 SIZE:1208389 CT:text/html; charset=utf-8 URL:https://www.evm.codes/`; second HEAD: `HTTP/2 200`, `etag: "cf495cdd198f35acf29e9b72011c2b3c"`, `date: Wed, 21 Oct 2026 15:47:20 GMT`, `server: Vercel`, `content-length: 1208389`. `/about` → `HTTP:200 SIZE:40602`.
- Opcode table and docs are client-rendered, so opened with `chromium --headless=new --no-sandbox --disable-gpu --virtual-time-budget=15000 --dump-dom 'https://www.evm.codes/#5B'` → exit 0, 1,466,680 bytes; `#14` 1,470,079, `#57` 1,468,789, `#63` 1,469,086 bytes (hash routing selects the opcode doc: the selected doc's text count rises by one, e.g. `#14` gives `left side integer` ×2 vs ×1 elsewhere).
- Page version/revision: title `EVM Codes - An Ethereum Virtual Machine Opcodes Interactive Reference`; `"buildId":"SnI4EiV4C4sZ8lujLV3M-"`. No publication date or version label displayed: rendered-DOM scan printed `2026 0`, `2025 0`, `last updated 0`. Revision is therefore the deployed buildId + ETag. Repo `duneanalytics/evm.codes` HEAD at access is `455302174aa034bd4aaf64321b79148046e9a60e` (2026-09-24, `api.github.com/repos/duneanalytics/evm.codes/commits?per_page=1`) — context only, not claimed as the deployed revision.
- Captures: sha256 `ad69f51c530aeaa7b0517641a63ea9b5a92a3c7f4dad5d355b012b570e59e1cc` (`/tmp/evmcodes.html`), `012269abae497613ee2e948a79b7afa08d8dfb9fe299055a1cc2b96b7475fd54` (`/tmp/evm_dom_63.html`), `21f7736cea2ab7df0b0e197d234db51034a0010377cb62e75277b4015a4deb18` (`/tmp/evm_dom_5b.html`).

## Quotes (verbatim, rendered DOM; inline links removed, spacing normalized)

1. 6 words — “Place 4 byte item on stack” — opcode table row `63` (PUSH4), Description column; row also reads Minimum Gas `3`, Stack Output `value` (headers extracted: `Opcode`, `Name`, `Minimum Gas`, `Stack Input`, `Stack Output`, `Description`).
2. 17 words — “counter: byte offset in the deployed code where execution will continue from. Must be a JUMPDEST instruction.” — `/#57` (JUMPI), heading **Stack input**, item 0.
3. 18 words — “Mark a valid destination for JUMP or JUMPI. This operation has no effect on machine state during execution.” — `/#5B` (JUMPDEST), heading **Notes**.

Each was matched as a raw-HTML regex allowing the page's inline `<a>` elements: `#5b` and `#57` printed `MATCH`, `#63`'s row and `#57`'s error sentence likewise. Detail headers read `Since` = `Frontier`, `Group` = `Push Operations` (0x63) and `Stack Memory Storage and Flow Operations` (0x57, 0x5B); EQ row reads `Minimum Gas` `3`, Stack Output `a == b`.

## Bearing on C09 (observed → inference → unknown)

- Observed bytes: `corpus/fixtures/evm-r19/fixture.hex:1` = `0x60003560e01c63deadbeef14601057005b00`; decode at offsets `06: PUSH4 0xdeadbeef`, `0b: EQ`, `0c: PUSH1 0x10`, `0e: JUMPI`, `10: JUMPDEST`. `corpus/fixtures/evm-r19/truth.json:8-10` records `push4_opcode_offset: 6`, `selector_immediate_offset: 7`, `selector_immediate_length: 4`.
- The page's stated mechanics apply exactly to those bytes: PUSH4 leaves a 4-byte value at 07–0a; JUMPI's counter here is `0x10`; byte `0x10` is the JUMPDEST marker (quote 3 says it is inert during execution).
- Inference for the entry (label as inference): a PUSH4 immediate is a 4-byte constant candidate, and a PUSH4→EQ→JUMPI path whose counter resolves to a JUMPDEST is a dispatch-shaped candidate. The page supports only the mechanics, never the naming.
- Unknown/limits: the page does not say a JUMPI counter is statically known (only that it is a byte offset which must be a JUMPDEST), so a computed counter makes a nearby PUSH4 non-decisive; its error text qualifies the invalid-counter error as raised only when the jump is taken (paraphrase, `/#57` Error cases bullet 3); gas is labelled `Minimum Gas` only.

## Proposed SOURCES.md row (11 columns; id TBD — sibling `SrcSolidityMetadataTail` also proposes S016, so use S017 if it lands first)

| S0NN | EVM Codes (An Ethereum Virtual Machine Opcodes Interactive Reference) — https://www.evm.codes/ | community | C | stack effect of PUSH4, EQ, JUMPI and JUMPDEST and the rule that a JUMPI counter must be a JUMPDEST, as the page states them; not selector, ABI or dispatcher semantics | opcode table row 63 and detail pages /#63, /#14, /#57, /#5B (Notes, Stack input, Stack output, Error cases), Since column Frontier for all four; deployed buildId SnI4EiV4C4sZ8lujLV3M-, HTTP ETag cf495cdd198f35acf29e9b72011c2b3c; no publication date displayed, accessed 2026-10-21 | Which stack effect each of the four opcodes has, that JUMPI's counter must name a JUMPDEST, that an invalid counter errors only when the jump is taken, and that JUMPDEST is inert during execution. | queued | 2026-10-21 | 90d | — |

Validated on a /tmp copy with the contract's census awk: `malformed: 0`, row count `1`, `tier=C status=queued kind=community`.

## What the source does NOT state

- No selector/ABI link: rendered homepage DOM and `/about` both print `selector 0`, `ABI 0`, `dispatch 0`, `interface 0`. Nothing ties a PUSH4 immediate to a function selector, specifies selector byte order, or describes a dispatcher/extraction procedure.
- No static-analysis method: nothing about scanning bytecode, resolving JUMPI counters from constants, or candidate ranking.
- No normative status: `/about` renders `Brought to you by Dune . Powered by EthereumJS and SolcJS .` — a Dune community project, not a standards body; no errata, version policy or publication date.
- Nothing about this lane's fixtures or REA output; it must never be cited as fixture evidence.
- It is `kind=community`, so contract v1 fixes tier at C; it can never be the tier-A anchor.

## Decision

Tier C lead, status `queued` — useful corroboration, **not admissible as C09's anchor** (Q01: a tier-C row is never sole support). Flip conditions: (1) if the round opens a tier-A normative opcode source for the same scope (Ethereum Yellow Paper Appendix H Virtual Machine Specification, or `ethereum/execution-specs` source), this row may be cited beside it and then moves to `mined`; (2) the selector half of C09 may not cite this row at all until an ABI source is opened — the page carries zero selector text. If neither lands, C09's entry must not use this row. Not recorded as `rejected` because that status would lose the corroboration value for a row whose opening cost is already paid.

## Search log line for `## Search log`

- 2026-10-21, C09 opcode semantics for PUSH4/EQ/JUMPI/JUMPDEST. Query: what the four opcodes do and whether any selector convention is stated. Where: evm.codes homepage, /#63, /#14, /#57, /#5B, /about (rendered DOM), repo duneanalytics/evm.codes at 4553021. Identified 1, screened 1, included 1 (tier C, queued), excluded 0. Negative sweep: 0 occurrences of selector/ABI/dispatch/interface. Stop: the page's own text opened in full; no normative source opened by this screen.

## Leads (unopened)

- Ethereum Yellow Paper Appendix H (Virtual Machine Specification) — the tier-A companion the C09 entry needs.
- `ethereum/execution-specs` — tier-A source code for opcode behavior.
- Solidity ABI specification — names and encodes the selector this page never mentions.

Installs: none (curl and chromium already present).

VERDICT: evm.codes opened HTTP 200 (buildId SnI4EiV4C4sZ8lujLV3M-, no displayed date) and states PUSH4's 4-byte stack item, JUMPI's JUMPDEST-mandatory counter and JUMPDEST's inert marker, so it is a tier C lead only: with zero selector/ABI text it cannot anchor C09, which still needs a tier-A opcode source plus the ABI spec.
