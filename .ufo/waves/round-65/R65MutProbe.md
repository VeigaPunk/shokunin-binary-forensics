# R65MutProbe — readout.py self-consistency mutation probe (C1 / C05 surface)

**NOT-FALSIFIED (C1 entry's frozen recheck still passes at base) — but 3 of the 4 named self-consistency points are non-gating:** `crc32_matches` and `checksum_matches` are printed booleans, never assertions; `off == xml_size` **does not exist in the landed bytes**; and deleting the one exit-gating walk-end assertion (`assert cursor == eocd`, readout.py:119) admits a forged CD at **exit 0, 15 lines, all 12 printed booleans true**, differing from the honest run only in the `archive` fact's own file digest. Only `cursor == eocd` is load-bearing against overshoot, and it is a single point.

## Contract read

- `reports/round-65/claims.md` read in full before scoring. My probe is not a C1/C2 scorer: `grep -c readout reports/round-65/measure.py` → **0**, so no frozen label (`K_HELD`, `K_ROW C05`, `C5_*`, `HOLDS_OK_V3`) is touched by anything below. Kill rule/predicate untouched; no contract text changed.
- Target: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/readout.py` (11236 B, sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`); fixture `fixture.apk` (947 B, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`), `ZIP_STORED`, 3 members, CD 737..925, EOCD 925.
- Bounds: all copies under `/tmp/r65mutprobe/` (outside the fleet root). No git/jj command run. No repo file written except this report. No tool installed; host Python 3.14.8 used unmodified.

## Detectors (bounded, run on pristine / forged / restored bytes)

| id | predicate |
|---|---|
| `D_exit` | `python3 -B readout.py` exits 0 (the readout "accepts" the fixture) |
| `D_flag(f)` | exit 0 **and** the named printed boolean is `true` (`crc32_matches`, `checksum_matches`, `signature_matches`, `xml_total_size_equals_member`, `cd_end_equals_eocd_offset`) |
| `D_hash` | exit 0, 15 stdout lines, stdout sha256 == `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (the entry's frozen recheck, entry:5) |

Baseline calibration (pristine script × pristine apk): rc 0, 15 lines, stdout sha256 `507d79f8…dad247` = frozen value, all booleans true, walk end 416 == `xml_total_size` 416. Detector healthy → mutations are scorable.

## The four named points, as landed

| point | site | form | gates exit? |
|---|---|---|---|
| `off == xml_size` | absent — `grep -c 'off == xml_size'` → **0**; walk is `while off < xml_size:` readout.py:133, `off += csize` :141, no post-loop check | — | **no such check** |
| `cursor == eocd` | readout.py:119 `assert cursor == eocd, (cursor, eocd)` | assert | **yes** |
| crc match | readout.py:116 `crc32_matches=(crc_stated == f"{zlib.crc32(payload)&0xFFFFFFFF:08x}")` | printed boolean | **no** |
| checksum match | readout.py:242 `checksum_matches=(checksum == (zlib.adler32(dex[12:])&0xFFFFFFFF))` | printed boolean | **no** |

`grep -c 'assert '` → 6 asserts total (lines 90, 98, 104, 119, 129, 162) + one `raise` (:140); the five self-consistency *bits* (85, 116, 143, 242, 245) have no assert.

## Mutants (one behavior-bearing point weakened each)

| id | edit (readout.py) | old → new | pristine-input behaviour |
|---|---|---|---|
| M1 | :119 | `assert cursor == eocd, (cursor, eocd)` → `assert cursor <= eocd, (cursor, eocd)` | rc 0, frozen sha **unchanged** |
| M1b | :119 | assert deleted (line removed) | rc 0, frozen sha **unchanged** |
| M2 | :116 | `crc32_matches=(…)` → `crc32_matches=True` | rc 0, frozen sha **unchanged** |
| M3 | :143 | `xml_total_size_equals_member=len(axml) == xml_size` → `=True` | rc 0, frozen sha **unchanged** |
| M4 | :242 | `checksum_matches=(…)` → `checksum_matches=True` | rc 0, frozen sha **unchanged** |

**All four weakenings are invisible to `D_hash`/`D_exit` on the honest fixture** (`507d79f8…` in every case). The entry pins the script's digest in prose (entry:4, entry:162 "saved verbatim … sha256 `92e347c3…`") but no executed check compares it, so script-level weakening is caught only by a human digest comparison.

## Forged fixtures (byte edits from the pristine apk; `ZIP_STORED`, so payload edits do not move layout)

| id | edit | base-script result |
|---|---|---|
| F1 | last CD record `comment_len`@892 = 4 (record claims 4 bytes that are the EOCD) | rc **1**, `AssertionError: (929, 925)` → refused |
| F2 | `META-INF/MANIFEST.MF` payload byte 678 ^= 1, declared CRCs left stale | rc **0**, `crc32_matches=false` for that member only |
| F3 | AXML last chunk (rel 392) size 24 → 28: walk ends at **420** in a 416-byte document | rc **0**, all booleans true except AXML crc; **no fact reports the overrun** |
| F4 | `classes.dex` payload byte 526 ^= 1 (inside declared signature field 12..32) | rc **0**, `checksum_matches=false` **and** `signature_matches=false` |
| F5 | F2 **plus** declared CRC rewritten consistently (lh+14 = 632, cd+16 = 876) | rc **0**, **all** booleans true; only jar `sha256`/`payload_first16_hex` and `archive.sha256` differ |
| F6 | F3 **plus** AXML CRC rewritten consistently (14, 753) | rc **0**, **all 12 booleans true**, walk end 420 ≠ `xml_total_size` 416 |
| F7 | AXML root document size field@53 = 408, CRC rewritten | rc **0**, `xml_total_size_equals_member=false` (walk still ends 416) |
| F8 | EOCD `total_entries`@935 = 2 | rc **1**, `AssertionError: (859, 925)` → refused |

## Matrix and verdicts

| mutant × forgery | actual output | verdict |
|---|---|---|
| **M1b × F1** | rc **0**, **15 lines**, out sha `ccd25f43b1ca10ec…`; flags `cd_end=true`, all `crc=true`, `xml_size_eq_member=true`, `walk_end=416/416`, dex cksum+sig true. `diff` vs base = **one line**: `archive.sha256` `05d2280f…` → `9f958337…`. Every structural fact identical. | **SURVIVED** — `assert cursor == eocd` is the sole guard on directory-walk termination; remove it and a lying central directory passes at exit 0 with every printed consistency bit true. Killed by `D_exit` at base (base refused, rc 1) → the assertion **is load-bearing**, single-point. |
| M1 × F1 | rc **1**, `AssertionError: (929, 925)` | weakening `==`→`<=` does **not** open overshoot (929 > 925). Direction-specific. |
| M1 / M1b × F8 | both rc **1**, `KeyError: 'META-INF/MANIFEST.MF'` | undershoot is doubly guarded: member lookups (`members["…"]`) refuse it even with the assert weakened/removed. The assert's *unique* coverage is overshoot only. |
| **M2 × F2** | mutant rc **0**, `crc32_matches=true` for the tampered member (base: `false`) | survives `D_exit` (base also rc 0 → the crc check never refuses anything); killed only by `D_flag(crc32_matches)`. **Report-only check.** |
| M2 × F5 | output byte-identical to base × F5 (`b281002b44ee29…`) | equivalent mutant: with declared CRC rewritten, the check was never going to fire. |
| **M3 × F7** | mutant `xml_size_eq_member=true` (base: `false`) | killed by `D_flag(xml_total_size_equals_member)` — this bit owns exactly one forgery class: root size field ≠ member length. |
| **M3 × F3 / F6** | stdout **byte-identical** to base (`3bdd946a9088b9…` / `9535f2a1f2e730…`) | **equivalent mutant** on the walk-overrun forgery; the emitted bit is blind to a chunk whose size walks past the document end. |
| **M4 × F4** | mutant `checksum_matches=true`, `signature_matches=false` | survives `D_exit`; killed by `D_flag(checksum_matches)`, but F4 is still refused-looking via the signature bit → the checksum conjunct is not the unique detector. |

## Which checks are load-bearing

- **Load-bearing (exit-gating):** `readout.py:90` CD signature, `:98` local-header signature, `:104` local/CD name equality, **`:119` `cursor == eocd` (overshoot only)**, `:129` RES_XML root type, `:140` zero-size chunk `raise`, `:162` string length.
- **Report-only (never gate exit):** `:85` `cd_end_equals_eocd_offset` (computed from EOCD fields, so it stays `true` on F1 while the walk overshoots by 4), `:116` crc, `:143` root-size-vs-member, `:242` checksum, `:245` signature. Each can be replaced by a constant with **zero** observable change on the honest fixture.
- **Absent:** `off == xml_size`. F3/F6 prove the walk can terminate at 420 in a 416-byte document with no fact flagging it; the contradiction exists only in the printed `chunks` table, which a reader must re-add.
- **Redundant pairs:** checksum vs signature — no single-byte corruption yields `checksum_matches=false ∧ signature_matches=true` (adler32 covers `dex[12:]` ⊇ the signature field; any flip there also breaks the declared-vs-recomputed SHA-1). CRC-32 vs payload sha256 — same, sha256 changes on every payload edit.

## Forgeries that still escape at base (no mutation needed)

1. **Consistent-CRC tamper (F5):** rewrite the declaration alongside the payload → rc 0, every boolean true. CRC-32 here is *declared-vs-actual consistency*, not integrity; it cannot see a forger who edits both.
2. **AXML walk overrun (F3, F6):** the invariant the brief names is unenforced. F6 additionally carries every boolean as `true`.
3. **Lying root document size (F7):** refused only by a non-gating boolean.
4. In all cases the **only** surviving backstop is `archive.sha256` vs the pinned digest (`truth.json`/entry) — i.e. `D_hash`, which is equivalent to "hash the file" and attributes nothing to a specific invariant. Once the whole-file digest differs, the 14 other facts add no detection power.

## Calibration finding (routed, not a contract change)

The C1 recheck exercises the readout **only on the honest fixture**, where all five self-consistency bits are `true` by construction; it is invariant under every weakening above. This is the same gap shape the round's C2 closes for the receipt scripts (in-script forged-input control). Candidate future criterion, same shape as C5: one forged-fixture control per assertion family (F1/F2/F4/F6 bytes) requiring non-zero exit or a `false` verdict bit, plus making the five bits exit-gating and adding the missing `assert off == xml_size`. Per the frozen rule, this is a **coverage finding**; nothing in `claims.md`, the entry, or the verifier scripts was edited by this seat.

## Restoration evidence

Originals were never opened for write; all mutants/forgeries are copies under `/tmp/r65mutprobe/`.

```
before: 92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py
        05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk
after:  92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py
        05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk
        readout.py mtime 2026-10-24 02:39:41 (pre-wave, unchanged)
```

Scratch `/tmp/r65mutprobe/` is disposable and outside the lane; no restore was needed.
