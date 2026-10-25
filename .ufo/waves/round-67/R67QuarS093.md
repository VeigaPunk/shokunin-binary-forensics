ABSENT — all 3 quoted strings missing from the fetched PDF (HTTP 200, 731467 bytes, real document); near-misses identified for strings 1 and 2; string 3 has no near-miss anywhere in the document.

# Quarantine hand-check: register row S093 (revenger, round3, payload-absent)

- Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:163` (READ-ONLY; read only, never written)
- Cited source: https://seg.nju.edu.cn/uploadPublication/copyright/1221412498312.pdf

## Fetch receipt

```
$ curl -sL --max-redirs 15 -w 'HTTP %{http_code} bytes %{size_download} url %{url_effective}\n' -o source.bin 'https://seg.nju.edu.cn/uploadPublication/copyright/1221412498312.pdf'
HTTP 200 bytes 731467 url https://seg.nju.edu.cn/uploadPublication/copyright/1221412498312.pdf
$ sha256sum source.bin
16826e4f9c911f35c7eae3e9ab49c0697e38c1ba23580101018af48fbc53e4a1
$ file source.bin
PDF document, version 1.4, 10 page(s)
```

Saved bytes (≤2MB): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S093/source.bin`

Document identity: cover page of NJU SEG Technical Report No. NJU-SEG-2021-CJ-003, "物联网固件安全缺陷检测研究进展" (Research Progress on Security Defect Detection of IoT Firmware), 张弛/司徒凌云/王林章, Journal of Cyber Security Vol.6 No.3, May 2021.

## Search surfaces

1. `source.bin` — raw PDF bytes (731467 B).
2. `streams.bin` — all 205 `stream`/`endstream` blocks, 100 zlib-decompressed (FlateDecode), remainder raw (4597817 B).
3. `extracted.txt` — `pdftotext -raw` output (86824 B).

Each quoted string searched fixed-string, case-sensitive, in UTF-8, UTF-16-BE, UTF-16-LE, and lower-hex PDF-string form, plus `html.escape`/`html.unescape` variants, on all three surfaces.

## Per-string results

### String 1 — `Software Engineering Group / Department of Computer Science / Nanjing University / Technical Report No. NJU-SEG-2021-CJ-`

**ABSENT** on every surface, every encoding. The ` / `-joined single-line form does not exist; the real text has these as separate lines, and the report number is never truncated:

```
extracted.txt:2  Software Engineering Group
extracted.txt:3  Department of Computer Science
extracted.txt:4  Nanjing University
extracted.txt:5  Technical Report No. NJU-SEG-2021-CJ-003
```

Near-miss (probable distortion source): the four separate cover lines joined with ` / ` and `NJU-SEG-2021-CJ-003` truncated to `NJU-SEG-2021-CJ-`.

### String 2 — `中图分类号 TP311 DOI 号 10.19363/J.cnki.cn10-1380/tn.2021.05.09`

**ABSENT** on every surface, every encoding. The true sentence at extracted.txt:34 is:

`中图法分类号 TP311 DOI 号 10.19363/J.cnki.cn10-1380/tn.2021.05.09`

Near-miss (probable distortion source): quoted string drops the character `法` — `中图分类号` vs the real `中图法分类号`. `中图分类号` never occurs; `中图法分类号` occurs once (line 34).

### String 3 — `CLI header 结构速查`

**ABSENT** on every surface, every encoding. No near-miss: `CLI`, `速查`, and `结构速查` occur nowhere in the document (`结构` appears only in unrelated technical prose such as `局部调用结构匹配`, extracted.txt:1064). Nothing CLI-header-shaped exists in this Chinese-language academic survey.

## Row verdict

Register claim confirmed: all three quoted strings are absent from the cited source. **ABSENT** (fabrication-class confirmation). Strings 1 and 2 are distortions of real document lines (line-join + report-number truncation; dropped `法`); string 3 appears entirely foreign to this document.

## Artifacts

- `quarantine/S093/source.bin` — fetched PDF, sha256 `16826e4f9c911f35c7eae3e9ab49c0697e38c1ba23580101018af48fbc53e4a1`, 731467 B
- `quarantine/S093/extracted.txt` — pdftotext -raw rendering
- `quarantine/S093/streams.bin` — decompressed stream dump

## Tooling

No installs needed; used pre-installed `curl`, `pdftotext` (poppler), `qpdf` (checked only), `python3`+zlib. Pacman untouched per 2026-10-20 pause ruling.

## Bounds compliance

Wrote only this report path and `quarantine/S093/` scratch artifacts. `/home/vgpnk/Projects/shokuknow` accessed read-only (single grep of the register). No git/jj mutations, no other seats contacted.

Report: .ufo/waves/round-67/R67QuarS093.md
