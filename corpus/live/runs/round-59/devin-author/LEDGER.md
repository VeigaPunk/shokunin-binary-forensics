# Round 59 (devin-author leg) — named type key at type level: coverage extension

Host: devin. Prior rounds executed on prime-agent; this leg's producer run and
byte-oracle were executed on the devin host.

- BEFORE: all authored PE fixtures used numeric type keys (id 3/14/10). The
  `kind:"name"` branch of the resource TYPE key was never scored; every prior
  root directory had `named_entries=0`. Separately, the calibration axis is
  halted (r59 malformed-name refusal prediction falsified); this leg is a
  distinct route on the coverage axis, not a re-tread of that claim.
- CLAIM: a PE32+ fixture whose root directory carries one named type entry
  `REVTEST` plus id entries 3 and 14 is statically enumerated byte-exact —
  4/4 leaves including the named-type leaf, icon-group ordered links intact,
  no false link onto the opaque named-type leaf.
- FIXTURE: `corpus/fixtures/pe-r59d/fixture.exe`, SHA-256
  `99bebcf14c462075e63d6504c97a45267063f33e05f215c1235f89d666b5c0f3`, 1536
  bytes. Built by `corpus/fixtures/pe-r59d/build_fixture.py` from r55 header
  bytes [0:512]; resource data-directory size field at offset 220 set to 320;
  icon/group payload bytes byte-identical to r55. `truth.json` in same dir.
  No PE execution.
- OBSERVATION [REA Evidence
  `ev_8efa2368e77f5370b305faea34e37042cb405f7c3583ed6b6c6ea7ba2dab6038`]:
  `npx -y rea-agents@6.4.0 inspect-pe-resources <abspath> --format json`
  exit 0, empty stderr. Saved `inspection.raw.json` SHA-256
  `e04b14ef31ffb66e3534cbc6b008544076972a236249c86982b53c0720cc936e`,
  `receipt.json` here. normalized_result: format pe32-plus, machine 34404,
  directory rva 8192 @512 bytes 320, coverage complete
  (examined_entries 11, resources 4).
- RESOURCE INVENTORY (byte-derived, confirmed by `verify.py` exit 0):
  - index 0: type `{"kind":"name","name":"REVTEST","utf16le_hex":"5200450056005400450053005400","location":{offset 812, bytes 16}}`, name id 1, lang 1033, data entry @784, payload rva 8648 @968 bytes 23, sha `d069b3846e5c7185f65263b6ca4e7a81670214b038f38805ed355f6c55191da6`.
  - index 1: type id 3, name id 1, lang 1033, data entry @736, payload rva 8512 @832 bytes 48, sha `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` (= r55 icon1).
  - index 2: type id 3, name id 2, lang 1033, data entry @752, payload rva 8560 @880 bytes 48, sha `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae` (= r55 icon2).
  - index 3: type id 14, name `A😀B!` utf16le `41003dd800de42002100` @800 bytes 12, lang 1033, data entry @768, payload rva 8608 @928 bytes 34, sha `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a` (= r55 group).
  - icon_groups[0]: resource_index 3, images [id1 → candidates [1], same-language 1, size true] and [id2 → candidates [2], same-language 2, size true]. The named-type leaf is never a candidate.
- BYTE-ORACLE: `python3 .shokunin/revenger/corpus/live/runs/round-59/devin-author/verify.py`
  → `PASS: 22 positive checks; 3/3 forged claims rejected`. The script
  re-derives directories, all entry_locations, data entries, name strings,
  payload ranges/digests and icon-group relations from fixture bytes only,
  then compares the full normalized_result; rejects forged candidate index 0,
  forged numeric type id 24, and a forged payload digest. Author-run, not an
  independent review.
- INFERENCE: on this authored fixture the static route resolves a named TYPE
  key (UTF-16 string with length prefix, `kind:"name"`) at the root level,
  orders it first in traversal, and keeps numeric-type branches and icon-group
  linking intact. Leaf precision/recall 4/4; group-image records 2/2; ordered
  candidate links 2/2; zero false links. This is a coverage extension of the
  scored shape space (named key at type level; root named_entries=1).
- Per-axis verdict claim: coverage **improved** (new key-kind at type level,
  first named root entry scored); depth **unchanged** (same three-level tree,
  same group relation semantics); calibration **unchanged** (byte-oracle
  discipline preserved; no refusal/negative-validity claim — that axis stays
  halted per r59 LOG). No axis regressed.
- UNKNOWN: whether the route accepts named keys at name level combined with
  arbitrary type ids, malformed/overlong names, duplicate names, Windows
  loader behavior, image decode/rendering, producer authentication, native
  disassembler readiness, arbitrary PE correctness. No push, no merge, no
  verdict marking.
