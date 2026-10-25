Q12 n/a (the entry writes no rejected source row — confirmed against committed bytes)

Seat: R67ReviewEntryQ12 · scope: Q12 fresh-seat admission decision on the landed v2 candidate
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md` (committed bytes, non-author).

## Criterion under test

`corpus/QUALITY.md:24` — Q12: "A rejected source row states a reject reason grounded in a located
quote, and its `flip` names a change to the source (a successor or revision) or a scope the reject
reason does not exclude." Reject when the flip asks for content the row already credits the source
with. Q12 only has an object to test when the entry writes a source row whose status is `rejected`.

## Decision basis (strongest counterexample tested)

The strongest available counterexample: the entry's source header cites S043 as "supersedes S039"
(entry:2), and its admission-status prose says the round-65 candidate was "falsified" (entry:8) —
either could arguably constitute writing a reject. Both fail on committed bytes:

1. S043/S039/S038/S041/S045 are *cited* rows, not written rows. Their registry status fields in
   `corpus/SOURCES.md` are `mined` (S038 :52, S039 :53, S041 :55) or `queued` (S043 :57, S045 :59).
   The S043→S039 supersession is a queued registry row written in round 66, not a rejected row and
   not written by this entry. `grep -nE '\| (mined|queued|rejected) \|' corpus/SOURCES.md` →
   37 mined / 4 queued / 4 rejected; the 4 rejected rows are S008 (:22), S012 (:26), S024 (:38),
   S025 (:39) — each carries a located-quote `REJECTED:` reason plus a `flip:` naming a successor
   or in-scope change (e.g. S024's flip: "a successor RFC or BCP supersedes RFC 3227"), conforming
   to Q12 — and none is written or touched by this entry.
2. The "falsified round-65 candidate" (entry:8) is a knowledge entry
   (`corpus/knowledge/round-65-apk-axml-byte-evidence.md`), not a `corpus/SOURCES.md` row; its
   `admission-status` is governed by `reports/round-67/claims.md:64-66` (kill rule), outside Q12.
3. Entry:155 Q-map row: `| Q12 | n/a | no rejected source row is written by this entry. |` —
   the named reason is accurate: `grep -nE 'reject|flip|REJECT|verdict'` over the entry returns
   only line 8 (README-flip admission-order prose, not a source-row flip) and line 155.

Decision: n/a, matching the brief's expected outcome. No FAIL fact exists.

## Spot re-derivation (OFF-criterion sweep, all clean unless prefixed OFF-)

- `sha256sum`: fixture.apk `05d2280f…f03e`, truth.json `27303bae…8173`, readout.py
  `92e347c3…3976` — all match entry:4/5/16. Snapshot digests: dex-format.html
  `c0428612…d9f4`, rea-android-applications.md `412d9cb4…fa74c`, ResourceTypes.h
  `56b88bc4…c56f` — all match the registry anchors.
- `python3 -B corpus/fixtures/apk-r65/readout.py` (run from lane root): exit 0, 15 stdout lines,
  stdout sha256 `507d79f8…ad247` — matches recheck entry:6 and §Reproduce :166.
- S038 enum anchor: snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` lines 237-253
  span `enum {` through `RES_XML_RESOURCE_MAP_TYPE = 0x0180` at :253 — matches entry:1/:56.
- S043 anchor: `rea-android-applications.md:7-8` = "Start with `inspect_android_package` …" —
  matches entry:2; the rejected line-5 anchor claim is accurate (line 5 is not this sentence).
- S045 anchor quotes present in `dex-format.html`: "must be 0x70", `ENDIAN_CONSTANT = 0x12345678;`
  — matches entry:3/:106.
- attrExt provenance: ResourceTypes.h:634/647/660/675 carry "Appears header.headerSize bytes
  after a ResXMLTree_node" and :686 "Byte offset from the start of this structure where the
  attributes start" — supports the item-8 derivation sentence (entry:81).
- OFF- entry:45 — editorial ambiguity only: "`4d616e69666573742d` — ASCII `Manifest-`, the
  16-byte prefix of `Manifest-Version: 1.0`" — `Manifest-` is 9 bytes; the intended referent is
  the 16-byte `payload_first16_hex` `4d616e69666573742d56657273696f6e` (value itself verified
  correct against the readout). No admission-impact.

No installs performed; no files written outside this report path.
