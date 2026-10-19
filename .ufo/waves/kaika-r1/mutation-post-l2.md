# Post-landing mutation probe L2 — revenger C1 (ROOT/HIST split)

Lane: `.tower/worktrees/kaika/revenger-shokunin` (branch `kaika/round`, base `8bbcb4e`).
Targets: `corpus/verify_icon_languages.py`, `corpus/verify_multi_icon_states.py` (ROOT/HIST split: bytes read from current ROOT, saved `artifact.path` + receipt command pinned to `HIST`).
Method: lane `corpus/` copied to `mktemp -d /var/tmp/rev-mut-XXXX`; every mutant applied to its own fresh copy of that pristine base; each run `cwd=/`, `python3 <copy>/corpus/<verifier>`. Lane files never edited.

Detector: for each mutant, (a) the unmodified pristine-run detector (mutant must still PASS on genuine records), and (b) where the mutant weakens a specific clause, an adversarial saved-record probe that the pristine verifier rejects. `killed` = mutant fails the pristine run OR accepts a forgery the pristine verifier rejects at exit 1. Baseline failure would be inconclusive; none occurred.

## Baselines (pristine copy, cwd=/)

| run | exit | last line |
|---|---|---|
| verify_icon_languages.py | 0 | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` |
| verify_multi_icon_states.py | 0 | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` |

Probe baselines (pristine verifier vs forged saved record; all must reject):

| probe | exit | last line |
|---|---|---|
| lang artifact.path→copy ROOT (r48) | 1 | `AssertionError: r48: artifact` |
| lang receipt command→copy ROOT (r48) | 1 | `AssertionError: r48: receipt` |
| lang stdout_sha256→zeros (r48) | 1 | `AssertionError: r48: receipt` |
| lang self-consistent path forgery (r48, path+rehashed stdout) | 1 | `AssertionError: r48: artifact` |
| multi artifact.path→copy ROOT (r43) | 1 | `AssertionError: r43: artifact` |
| multi receipt command→copy ROOT (r44) | 1 | `AssertionError: r44: receipt` |
| multi stdout_sha256→zeros (r44) | 1 | `AssertionError: r44: receipt` |
| multi self-consistent path forgery (r43, path+rehashed stdout) | 1 | `AssertionError: r43: artifact` |

Forged records were written preserving original serialization (inspection: compact+`\n`; receipt: indent=2+`\n`) and only the named field(s) differ, except the self-consistent probe which also recomputes `stdout_sha256` so the receipt binding stays valid and the dropped path clause is isolated.

## Mutants

`exit` = pristine exit; `p` = adversarial-probe exit by the same mutant binary. A kill via probe means mutant `p=0` while pristine baseline probe exits 1.

| mutant | file | exit | finding (last line) | verdict |
|---|---|---|---|---|
| L-C1 | verify_icon_languages.py | 1 | `hist=fixture` (revert to ROOT); pristine fails `r47: artifact` | killed |
| L-C2 | verify_icon_languages.py | 0 / p0 | receipt-command clause deleted; accepts copy-ROOT command (probe baseline 1 `r48: receipt`) | killed |
| L-C3 | verify_icon_languages.py | 1 | `HIST=root` (repoint at copy); pristine fails `r47: artifact` | killed |
| L-C4 | verify_icon_languages.py | 0 / p0 | artifact equality loosened to sha256+bytes (path dropped); accepts self-consistent path forgery (baseline 1 `r48: artifact`) | killed |
| L-C5 | verify_icon_languages.py | 0 / p0 | command loosened to `endswith('<name> --format json')`; accepts copy-ROOT command (baseline 1 `r48: receipt`) | killed |
| L-C6 | verify_icon_languages.py | 0 / p0 | stdout_sha256 binding dropped; accepts zeroed receipt hash (baseline 1 `r48: receipt`) | killed |
| M-C1 | verify_multi_icon_states.py | 1 | `hist=fixture` (revert to ROOT); pristine fails `r42: artifact` | killed |
| M-C2 | verify_multi_icon_states.py | 0 / p0 | receipt-command clause deleted; accepts copy-ROOT command (baseline 1 `r44: receipt`) | killed |
| M-C3 | verify_multi_icon_states.py | 1 | `HIST=root` (repoint at copy); pristine fails `r42: artifact` | killed |
| M-C4 | verify_multi_icon_states.py | 0 / p0 | artifact equality loosened to sha256+bytes (path dropped); accepts self-consistent path forgery (baseline 1 `r43: artifact`) | killed |
| M-C5 | verify_multi_icon_states.py | 0 / p0 | command loosened to filename suffix; accepts copy-ROOT command (baseline 1 `r44: receipt`) | killed |
| M-C6 | verify_multi_icon_states.py | 0 / p0 | stdout_sha256 binding dropped; accepts zeroed receipt hash (baseline 1 `r44: receipt`) | killed |
| L-R1 | verify_icon_languages.py | 1 | saved artifact.path rewritten to copy ROOT (r48); fails `r48: artifact` | killed |
| L-R2 | verify_icon_languages.py | 1 | saved receipt command forged to copy ROOT (r48); fails `r48: receipt` | killed |
| L-R3 | verify_icon_languages.py | 1 | saved `same_language_resource_index` flipped 0→2 (r49); fails `r49: icon_groups` | killed |
| L-R4 | verify_icon_languages.py | 1 | saved artifact.path + receipt command both repointed at copy ROOT (r47); fails `r47: artifact` | killed |
| L-R5 | verify_icon_languages.py | 1 | saved artifact.bytes flipped 1536→1535 (r48); fails `r48: artifact` | killed |
| M-R1 | verify_multi_icon_states.py | 1 | saved artifact.path rewritten to copy ROOT (r43); fails `r43: artifact` | killed |
| M-R2 | verify_multi_icon_states.py | 1 | saved receipt command forged to copy ROOT (r44); fails `r44: receipt` | killed |
| M-R3 | verify_multi_icon_states.py | 1 | saved second-image `same_language_resource_index` flipped None→1 (r45); fails `r45: icon_groups` | killed |
| M-R4 | verify_multi_icon_states.py | 1 | saved artifact.path + receipt command both repointed at copy ROOT (r42); fails `r42: artifact` | killed |
| M-R5 | verify_multi_icon_states.py | 1 | saved artifact.bytes flipped 1536→1535 (r43); fails `r43: artifact` | killed |

