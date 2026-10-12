# Round 2 archive inventory — 20261012T164246Z

## Fixture and route
- Known truth: `.shokunin/revenger/corpus/fixtures/archive-r2/truth.json`; generated via Python `zipfile.ZipFile` with `ZIP_DEFLATED`, level 9, adding `bin/checksum` from r1 ELF and `README.txt` literal. Archive SHA-256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`. No target execution.
- `npx -y rea-agents@6.4.0 inspect-artifact /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/archive-r2/fixture.zip --format json` returned exit 0; full result `artifact-inspection.json`, stderr `artifact-inspection.stderr`. This is a provider-neutral archive inspection; it does not imply an opened native provider session. Top-level Evidence ID `ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d`, nested inventory Evidence ID `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b`.

## Ledger
| class | REA finding | Evidence ID | truth comparison |
|---|---|---|---|
| OBSERVATION | ZIP root SHA-256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, size 2964, format `zip` | `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | all three match `truth.json` / local hash and file size |
| OBSERVATION | Member `bin/checksum`: ELF SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`, size 16160, compressed size 2668 | `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | path, format, hash and sizes match source ELF and independent ZIP manifest |
| OBSERVATION | Member `README.txt`: file SHA-256 `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3`, size 84, compressed size 78 | `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | path, hash and sizes match independent ZIP manifest |
| OBSERVATION | Root has two `contains` edges and no unexplored branch within this inspection | `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | consistent with two central-directory entries; not a proof of no trailing bytes |
| INFERENCE | This fixture's expected root and two members are all found in REA's archive graph | `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | deterministic comparison of `nodes`+`occurrences` against `truth.json`: exact member map equality |
| UNKNOWN | Function-level behavior of embedded ELF and any bytes after ZIP central directory | no native behavior Evidence ID | REA limitation explicitly says inventory is central-directory-only; native analysis remains blocked from r1 |

## Score and limitations
- Define identity units: root digest+format+size (1 unit); each named member with hash+uncompressed/compressed size (2 units). All **3/3 observed units correct**, **0 false identity units**, precision 3/3 and recall 3/3 against this declared fixture inventory. Two `contains` edges match ZIP member count. Neither score measures code behavior.
- Independent check: `python3 -c "import json; from pathlib import Path; p=Path('.shokunin/revenger/corpus/live/runs/20261012T164246Z/artifact-inspection.json'); t=json.loads(Path('.shokunin/revenger/corpus/fixtures/archive-r2/truth.json').read_text()); i=json.loads(p.read_text())['normalized_result']['substeps'][0]['evidence']['normalized_result']; n={x['artifact_id']:x for x in i['nodes']}; a={x['logical_path']:(n[x['artifact_id']]['sha256'],n[x['artifact_id']]['size'],x['compressed_size']) for x in i['occurrences'] if x['logical_path']!='.'}; b={x['path']:(x['sha256'],x['size'],x['compressed_size']) for x in t['members']}; print(i['manifest']['root_sha256']==t['archive_sha256'],a==b)"` → `True True`.
- `coverage.status` is `complete-within-substeps`, one completed `inventory_artifact`, no omitted observations, but the tool's stated boundary is central-directory entries only. No extraction, decompilation, target execution, signing-block examination, or runtime claim.
