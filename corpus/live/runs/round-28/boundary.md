# Round 28 boundary — one-byte payload-control comparison

## Observed comparison

The round-27 baseline is a 1,024-byte hand-built PE32 fixture with one RT_RCDATA resource (type 10, name 1, language 1033). Its payload occupies file offset 600 for 15 bytes and hashes to `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa`. Round 28 truth records an exact copy except byte 600 changed from `0x52` (`R`) to `0x53` (`S`); the payload becomes `SEV-R27-PAYLOAD`, with hash `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. Both inspections report the same PE32 structure and resource identity, offset, and length; the payload digest changes accordingly.

## What this comparison supports

Given the authored fixture truth and the two static inspection records, this controlled pair supports that a one-byte change inside the payload is reflected in the reported payload digest while the observed resource mapping and surrounding inventory remain invariant. The authored construction attributes the difference between these fixture versions to that byte. This is evidence about this parser operation on these two shipped fixture artifacts, not a general proof of parser correctness.

## What it does not support

It does not establish that the changed byte has any particular application meaning, that the payload is decoded or consumed, that Windows or another runtime loads it, or that program behavior changes. The inspection explicitly treats non-`RT_GROUP_ICON` payloads as opaque. It does not test one-byte changes in headers, resource directory structures, other PE variants, malformed inputs, or other providers. Nor does a hash difference alone prove a byte-level mapping; that attribution relies on the fixture's recorded authored truth and baseline.

## Scope / attribution hazard

The control is fixture-level attribution, not target-execution or behavioral attribution. Do not describe it as a live target test or as proof of runtime resource selection. At inspection time `git status --short` also showed `LOG.md` modified and round-28 fixture/run files untracked (all under `.shokunin/revenger/`); their prior ownership is unknown here. Keep any claim of changed scope limited to this boundary file, and do not stage or attribute unrelated dirty paths to this comparison without checking provenance.
