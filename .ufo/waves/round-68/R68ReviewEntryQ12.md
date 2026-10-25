PASS (correctly n/a) — Q12 cannot apply to these bytes: the entry writes no rejected source row, and no rejected row is cited either, so no reject reason or `flip` is owed; the entry's n/a names that reason, which satisfies QUALITY.md admission step 1 and the C2 predicate's "n/a only with the entry's named reason".

seat: L1Revenger68.R68ReviewEntryQ12 · criterion: **Q12 only** · target bytes:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`
sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`, 33442 bytes (read-only; nothing edited).

## Criterion as frozen

`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md` Q12 row:
"A rejected source row states a reject reason grounded in a located quote, and its `flip` names a change to the source (a successor or revision) or a scope the reject reason does not exclude." Reject when: "the flip asks for content the row already credits the source with, so it can never change the verdict (S008, superseded by S024)" — lesson M21, `corpus/lessons/round-61.md:37`.
Admission procedure step 1 (`QUALITY.md`): "A criterion marked `n/a` names why it cannot apply."

The applicability test therefore has two branches, and I checked both:
- **written branch** — does the entry itself author a source row in rejected state?
- **cited branch** (the stricter reading the r64 precedent used, `corpus/knowledge/round-64-firmware-region-byte-evidence.md:220` "no rejected source row cited") — does the entry rest support on a rejected row?

## Evidence — commands and their actual stdout

### 1. The Q12 decision row itself (line 183, verbatim)

```
$ sed -n '183p' corpus/knowledge/round-68-apk-axml-byte-evidence.md
| Q12 | n/a | no rejected source row is written by this entry. |
```

The reason is named, not blank — QUALITY.md step 1 is met, and it is falsifiable in one command (below).

### 2. No rejected row exists in the entry bytes; no `flip` field exists at all

```
$ grep -c -i 'flip' corpus/knowledge/round-68-apk-axml-byte-evidence.md
0
$ grep -c -i 'reject' corpus/knowledge/round-68-apk-axml-byte-evidence.md
2
$ grep -n -i 'reject' corpus/knowledge/round-68-apk-axml-byte-evidence.md   # (truncated here)
9:admission-status: candidate — ... on a fail the row stays `uncovered` and this file is marked `rejected`.
183:| Q12 | n/a | no rejected source row is written by this entry. |
```

Both occurrences are accounted for and neither is a source row:
- **:9** is a *prospective* self-status for this entry on a C2 fail (claims.md §C2 kill rule), not a source row, and it carries no reject reason and no `flip` because nothing is being rejected yet.
- **:183** is the n/a statement under review.

There is no `flip:` token anywhere in the file (`grep -c -i flip` = 0), so a Q12 reject ("its `flip` names…") has no surface to fail on: the entry writes zero rejected rows and therefore owes zero flips.

**Verdict for the written branch: the n/a reason is factually true.**

### 3. The cited branch — every `S###` the entry names, with its registry status (parsed, not eyeballed)

```
$ python3 - <<'EOF'
for i,l in enumerate(open('corpus/SOURCES.md'),1):
    if l.startswith('| S0'):
        c=[x.strip() for x in l.rstrip().split('|')]
        ...
EOF
S032 line 46  status: mined
S034 line 48  status: mined
S038 line 52  status: mined
S039 line 53  status: mined
S041 line 55  status: mined
S043 line 57  status: queued
S045 line 59  status: mined
S046 line 61  status: mined
```

Every id the entry cites (`grep -o -E 'S0[0-9]{2}' … | sort | uniq -c` → S032×3, S034×4, S038×16, S039×1, S041×5, S043×5, S045×9, S046×1) is `mined` or `queued`. **Not one is `rejected`.**

The four rejected rows that exist in the registry are, and each has `used-by` `—` (i.e. no entry rests on it):

```
line 22 S008 status='rejected' used-by='—'
line 26 S012 status='rejected' used-by='—'
line 38 S024 status='rejected' used-by='—'
line 39 S025 status='rejected' used-by='—'
```

So even under the strict cited branch, Q12 is not triggered: this entry neither writes nor leans on any rejected row.

### 4. Lineage consistency (no regression, no new debt)

```
$ grep -n '| Q12 ' corpus/knowledge/round-65-apk-axml-byte-evidence.md
151:| Q12 | n/a | no rejected source row is written by this entry. |
$ grep -n '| Q12 ' corpus/knowledge/round-67-apk-axml-byte-evidence.md
155:| Q12 | n/a | no rejected source row is written by this entry. |
```

