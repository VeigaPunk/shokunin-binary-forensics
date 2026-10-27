# CoreS062Review — radare2 source check

**Judgment: REVISE (S062 quote evidence); linked entry wording supported.**

## Evidence

Reopened the pinned public source at `https://raw.githubusercontent.com/radareorg/radare2/6ac96f50eafef46c1ac75a478a1460819968c66f/README.md` (10,644 bytes; SHA-256 `dc86af03a0eb92735a59fa18e397520a90d593683abd504d5f85f4f80db1b7c9`). Under `### Description` (README lines 16–18), it says:

> “The **radare** project started as a simple command-line hexadecimal editor focused on forensics. Today, r2 is a full-featured low-level command-line tool with support for scripting with the embedded Javascript interpreter or via r2pipe.”

The S062 quote in `corpus/SOURCES.md:76` and the lesson Gate at `corpus/lessons/round-72.md:21` instead give “Today, r2 is a full-featured low-level command-line hexadecimal editor.” That exact string is absent from the pinned README, including after whitespace normalization. It splices the prior sentence's “command-line hexadecimal editor” with the following “Today, r2 is a full-featured low-level command-line tool.” The locator `README.md “Description”` is correct, and the 11-word quote is within the 25-word limit, but it is not a located verbatim quote. The lesson Gate's statement that quotes are located is therefore not satisfied for S062; correct the quote to source wording (for example, end it with “tool”).

The documented scope itself is supported: the same section describes scripting via embedded Javascript/r2pipe, editing files, debugging locally or through remote servers, and analyzing/emulating/debugging/modifying/disassembling binaries. The entry `corpus/knowledge/round-72-tool-landscape.md` accurately limits its paraphrases to command-line binary analysis and hex/format/scriptable inspection, and explicitly says feature parity, correctness, licensing, and local provider readiness are not inferred. The SOURCES row also bounds edits/debugging as documented rather than work performed. No inference about installation, availability, accuracy, or execution is warranted.

S062 is marked `mined` and its `used-by` names `corpus/knowledge/round-72-tool-landscape.md` (`corpus/SOURCES.md:76`), so those linkage facts are present; this review does not adjudicate the overall C15 predicate. The frozen counter's stated predicate is row/entry/status linkage and citation counts, not quote verification, so the misquote is an evidence-quality/Gate defect, not evidence that this source row is absent from the counter's citation count.

**Verification limits:** GitHub API commit lookup was rate-limited. The raw URL at the pinned full commit hash returned the README bytes; its SHA-256 and size matched the separately fetched current `master` README, which also lacks the claimed quote. No LSP device was available in the provided tool inventory. No tool was installed or executed.
