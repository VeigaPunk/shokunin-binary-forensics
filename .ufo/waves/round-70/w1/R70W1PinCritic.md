HONEST-SCOPED for r68 as landed — but the pin rule is GAMEABLE in general (proved below: one JSON row silences a real one-character transcription typo with entry bytes untouched); the r68 instance is honest only because the entry's own text names the pinned digest.

Seat: R70W1PinCritic (advisory, wave 1). Target commit `aa1842fac199aa524930e5565ed3715de5f84c6d`; base
`3f5edbc206351232a3d2d801334dd930499ccaf5`. Counter `reports/round-70/measure.py` sha256
`488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76` (re-derived, matches claims.md).
No lane file was edited; all mutation work ran on `git archive aa1842f` under
`/tmp/revenger-r70-R70W1PinCritic` (deleted before return). No tool installed or upgraded (pacman paused; none needed).

## 0. Corrected premise (matters for wave-2 seats)

The assignment asked me to confirm that `git show 3f5edbc:corpus/derive_axml_anchors.py | sha256sum` equals the pin.
It does **not**, and must not:

```
$ git -C …/revenger-shokunin show 3f5edbc…:corpus/derive_axml_anchors.py | sha256sum
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa      # = S047 row (r69 extension, 20 lines)
$ git -C …/revenger-shokunin show 4232235:corpus/derive_axml_anchors.py | sha256sum
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249      # = S046 row, = pin, = r68 revision
```

claims.md §C3 does **not** assert base==pin; it asserts `derive_axml_anchors_r68.py` sha256 `bce497d6…` = the S046
row's digest. That assertion holds. The equality a wave-2 seat should re-check is the four-way one below, not
base==pin — asserting base==pin would itself be a false claim, since round 69 extended the script in place (that
extension *is* the drift under test).

## 1. Digest chain — all four links verified

```
$ git show 3f5edbc…:corpus/SOURCES.md | grep -o 'bce497d6[0-9a-f]*' | head -1
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249            # SOURCES.md:60 (S046 row)
$ sha256sum corpus/embedded_output_pins.json  →  "sha256": "bce497d6…249"   # corpus/embedded_output_pins.json:5
$ sha256sum corpus/derive_axml_anchors_r68.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249
$ git show aa1842f…:corpus/derive_axml_anchors_r68.py | sha256sum
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249            # copy at candidate
$ grep -n 'S046_SCRIPT_SHA' reports/round-70/measure.py
35:S046_SCRIPT_SHA = "bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249"
```

SOURCES.md:60 (S046) and SOURCES.md:61 (S047) are both intact and mutually consistent at the candidate commit
(S046 = 17 lines / `bce497d6…`; S047 = 20 lines / `74d4c0d9…`). The pin row and the r68 copy were added by the
pre-registration commit `dbacce2`, not by the candidate `aa1842f` (`git log --diff-filter=A -- corpus/embedded_output_pins.json`
→ `dbacce2` only), so C3's machinery is outside the C05 candidate's diff — separability is clean on this point.

## 2. Gate runs at `aa1842f` (cwd = archive root)

```
r65: checked_blocks=15 problems=1 exit=1
r67: checked_blocks=16 problems=0 exit=0
r68: checked_blocks=17 problems=0 exit=0
r69: checked_blocks=17 problems=0 exit=0
--self-test: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest  (exit 0)
```

Frozen counter on the same tree (grep of the labels):

```
K_HELD_BACKED=8/14  K_HELD_BACKED_STRICT=8/14  C05_STATUS=uncovered  C1_GATE=checked_blocks=22 problems=0 exit=0 ok=yes
EMB_R65=checked_blocks=15 problems=1 exit=1
EMB_R67=checked_blocks=16 problems=0 exit=0
EMB_R68=checked_blocks=17 problems=0 exit=0
EMB_R69=checked_blocks=17 problems=0 exit=0
EMB_PINNED_SCRIPT_IS_S046=yes  EMB_R68_BYTES_UNCHANGED=yes  EMB_R65_BYTES_UNCHANGED=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1  HOLDS_C3_V1=yes  GATE_SELFTEST=exit 0  HOLDS_OK_V7=yes
```

