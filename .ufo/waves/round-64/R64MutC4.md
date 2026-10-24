# R64MutC4 report — independent C4 mutant confirmation (base survives, patched kills attributively)

Seat: mutation-tester, independent of the C2 author. No lane script, fixture, live byte,
registry, MANIFEST, jj or Git state was touched; all mutation work happened in
`/tmp/revenger-r64-mutc4/`. No tool was installed.

## Result

| tree | script | variant | exit | last line | verdict |
|---|---|---|---|---|---|
| base `666ea84b` | verify_icon_languages.py | control | 0 | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` | baseline green |
| base `666ea84b` | verify_icon_languages.py | c4 mutant | **0** | same PASS | **survived (red-before confirmed)** |
| base `666ea84b` | verify_multi_icon_states.py | control | 0 | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` | baseline green |
| base `666ea84b` | verify_multi_icon_states.py | c4 mutant | **0** | same PASS | **survived (red-before confirmed)** |
| patched working tree | verify_icon_languages.py | control | 0 | same PASS as base | patched base green |
| patched working tree | verify_icon_languages.py | c4 mutant | **1** | `AssertionError: r47: forged receipt stdout accepted` | **killed, attributed** |
| patched working tree | verify_multi_icon_states.py | control | 0 | same PASS as base | patched base green |
| patched working tree | verify_multi_icon_states.py | c4 mutant | **1** | `AssertionError: r42: forged receipt stdout accepted` | **killed, attributed** |

Verdict: C4 red-before 0/2 and patched attributed kill **2/2** both reproduce independently.
Both attributed last lines end with the frozen token `forged receipt stdout accepted`
(byte-exact, measured with `str.endswith` in the probe).

## Commands (exact, all absolute)

Scratch construction:

```
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus \
  | tar -x -C /tmp/revenger-r64-mutc4/base
cp -a /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus /tmp/revenger-r64-mutc4/patched/corpus
cp /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_languages.py \
   /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_multi_icon_states.py \
   /tmp/revenger-r64-mutc4/patched/corpus/
```

Probe: `python3 -B /tmp/revenger-r64-mutc4/probe.py` — per (tree, script, variant) it
`copytree`s the tree's `corpus` into `/tmp/revenger-r64-mutc4/out/<tree>-<script>-<variant>/`,
applies the mutant there, then runs

```
python3 -B <work>/corpus/<script> --self-test      # cwd=<work>
```

The mutant is the frozen one, copied verbatim from `reports/round-64/measure.py:212-224`
(`C4_CLAUSE = receipt\['stdout_sha256'\]\s*==\s*H\(raw_bytes\)`, deleted together with its
connecting `and`, exactly one match required or `could-not-evaluate`). Both trees had
match count 1; no `could-not-evaluate` fired.

## Diffs (identical single-line change in all four probes)

```diff
--- a/corpus/verify_icon_languages.py      (base 0f781c6a…, patched 2e9e56e8…)
+++ b/corpus/verify_icon_languages.py
@@ -117,7 +117,7 @@
 def receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes):
     return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
-            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))
+            receipt['evidence_id']==evidence_id)
```

```diff
--- a/corpus/verify_multi_icon_states.py    (base 0179e93f…, patched 9345cb8c…)
+++ b/corpus/verify_multi_icon_states.py
@@ -120,7 +120,7 @@
 def receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes):
     return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
-            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))
+            receipt['evidence_id']==evidence_id)
```

Saved as `out/{base,patched}-{verify_icon_languages,verify_multi_icon_states}-c4.diff`.

## Attribution integrity

- The mutant removes only the stdout conjunct, so with it `receipt_ok(forged_stdout)` returns
  exactly `receipt_ok(receipt) == True` (the forged copy is a `deepcopy` differing solely in
  `stdout_sha256`); `not True` fails the new control's `require`.
- Traceback confirms the failing frame is the new control, not an earlier assertion:
  `verify_icon_languages.py` line 152 / `verify_multi_icon_states.py` line 151, message
  `r{r}: forged receipt stdout accepted`. Occurrence count of that message in each mutated
  file is 1, so the endswith token cannot be produced by a different check.
- Base tree contains no `forged_stdout` symbol at all (`grep` shows only the `receipt_ok`
  clause at `:120`/`:123`), which is why the same mutant survives there — the survival is
  absence of the control, not a different predicate.
- The kill fires on the first round evaluated (r47 / r42) because both dicts iterate
  insertion-ordered; `receipt_ok` is shared by all rounds, so one firing suffices for clause
  coverage. Coverage finding (not a contract change): only the first round's new control is
  reached under this mutant; no per-round independence is demonstrated by the kill itself.

## Before/after hashes and restoration evidence

| file | pristine sha256 | unchanged after probe |
|---|---|---|
| base verify_icon_languages.py | `0f781c6a216bfdaa9cc1ab9b9fe8ae3ab9cb8a79d00ed56c4f94282c80a8efbd` | yes (src_before == src_after) |
| base verify_multi_icon_states.py | `0179e93f8bec17d5f4b60047f167ad26aa803a84440e98329fd8a8f2ea7a176d` | yes |
| patched verify_icon_languages.py | `2e9e56e8bd8d55ba56c91c87454c0768a66ac87cbe4ee02943cf1916a26d7d15` | yes |
| patched verify_multi_icon_states.py | `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e` | yes |

Mutated copies hashed: base icon_languages `0c8a099a…b129974`, base multi_icon
`b5375e35…f84f0fc52e`, patched icon_languages `6195a114…085126e10`, patched multi_icon
`069c24f5…8b80a28b`. Every mutated copy was then restored by `cp` from its pristine source;
copy hash == pristine hash and a re-run of `--self-test` exits 0 with the PASS line for all
four (`out/restored-*.out`). Lane working-tree files re-hashed after the probe:
`2e9e56e8…` / `9345cb8c…` — identical, untouched.

## Axes (godspeed)

1. **Detection fidelity** — base survives / patched kills, both scripts, 4/4 as contracted.
2. **Attribution integrity** — kill is produced by the named control line, endswith token exact.
3. **Restoration integrity** — pristine and restored hashes match; lane bytes provably unchanged.
4. **Independence** — base tree from `git archive 666ea84b`, patched copies from the live
   working tree, mutant applied only in scratch; reproduces `measure-before.log`'s
   `c4 exit=0` lines and predicts `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`.

## Findings routed (not acted on)

- Sibling `R64CriticC4` was notified of the mutant coordinates (clause regex, control lines)
  so its independent attribution attack targets distinct surface; no overlap claimed.
- Scratch `/tmp/revenger-r64-mutc4/` holds only evidence (`records.json`, diffs, stdout,
  restored logs); heavy scratch is L1's to remove on landing.
- No `pacman` transaction, no install, no git/jj mutation was performed (read-only
  `git archive`, `git status`, `git rev-parse`, `git diff` only).

Report: `.ufo/waves/round-64/R64MutC4.md`
