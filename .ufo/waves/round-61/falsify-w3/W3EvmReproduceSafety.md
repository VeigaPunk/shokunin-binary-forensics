GRADE: HOLDS — C09 `## Reproduce` safety (script-level data-I/O contract)

Axes checked: imports/dependencies; project-data reads; filesystem writes; EVM execution; network; output fidelity.

Finding H1 — no block-level safety defect found.
- Severity: none. Exploit path: none in the block. Impact: no mutation or external effect observed. Smallest remediation: none for this block.
- Static evidence: `corpus/knowledge/evm-saved-interface-candidates.md:104-137` imports only `hashlib`, `json`, and `pathlib`; data paths are `corpus/fixtures` and `corpus/live/runs` (107); reads are fixture `.read_bytes()` (112) and record `.read_text()` (130, 135). The remainder hashes/decodes in-memory bytes, walks opcode values, selects JSON fields, and prints; no process, network, or EVM runner API is used. The walk at 114-129 inspects bytes; it does not execute EVM bytecode.
- Dynamic evidence: extracted commit `ab580698212258a55e43e9bb9bf6ac78c91eae2a` to `/tmp/revenger-r61w3-W3EvmReproduceSafety` and ran the copied `## Reproduce` body from that archive root with Python 3.14.8 under strace 7.2. Exact run: `strace -f -yy -e trace=%file,%network,read,pread64,readv,write,writev ... python3 -B .../reproduce.py`. Exit 0; stderr 0 bytes; stdout 2,099 bytes. `cmp -s` against the `## Provenance` block at entry lines 145-159 returned 0 (byte-identical).
- Trace evidence: `trace-io.log:507-595` shows fixture and `round-{19,21,22,23,24,25,26}/inspection.json` opens/reads, all under the two stated corpus roots; record JSON is read twice per case. The only process writes during the run are `print` output to captured stdout in `/tmp/.../stdout-io.txt` (e.g. 513-519); no filesystem mutation syscall was observed (0 matches for create/truncate/append/rename/unlink/mkdir/chmod/chown), and no socket/network syscall was observed (0 matches). No writes occurred in the extracted archive.
- Scope caveat: the Python interpreter itself also opens host runtime files during startup/imports (e.g. `/usr/lib` and `/etc`; trace lines 1-93, including a system `distutils-precedence.pth`). Thus “reads only corpus/fixtures and corpus/live/runs” is confirmed for the block’s project-data reads, not as a process-wide OS file-access allowlist. The block itself imports only stdlib modules.

Installs/updates: none; strace 7.2 was already present.
VERDICT: HOLDS — the reproduce block is stdlib-only, reads only the specified corpus inputs as project data, writes no files, executes no EVM bytecode, opens no network, and reproduces the recorded output exactly.