and the prior-round adjudication of this exact shape: `corpus/lessons/round-66.md:35` — `| Q12 | PASS (correctly n/a) | R65ReviewEntryQ12 | consistent — entry writes no rejected row |`. The r68 row is byte-identical in substance to the r65/r67 rows the prior wave already adjudicated, and the added round-68 material (§item 11, S046, `:244`→`:245`) introduces no rejected row.

### 5. The entry's own commands re-run by me (read-only) — the surrounding bytes are the bytes claimed

```
$ python3 -B corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
...
enum RES_XML_START_NAMESPACE_TYPE : 245
...
comment attributeStart : 686
field attributeStart : 687
derive exit=0
$ python3 -B corpus/fixtures/apk-r65/readout.py | wc -l
15
readout exit=0
$ sha256sum /tmp/q12-readout.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/q12-readout.out
```

Both match the entry's `recheck:` line (`507d79f8…`, 15 stdout lines; 17 derivation lines, exit 0), and neither command's output contains a rejected source row or a `flip` — so Q12's applicability is unchanged by live re-execution, and nothing in the re-derived surface creates a rejected row that the entry would owe a reason and flip for.

## Entry lines at issue

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:183` — `| Q12 | n/a | no rejected source row is written by this entry. |` — **correct as written**; the correct value under Q12 on these bytes is `n/a` with that reason (a `pass` would also be defensible but is not owed; an `n/a` that names why it cannot apply is what QUALITY.md step 1 asks for).
- `:9` — the only other `reject` token; prospective self-mark on a C2 fail, not a source row. No change required.
- `:2` — the one reject-shaped sentence in the entry, examined and dismissed (see residual risk).

No line states a wrong value for this criterion; there is no FAIL to name.

## The one edge I examined and dismissed (why it is not a Q12 trigger)

Line 2 (`source: S043 — supersedes S039 — … — the round-65 draft cited "line 5", which is `older server.``) is the closest thing in the file to a rejection record: it gives a located quote (`older server.`, snapshot line 5) as the ground for correcting an earlier *citation*. It is not a rejected **source row**:
- the row it corrects is **S043 itself** (`corpus/SOURCES.md:57`, status `queued`, not `rejected`) — the entry keeps S043 as support and narrows its scope to "route-scope sentences only";
- the thing rejected is the *round-65 draft's citation* (an entry), and entries are not source rows;
- it states no `flip`, so it asks for no content and cannot exhibit the M21 defect (a flip that asks for what the row already credits).

Under Q12 as frozen, correcting a citation inside an entry is not a source-row rejection and owes no flip. Nothing here flips a verdict.

## Residual risk

1. **Reading-dependent n/a.** Q12's text does not restate its own applicability rule; I applied both the written branch (the entry's stated reason) and the cited branch (the r64 precedent) and both are clean, so the verdict does not depend on which reading the adjudicator takes.
2. **Q12's known weak branch.** `corpus/lessons/round-61.md:117` and `corpus/lessons/round-62.md:22` both record "Q12 successor-flip weakness / Unresolved criterion debt, no Q12 rewrite". That debt concerns rows that *are* rejected; this entry writes none, so the weakness cannot reach these bytes — but it means a `PASS (correctly n/a)` here is not evidence that Q12 itself is sound.
3. **Future promotion.** If a later round turns line 2's correction into a rejected source row (e.g. retiring S043/S039 in favour of a successor), that row would then owe a located-quote reject reason and a flip naming a source change or a non-excluded scope, per Q12. On these bytes that obligation does not exist.

## Verification gaps (stated, not filled)

- I did not audit Q01–Q11 or Q13 on these bytes; they are other seats' criteria. My PASS is scoped to Q12's applicability and the truth of `:183`.
- I did not verify the README C05 row's `uncovered` state as a claim of C2's predicate beyond a read (`corpus/README.md:34` reads `uncovered`, knowledge column `—`); the flip is not mine to judge.
- `corpus/SOURCES.md` row statuses were read from the working tree, not from a committed-tree extraction; the statuses I relied on (`mined`/`queued` vs `rejected`) would only strengthen a Q12 trigger if they differed at the measured tip, and no row cited here is rejected in either tree state I observed.

## Tooling

No install or upgrade was made (no package manager, uv, cargo or npm invocation in this seat); the only binaries used were `grep`, `sed`, `sha256sum`, `wc` and `python3 -B`, all already present. Nothing was written outside this report file; no git/jj mutation, no peer message.
