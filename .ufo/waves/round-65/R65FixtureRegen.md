PASS — regenerated fixture.apk and truth.json byte-identically from the committed fixture tree.

Axes: artifact-byte reproducibility; interpreter-version provenance.

Evidence
- Committed baseline: HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (`git show HEAD:corpus/fixtures/apk-r65/{generator.py,fixture.apk,truth.json}`).
- Copied `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/` to `/tmp/R65FixtureRegen-wfxqs_sl/repro` (using `shutil.copytree`, without running the generator in place). For `generator.py`, `fixture.apk`, and `truth.json`, the working source matched HEAD and the scratch copy matched the source.
- Ran `python3 -B generator.py` in `/tmp/R65FixtureRegen-wfxqs_sl/repro`; exit 0. Output:
  ```
  fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
  member AndroidManifest.xml offset=0 size=416 crc32=962d075f
  member classes.dex offset=465 size=112 crc32=2635c82a
  member META-INF/MANIFEST.MF offset=618 size=69 crc32=e948d738
  ```
- `cmp -s` regenerated `fixture.apk` vs HEAD: exit 0 (identical). SHA-256: `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 bytes).
- `cmp -s` regenerated `truth.json` vs HEAD: exit 0 (identical). SHA-256: `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` (2466 bytes).
- Python versions: runtime `Python 3.14.8`; committed truth `build_recipe.python_version` `3.14.8`; regenerated truth `build_recipe.python_version` `3.14.8`. The targeted one-field-normalization comparison also returned exit 0; raw files already matched, so no version-only difference was needed.
- Committed-source SHA-256: `generator.py` `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a`; `fixture.apk` `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`; `truth.json` `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`.

Pointers: `corpus/fixtures/apk-r65/generator.py:194-226` writes the APK and records the running Python version; `corpus/fixtures/apk-r65/truth.json:49-67,69-72` records the recipe, interpreter version, and expected image hash/size.

Risks/blockers: none for this scoped regeneration check. No production files were modified; the generator ran only in `/tmp`.