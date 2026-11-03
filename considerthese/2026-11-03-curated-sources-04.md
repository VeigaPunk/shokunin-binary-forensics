# Consider these: sparse image spans and byte evidence

**Status: unassimilated reading after hyaku.** Official source checked 2026-11-03 UTC. Source reading only; no image was downloaded, expanded, flashed or executed.

## AOSP libsparse: input bytes versus output blocks

**Original summary.** Android's sparse-image chunk header counts output blocks separately from encoded input bytes. RAW chunks carry their represented data; FILL chunks carry a four-byte pattern. DONT_CARE chunks have no payload, while checksum accounting can treat their represented span as zeros. A declared output span therefore does not establish an equal span of stored input bytes or observed device contents.

**Exact source.** AOSP `android-16.0.0_r1` resolves to [commit 68be0c2c0006a0740d0b1809abe4717308f90d15](https://android.googlesource.com/platform/system/core/+/68be0c2c0006a0740d0b1809abe4717308f90d15), committed **2025-04-23T01:35:06Z**. This is the source commit timestamp, not an asserted Android release date or installed-tool version.

**Reading path.** Read [sparse_format.h](https://android.googlesource.com/platform/system/core/+/68be0c2c0006a0740d0b1809abe4717308f90d15/libsparse/sparse_format.h): `sparse_header`, `chunk_header`, and the trailing payload comments. Then read [sparse_read.cpp](https://android.googlesource.com/platform/system/core/+/68be0c2c0006a0740d0b1809abe4717308f90d15/libsparse/sparse_read.cpp): `process_fill_chunk`, `process_skip_chunk` and `process_chunk`.

**Future question.** After hyaku, propose a paper-only worksheet for an already authorized sparse-image description. For each chunk, distinguish input offset and byte count, declared output block range, payload kind and checksum assumptions. Which assertions identify bytes actually present in the container, and which describe a reconstruction rule? Preserve unknown output contents rather than equating skipped ranges with a verified zero-filled disk.

**Limits and rights.** Header declarations are not full format validation, successful checksum verification or evidence of a particular flasher's behavior. Both linked files explicitly carry Apache-2.0 headers, with AOSP copyrights from 2010 and 2012 respectively; review applicable notices before later reuse. This is a per-file statement, not a blanket license claim for Android.

**Novelty.** Existing Android signing, boot-header and filesystem sources are related. The distinct gap is sparse transport representation versus reconstructed span. No libsparse/sparse-image family alias appeared in the reviewed inventories and earlier notes.