Every C3 mechanical conjunct reproduces exactly as claims.md states (`EMB_R68` before = 7, after = 0; r65 keeps
problems=1; r67/r69 clean; both entry sha256s unchanged base→candidate: `ef7f0232…` and `cf42cc20…`).
`EMB_R68 problems=7` reproduces precisely when the pin file is removed (control A of the claim, independently
re-run here): the seven problems are `entry:137`–`entry:143`.

## 3. What the pin is actually hiding: format, not numbers

```
$ python3 -B corpus/derive_axml_anchors_r68.py   # 17 lines
$ python3 -B corpus/derive_axml_anchors.py       # 20 lines
$ diff r68.out cur.out
9,15c9,18
< enum RES_STRING_POOL_TYPE : 239
< enum RES_XML_TYPE : 241
< enum RES_XML_START_NAMESPACE_TYPE : 245
…
> enum block open : 237
> enum RES_STRING_POOL_TYPE : 239 = 0x0001
> enum RES_XML_TYPE : 241 = 0x0003
> enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
> enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
…
> enum block close : 263
```

All seven cited line numbers (239, 241, 245, 246, 247, 248, 253) are **identical** under both revisions; r69
appended `= 0xNNNN` and added three lines. `drift()` (check_embedded_outputs.py:113-115) is exact-line membership,
so the reformatting alone produced the 7 problems. **No numeric drift is being hidden in this instance** — that is
the load-bearing fact behind HONEST-SCOPED.

But the mechanism has no notion of "number vs format": it freezes whatever the pinned revision printed. Had r69
changed a line number, the pinned r68 output would have validated the stale number and `problems=0` would have
been equally green. Nothing in the gate distinguishes the two cases.

## 4. Finding F1 (advisory, low): the entry's *live* recheck prose no longer reproduces its own block

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:7` — `recheck: \`python3 -B corpus/derive_axml_anchors.py\` from the lane root …`
- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:194` — "Anchor derivation: `python3 -B corpus/derive_axml_anchors.py` — exit 0, **17 lines**, one per cited symbol"
- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:128` — the fenced block header is `$ python3 -B corpus/derive_axml_anchors.py` (the unpinned spelling)

Running the command the entry displays prints **20** lines with 7 of them textually different from the block at
`:137-143` (diff in §3). The gate stays green only because `apply_pin` (check_embedded_outputs.py:98-110) silently
rewrites `argv[idx]` to `corpus/derive_axml_anchors_r68.py`. So `EMB_R68 problems=0` is **not reproducible by a
reader who copies the entry's own command**, and the entry's stated line count is stale against the live script.

Repair tension worth recording: the honest repair (name the pinned revision and its digest in `:7`/`:194`) would
change the entry bytes, which the frozen predicate forbids (`EMB_R68_BYTES_UNCHANGED`, `R68_SHA` at measure.py:33).
C3 as frozen **forecloses** its own best prose repair. Recommendation: do not edit the entry this round; record the
staleness as a scoped limitation in `corpus/lessons/round-70.md` (the same way S047 records that it supersedes S046),
and let a future round's entry-identity rule fix `recheck:` to name the digest.

## 5. Finding F2 (the real attack): the rule is GAMEABLE — proved

The pin's digest is checked only against the JSON row that the same commit authored. The gate never asks whether
the **entry** names that digest, so a pin can contradict the entry's own declared identity and still report green.

Proof (scratch copy, entry bytes untouched, gate bytes untouched):

```
# r65 entry:41 carries a genuine M39-class typo: hex 4d616e696673742d56657273696f6e = b'Manifst-Version'
# (the real readout prints 4d616e69666573742d56657273696f6e = 'Manifest-Version')
# added ONE pin row: {"round-65-apk-axml-byte-evidence.md": {"corpus/fixtures/apk-r65/readout.py":
#                    {"use":"corpus/pinned_r65.py","sha256":"b8995911ca943b927a1dc87b4f34c4804d2a43ba076a75099cfb16cb02dbaec8"}}}
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md
checked_blocks=15 problems=0        exit=0        # was problems=1
```