## Kill ratio

```
$ awk -F'|' '/^\| [LM]-[A-Z][0-9]/ {for(i=2;i<=6;i++) gsub(/^ +| +$/,"",$i); n++; if($6=="killed") k++} END{printf "killed %d/%d = %.0f%%\n", k, n, 100*k/n}' .ufo/waves/kaika-r1/mutation-post-l2.md
killed 22/22 = 100%
```

Survivors: none. Gap vs equivalent-mutant adjudication: L-C4 and M-C4 initially read as survived against the plain `artifact.path` rewrite, but that probe changes `inspection.raw.json` bytes and is therefore also caught by the `stdout_sha256` binding — the failure was not attributable to the dropped path clause. The self-consistent forgery (path rewritten, `stdout_sha256` rehashed) isolates it: pristine verifier still rejects at `artifact`, the loosened mutants accept (exit 0). Both are genuine coverage kills, not equivalent mutants.

## Restoration and cleanup evidence

- Lane verifier sha256 before == after: `verify_icon_languages.py` `ed0ad16655e3e3c8989c80fb92c0fc35bf35dbb7dd1007f2b9d4be1d84c6bd95`; `verify_multi_icon_states.py` `5b75339c0b80ed619c08af1d87b73938e6d1a607ed0baebc89258cf6d17f49f8`. No lane file was modified; all mutation/revert cycles happened on copies rebuilt from the pristine base.
- Post-run restored-state check: both verifiers on a fresh pristine copy exit 0 with the PASS lines above.
- Mutated verifier sha256 per code mutant (record mutants leave the script byte-identical to the lane hash):
  - L-C1 `6f1eadccc1952ee6e1ed32d8bac9fe38e12af86ad507d1668714a453c7a2152e`
  - L-C2 `4d72c3fb833be66227cef2dd799633e0b908dff75b45ed6328178287f51d4500`
  - L-C3 `18d16790694455b6dab548bc28e8b808746ca02b2aca92f5740728563187fc38`
  - L-C4 `44791188807805a08c1cdae5182fc0a70ac27704b04c2b55c9f2e67e8f9b4d38`
  - L-C5 `14188969d7bbac7f0b99920a0913f28a320ee83199ece61140a634db14b11936`
  - L-C6 `19a16ceb3d8f3bd7dfc8e5b858ff4a8fdcd0b0028bb808ee413adb23afc102bb`
  - M-C1 `1c41312608d1775cabfb6c28185ae8a3073521dd3396f1edf1190c44fda1d834`
  - M-C2 `c0daa5cd40e20c05db46ddc6913278b11584c760464f57ea45f49c37bbd6a828`
  - M-C3 `d227057c1953cd7ae7e46b89c92e1d1007382c1af89e2730b7c2da70f2f965e4`
  - M-C4 `ee4908e243b088d06755d1b6c8698d1773b87d5aebf4b359f659dfc175c97dcd`
  - M-C5 `3b36980acd8a22a346a31680534b6e65a583ef929a722ad3b1e4fa452efd9c43`
  - M-C6 `af9ebb49661e22b5c75382bbad8b39ecb608cb5971efe96c0c08d6ef92d02025`
- Temp dir `/var/tmp/rev-mut-efucyvjo` deleted after evidence capture; verified with `ls -d /var/tmp/rev-mut-*` → `No such file or directory`.
