PASS — S038/S039/S040 snapshot hashes match both recorded digests and re-fetched source bytes; no drift observed.

## Snapshot-to-record comparison

`corpus/SOURCES.md:52-54` and `corpus/lessons/round-65.md:12-14` record the following digests. Recomputed with `sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/*`; all match both records:

| Source | Snapshot | SHA-256 | Bytes |
|---|---|---|---:|
| S038 | `ResourceTypes.h` | `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` | 86255 |
| S039 | `rea-android-applications.md` | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` | 1992 |
| S040 | `zipfile-docs.html` | `e7fe6715126a3be8e6ea7ca4d3dc2d8713b6c979bde13f8fa9d6c458a3c49c6a` | 139782 |

The directory contained exactly these three snapshot files. `wc -c` confirmed the byte counts above; the S039 registry/gate records specify 34 lines.

## Re-fetch results

- **S038 / AOSP:** Fetched the pinned `ResourceTypes.h?format=TEXT` URL with curl, base64-decoded the response, then compared it with the snapshot. Output: `HTTP_STATUS=200 URL=https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h?format=TEXT REDIRECTS=0`; decoded SHA-256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`; `BYTE_COMPARE=identical`.
- **S039 / REA npm package:** Ran `npm pack rea-agents@6.5.0`, extracted `package/skills/reverse-engineer-anything/references/android-applications.md` from the tarball, and compared it with the snapshot. npm reported `npm http fetch GET 200 https://registry.npmjs.org/rea-agents` (twice) and `npm http fetch GET 200 https://registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz` (all `cache revalidated`); package version `6.5.0`, command exit 0. Extracted member SHA-256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`; `BYTE_COMPARE=identical`.
- **S040 / CPython docs:** Fetched `https://docs.python.org/3/library/zipfile.html` with curl. Output: `HTTP_STATUS=200 URL=https://docs.python.org/3/library/zipfile.html REDIRECTS=0`; fetched SHA-256 `e7fe6715126a3be8e6ea7ca4d3dc2d8713b6c979bde13f8fa9d6c458a3c49c6a`; `BYTE_COMPARE=identical`.

The first docs fetch attempt failed locally because its `/tmp` output directory had not yet been created (`curl: (23) client returned ERROR on write`); after creating the scratch directory, the fetch and byte comparison completed successfully. No repo files other than this report were written.