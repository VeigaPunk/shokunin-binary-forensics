# ExecFrozen — round 95 w1 report (attempt 1, calibration)

Seat: ExecFrozen (executor, leaf). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Scope: freeze-state verification facts for the vote binding; no lane file edited; no
git/jj write command run; every Python invocation `python3 -B`.

## Verdict

FREEZE-STATE VERIFIED — all checks pass. Nothing to escalate.

## Files written (all inside my wave dir)

- `.ufo/waves/round-95/w1/ExecFrozen/digest.txt` — 64 bytes, the digest only (no newline)
- `.ufo/waves/round-95/w1/ExecFrozen/freeze-state.md` — full command log, hash pairs, digest

## Results

1. Freeze commit `6e0bf15fed58f357b7fa0c881371ac7616a116f7` (type `commit`) carries all
   four frozen targets (`cat-file -e` OK on claims.md, c1_k_admit_counter4.py,
   forge_battery4.py, and the superseding entry) plus the full r93/r94 instrument trees
   and the round-95 receipts (`S500/S501` bodies + receipts + `fetch-log.md`).
2. Working tree == freeze commit for every tested path:
   - claims.md `7d9fafe192579c7fbbf344c2b1ceb490682394d772a37f1caca534a744d29264`
   - c1_k_admit_counter4.py `fbbec26cf1bcedea4117bff6d46be33d87dae426d76d1c44612efbcff039b6d9`
   - forge_battery4.py `8092523c47280c18dc001073e9bd61615560d72e510e3126cf1523a570769b73`
   - entry `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`
3. Frozen receipts match the claims sentences exactly: S500 body 17010 B
   sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`; S501 body
   18784 B sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`;
   receipts and fetch-log.md also working==freeze.
4. Vote-binding digest (exact recipe, lane root, `python3 -B`):
   `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`.
   Identity note for downstream seats: the entry's only `admission-status:` line
   (line 21) already reads `admission-status: candidate`, so the normalizer is an
   identity transform and digest == raw entry sha256 today; votes bind this value.

## Hygiene

- Scratch `/fast/scratch/hyaku/revenger-r95/ExecFrozen/` created, unused (output captured
  in-command), deleted before yield.
- Wrote nothing outside `.ufo/waves/round-95/w1/ExecFrozen/`; read-only git subcommands
  only; no installs performed; no network use; no spawns.
