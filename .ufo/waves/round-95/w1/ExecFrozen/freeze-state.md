# ExecFrozen — round 95 freeze-state record (attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (all commands run from the lane
root). Freeze commit: `6e0bf15fed58f357b7fa0c881371ac7616a116f7` (type: `commit`).
All commands read-only (`git cat-file -e`, `git cat-file -t`, `git ls-tree`, `git show`,
`sha256sum`, `stat`, one `python3 -B` digest computation). No lane file edited; no
git/jj write command run. Scratch `/fast/scratch/hyaku/revenger-r95/ExecFrozen/` was
created with `mkdir -p`, used for nothing (all output captured in-command), and deleted
before yield. Every Python invocation used `python3 -B` (r94 lesson M5).

## 1. Freeze-commit object existence

Command (per path):

```
git cat-file -e 6e0bf15fed58f357b7fa0c881371ac7616a116f7:<path> && echo OK
git cat-file -t 6e0bf15fed58f357b7fa0c881371ac7616a116f7
```

Results: `commit`; all four targets OK —

- `reports/round-95/claims.md` OK
- `reports/round-95/c1_k_admit_counter4.py` OK
- `reports/round-95/forge_battery4.py` OK
- `corpus/knowledge/round-95-evidence-ledger-discipline.md` OK

Frozen instrument paths present at the freeze commit via
`git ls-tree -r --name-only 6e0bf15… -- reports/round-95/quote-receipts/ reports/round-93/ reports/round-94/`:

- `reports/round-95/quote-receipts/`: `S500.receipt.json`, `S501.receipt.json`,
  `raw/S500.body`, `raw/S501.body`, `fetch-log.md`
- `reports/round-93/*`: `c1_k_admit_counter2.py`, `forge_battery.py`, `claims.md`,
  `controls/*` (7 logs), `quote-receipts/*` (S496/S497), `votes/*` (3)
- `reports/round-94/*`: `c1_k_admit_counter3.py`, `forge_battery3.py`, `claims.md`,
  `controls/*` (10 logs), `quote-receipts/*` (S498/S499), `votes/*` (3)

## 2. Working tree vs freeze commit — hash pairs

Command pattern:

```
sha256sum <path>
git show 6e0bf15fed58f357b7fa0c881371ac7616a116f7:<path> | sha256sum
```

| path | working tree | freeze commit | equal |
|---|---|---|---|
| `reports/round-95/claims.md` | `7d9fafe192579c7fbbf344c2b1ceb490682394d772a37f1caca534a744d29264` | `7d9fafe192579c7fbbf344c2b1ceb490682394d772a37f1caca534a744d29264` | YES |
| `reports/round-95/c1_k_admit_counter4.py` | `fbbec26cf1bcedea4117bff6d46be33d87dae426d76d1c44612efbcff039b6d9` | `fbbec26cf1bcedea4117bff6d46be33d87dae426d76d1c44612efbcff039b6d9` | YES |
| `reports/round-95/forge_battery4.py` | `8092523c47280c18dc001073e9bd61615560d72e510e3126cf1523a570769b73` | `8092523c47280c18dc001073e9bd61615560d72e510e3126cf1523a570769b73` | YES |
| `corpus/knowledge/round-95-evidence-ledger-discipline.md` | `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` | `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` | YES |

The working-tree entry bytes equal the freeze commit's bytes (recipe precondition holds).

## 3. Frozen receipts — working tree vs freeze commit, and against the claims sentences

Same command pattern over `reports/round-95/quote-receipts/`:

| path | size | working tree = freeze commit sha256 | equal |
|---|---|---|---|
| `raw/S500.body` | 17010 | `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` | YES |
| `raw/S501.body` | 18784 | `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` | YES |
| `S500.receipt.json` | — | `9a0320e16cba51e8bb00df61943d3820beda4ead5cbe54ac700544d6cb81b412` | YES |
| `S501.receipt.json` | — | `c359e26e57c2affc2f46811fbe7a0f6b834017f5f2506eb963c756130dca362e` | YES |
| `fetch-log.md` | — | `61f12cc8b0896cf5b8516f18194ff71578d395222901f6b7a2604d37add98f9b` | YES |

S500 and S501 body sizes and sha256 values match the frozen sentences in
`reports/round-95/claims.md` byte-for-byte (17010 / `69fe2245…`, 18784 / `f7add697…`).

## 4. Vote-binding digest

Recipe (exact bytes from the wave task, run from the lane root; `python3 -B` added per
the spec-template rule — `-B` does not alter computation):

```
PYTHONUTF8=1 python3 -B -c "import hashlib,re;t=open('corpus/knowledge/round-95-evidence-ledger-discipline.md',encoding='utf-8').read();n=re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t);print(hashlib.sha256(n.encode('utf-8')).hexdigest())"
```

Output (written to `.ufo/waves/round-95/w1/ExecFrozen/digest.txt`, 64 hex chars only):

```
476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9
```

Identity note: the entry currently carries exactly one `admission-status:` line
(line 21, `admission-status: candidate`), so the normalizer is an identity transform
over the current bytes and the digest equals the raw entry sha256. This is the expected
pre-admission candidate state; after admission the digest will diverge from the raw sha,
which is what the trio votes bind.

## 5. Verdict

FREEZE-STATE VERIFIED: all four frozen targets exist at `6e0bf15…`; every
working-tree/freeze-commit pair tested is byte-identical; the receipt hashes match the
frozen claims sentences; the vote-binding digest is `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`.
