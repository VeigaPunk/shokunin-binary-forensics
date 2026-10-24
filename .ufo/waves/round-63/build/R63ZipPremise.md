# R63 C06 fixture premise re-verification

Scope: `corpus/fixtures/archive-r2/fixture.zip`, its `truth.json`, replay reconstruction, and the saved record/ledger at `corpus/live/runs/20261012T164246Z/`. No fixture, truth, record, or ledger bytes were repaired or edited. No tools were installed or updated.

## Archive root

Command:

```sh
sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/archive-r2/fixture.zip && stat -c 'size=%s' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/archive-r2/fixture.zip
```

Output:

```text
857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/archive-r2/fixture.zip
size=2964
```

## ZIP member bytes and truth comparison

Command (Python checker reads EOCD and central-directory records with `struct`, uses local-header offsets and central-directory compressed sizes to read member bytes, and hashes decompressed content):

```sh
python3 -B /tmp/revenger-r63-zip-premise.XkwXIk/check_zip.py /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/archive-r2/fixture.zip /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/archive-r2/truth.json
```

Output:

```text
archive_sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e expected=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e match=True
archive_size=2964 expected=2964 match=True
member=bin/checksum sha256=f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0 expected_sha256=f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0 size=16160 expected_size=16160 compressed_size=2668 expected_compressed_size=2668 match=True
member=README.txt sha256=7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3 expected_sha256=7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3 size=84 expected_size=84 compressed_size=78 expected_compressed_size=78 match=True
central_directory_entries=2 truth_member_count=2 match=True
```

## Replay reconstruction

Command (fresh output path was absent before invoking the replay script; `cmp` compares the reconstructed and committed ZIP bytes):

```sh
test ! -e /tmp/revenger-r63-zip-premise.XkwXIk/reconstructed.zip && printf 'output_initially_absent=yes\n' && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/replay_fixtures.py /tmp/revenger-r63-zip-premise.XkwXIk/reconstructed.zip && cmp --silent /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/archive-r2/fixture.zip /tmp/revenger-r63-zip-premise.XkwXIk/reconstructed.zip && printf 'replay_byte_compare=identical\n'
```

Output:

```text
output_initially_absent=yes
sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e size=2964 expected_sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e
replay_byte_compare=identical
```

## Saved record and ledger

Command (loads the record and truth as JSON, extracts the saved inventory manifest root hash, and compares the ledger's root row hash and size):

```sh
python3 -B -c 'import json,re; from pathlib import Path; base=Path("/home/vgpnk/Projects/shokunin/revenger-shokunin"); truth=json.loads((base/"corpus/fixtures/archive-r2/truth.json").read_text()); record=json.loads((base/"corpus/live/runs/20261012T164246Z/artifact-inspection.json").read_text()); inventory=record["normalized_result"]["substeps"][0]["evidence"]["normalized_result"]; saved=inventory["manifest"]["root_sha256"]; ledger=(base/"corpus/live/runs/20261012T164246Z/LEDGER.md").read_text(); row=next(line for line in ledger.splitlines() if line.startswith("| OBSERVATION | ZIP root")); match=re.search(r"root SHA-256 `([0-9a-f]{64})`, size ([0-9]+)",row); ledger_sha,ledger_size=match.group(1),int(match.group(2)); assert saved==truth["archive_sha256"]; assert ledger_sha==truth["archive_sha256"] and ledger_size==truth["archive_size"]; print(f"artifact_json=valid saved_root_sha256={saved} matches_truth=True"); print(f"ledger_root_sha256={ledger_sha} ledger_size={ledger_size} matches_truth=True")'
```

Output:

```text
artifact_json=valid saved_root_sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e matches_truth=True
ledger_root_sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e ledger_size=2964 matches_truth=True
```

The ledger also parsed to CommonMark XML:

```sh
cmark --to xml /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/20261012T164246Z/LEDGER.md >/dev/null && printf 'cmark_xml_parse=valid\n'
```

```text
cmark_xml_parse=valid
```

## Result

No drift found: archive SHA-256/size, both member SHA-256/uncompressed-size/compressed-size tuples, byte-exact replay, saved inventory root SHA-256, and ledger root SHA-256/size all agree with `truth.json`. No repairs were made. Boundary: this is evidence for the authored fixture and cited saved record only, not a general ZIP parser claim.