The entry names `readout.py` sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`
(round-65 entry:3), which the pin contradicts — and the gate does not notice. The same one-row move would silence
any retained entry's transcription drift. This round it is bounded only by three claim-specific conjuncts
(`EMB_R65 problems=1`, `EMB_R68_BYTES_UNCHANGED`, `EMB_PINNED_SCRIPT_IS_S046`) — guards in the counter, not
invariants in the gate. The gate's own self-test (check_embedded_outputs.py:186-194) tests a tampered **copy**
(digest mismatch), never a **mis-keyed pin**.

Smallest safe correction (prototyped on a scratch copy, ~4 lines in `apply_pin`): require the pin's sha256 to appear
verbatim in the entry's own text, else return an attributed problem:

```
entry_text = Path(cwd, entry_rel).read_text(encoding="utf-8") if entry_rel else ""
if pin["sha256"] not in entry_text:
    return cmd, f"{PIN_MARKER}: pin digest not named by the entry: {pin['sha256']}"
```

Measured effect of the prototype:

```
r68 (digest IS named at entry:4, S046 row):  checked_blocks=17 problems=0  exit=0    # unchanged, stays green
r65 + typo-silencing pin (digest NOT named): checked_blocks=0 problems=15 exit=1    # "pinned historical script
                                              digest mismatch: pin digest not named by the entry: b8995911…"
```

It preserves C3's pass, kills the F2 move, needs no new predicate conjunct, and stays inside the existing
`PIN_MARKER` attribution contract. Note it is a wave-2/next-round change: the gate is frozen this wave.

## 6. What a reader may and may not conclude from `EMB_R68 problems=0`

MAY conclude: the 17 lines at `corpus/knowledge/round-68-apk-axml-byte-evidence.md:129-145` are exactly the stdout
of `corpus/derive_axml_anchors.py` **at sha256 `bce497d6…`** over `corpus/snapshots/ResourceTypes.h` at sha256
`56b88bc4…`; that revision is the one the entry itself declares (entry:4, S046), so the block is re-derivable
against the script that actually printed it; and the seven cited line numbers are still the ones the current
script finds.

MAY NOT conclude: that the current `corpus/derive_axml_anchors.py` prints the block verbatim (it prints 20 lines,
7 reformatted); that the numbers were re-verified against any later script or snapshot revision; that the entry's
displayed command reproduces the block (the gate substitutes a different file); or that a green `EMB_R68` implies
any *other* entry was validated against a historical revision (only r68 has a pin row).

## 7. Impacted axes

- freshness (C3): the conjuncts hold and the hidden drift is format-only — C3 is not falsified; but its gate has a
  provenance hole (F2) and its own prose repair is foreclosed by its bytes-unchanged conjunct (F1).
- identity/provenance: `EMB_R68 problems=0` describes a command the entry does not display; the gate's report is
  one substitution away from the entry's text.
- coverage (C1): indirectly — C3 is the freshness guard protecting retained candidates; a gameable freshness gate
  weakens the retention argument the v5 candidate leans on, though not the candidate's own bytes.
- Not impacted: C2, HOLD_REPLAY, gate self-test (all green and independently re-run).

## 8. Verdict

**HONEST-SCOPED** for the r68 instance: the pin re-derives against exactly the revision the entry names, and the
seven problems it removes are formatting changes with every line number unchanged. **GAMEABLE** as a rule: a single
JSON row can silence a genuine transcription typo (proved on r65), and the only things stopping that this round are
frozen counter conjuncts rather than any structural guard. Fix F2 in the gate (prototype above) before the pin rule
is used on a second entry; record F1 as scoped staleness rather than editing the frozen r68 bytes.
