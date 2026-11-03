# Consider these: ZIP reader mode and evidence

**Status: unassimilated future reading after hyaku.** Primary sources checked 2026-11-03 UTC. Source candidate only, not a training round, admission or readiness claim. No candidate software, binaries, live targets or private artifacts were run, tested or uploaded.

## libarchive: seekable versus streaming ZIP

**Original summary.** libarchive registers separate streaming and seeking ZIP readers. Its seeking reader uses the central directory and receives preference when available; the streaming reader disables Mac-extension processing. Consequently, a ZIP inventory needs its input mode and parser path recorded, not just a tool name. A successful listing alone cannot establish that every metadata surface was considered.

**Exact source.** [Source snapshot 2774b74cb7269c9b5fa89e7d876b11d5a729c421](https://github.com/libarchive/libarchive/commit/2774b74cb7269c9b5fa89e7d876b11d5a729c421), committed 2026-11-03T07:34:02Z. The commit concerns FILE-stream seek recovery. This is a development-source pin, not a released-build or installed-tool claim.

**Reading path.** Read ZIP support in [archive_read_format.3](https://github.com/libarchive/libarchive/blob/2774b74cb7269c9b5fa89e7d876b11d5a729c421/libarchive/archive_read_format.3), then [archive_read_support_format_zip.c](https://github.com/libarchive/libarchive/blob/2774b74cb7269c9b5fa89e7d876b11d5a729c421/libarchive/archive_read_support_format_zip.c): `archive_read_support_format_zip`, the streamable initializer, `read_eocd` and the seekable bidder. Compare documented dispatch with the implementation's metadata boundary.

**Future question.** After hyaku, consider a paper-only review of an already authorized archive inventory: was the source seekable, was a central-directory view available, and which metadata remained unexamined? Could a missing Mac metadata observation arise from reader mode rather than absent bytes? Keep expected observations separate from any future tool output. Do not convert a library's capability list into a claim about an existing report without identifying its actual input route.

**Limits and rights.** No archive extraction, decompression, sample downloads or parser execution here. This is not an independent replacement for PKWARE's format specification. [COPYING](https://github.com/libarchive/libarchive/blob/2774b74cb7269c9b5fa89e7d876b11d5a729c421/COPYING) makes individual-file notices controlling; the linked manual and ZIP reader carry two-clause BSD terms, while other distribution files have exceptions. Preserve applicable notices before reuse.

**Novelty.** No libarchive/bsdtar family match in the reviewed inventories and prior notes. Existing ZIP layouts and diffoscope comparison are related; input-mode-dependent metadata coverage is the distinct practical gap.

Any later adoption requires independent review after hyaku. No training or deployment changes.
