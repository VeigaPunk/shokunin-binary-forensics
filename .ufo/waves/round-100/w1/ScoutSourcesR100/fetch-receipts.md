# ScoutSourcesR100 — fetch receipts (access date 2026-11-05)

All bodies fetched with `curl -sSL` on 2026-11-05 and saved in this directory (all < 2 MB).
sha256 = full sha256 of the saved body bytes (`sha256sum`).

| # | URL | HTTP | bytes | sha256 | saved copy |
|---|-----|------|-------|--------|------------|
| 1 | https://raw.githubusercontent.com/androguard/androguard/v4.1.4/README.md | 200 | 4329 | `3e04d4aa3227689b9b559f67a4cd76421311051c0dcc88866cd40ab932dc3351` | `ag-readme-v414.md` |
| 2 | https://raw.githubusercontent.com/androguard/androguard/master/README.md | 200 | 18404 | `727cbd9ba53e9d281920517f938b2ab7f6e3827460cf383e5c9c1283060fcee9` | `ag-readme-master.md` |
| 3 | https://androguard.readthedocs.io/en/latest/ | 200 | 14255 | `a0ec8c6284c13a1a86887be83f85049b41e9b7684670229c170e8d3265da508a` | `ag-rtd-index.html` |
| 4 | https://androguard.readthedocs.io/en/latest/tools/androaxml.html | 200 | 8751 | `6507e7607f8c6d9b149d6a2f76079508b44e1a701510a49939008d855cbc2efc` | `ag-rtd-androaxml.html` |
| 5 | https://androguard.readthedocs.io/en/latest/intro/axml.html | 200 | 23339 | `21a748331cc5b67697821fcf84878120b52c002378e43a223da7c563470f7a47` | `ag-rtd-intro-axml.html` |
| 6 | https://raw.githubusercontent.com/androguard/androguard/eef97351/docs/tools/androaxml.rst | 200 | 205 | `a091672b7cb4de483657affb7add0290845bd884cefd4308832d2a3e5717c707` | `ag-androaxml-rst-eef97351.rst` |
| 7 | https://github.com/iBotPeaches/Apktool/releases/tag/v3.0.3 | 200 | 178774 | `3356d86d4f9b37ceb9384eefa03466215fbc6c54e5d36b39979a0abe1a508c77` | `apktool-release-v303.html` |
| 8 | https://apktool.org/ | 200 | 17129 | `b27b1f8d7160cdc6ad632deac9168ae1a760d25e8c585a360a24071cee268370` | `apktool-org-index.html` |
| 9 | https://apktool.org/documentation | 200 | 331 | `42e19905d983fb262aa2bd80fd5595358bb57c659e209c3139cd6a9b31a320b6` | `apktool-org-documentation.html` (meta-refresh stub → `/wiki/the-basics/intro`) |
| 10 | https://apktool.org/blog/apktool-3.0.3 | 200 | 27611 | `77cec9d372ee31bc909a7b862ad60dbb0beed9eab86637e5b926b72c6f52e783` | `apktool-org-blog-303.html` |
| 11 | https://apktool.org/wiki/the-basics/intro | 200 | 23480 | `7e1c418b4572e4bc7738799677a52c848919ba4592c24046a79cce764727cf4f` | `apktool-wiki-intro.html` |
| 12 | https://raw.githubusercontent.com/iBotPeaches/apktool.org/main/wiki/the-basics/intro.mdx | 200 | 1626 | `f640bbffc53506ffcb4cad53e2f131b7acc5c8a0fc1b34411bbf409a43e6cad8` | `apktool-wiki-intro.mdx` |

Probes that returned 404 (no body kept):

- `https://raw.githubusercontent.com/androguard/androguard/v4.1.4/docs/source/tools/androaxml.rst` → 404
- `https://raw.githubusercontent.com/androguard/androguard/v4.1.4/docs/tools/androaxml.rst` → 404
- `https://raw.githubusercontent.com/androguard/androguard/v4.1.4/docs/source/intro/axml.rst` → 404
- `https://raw.githubusercontent.com/androguard/androguard/v4.1.4/androguard/docs/source/tools/androaxml.rst` → 404
- `https://apktool.org/wiki/the-basics/cli` → 404
- `https://apktool.org/docs/cli` → 404
- `https://apktool.org/docs/the-command-line-interface` → 404

Derivation commands (run 2026-11-05 from the wave dir):

```
$ sha256sum ag-readme-v414.md ag-rtd-androaxml.html ag-androaxml-rst-eef97351.rst apktool-release-v303.html apktool-wiki-intro.html apktool-wiki-intro.mdx
$ wc -c <same files>
```
