GRADE: BROKEN — corpus/knowledge/round-62-commonjs-require-name-evidence.md (Q13 boundary; fails Q11, Q13 n/a basis false)

Seat RevengerR61-2.R62FJsQ13Boundary (critic; not author/corrector). Frozen revision `d97761952be256d145d298022de03091de91d358`
(`git -C <repo> archive d977… | tar -x` into /fast/scratch/hyaku/revenger-r62/R62FJsQ13Boundary/tree).
Candidate blob `480f62c490b43d7c21248caf8905357d1bb67726`, file SHA-256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`, 296 lines.
Criteria: tree `corpus/QUALITY.md:23` (Q11), `:25` (Q13); `reports/round-62/claims.md:98-101`; `corpus/lessons/round-62.md:19,93-101`.

## Observation
O1. Guard-credit scan (`grep -i 'guard|verif|detect|enforc|deletion|mutant|recheck|checker|fail closed|covered'`): no verifier is credited and no mutant
    or clause-deletion detection is claimed (:10, :65, :274-276, :296). The `recheck:` header (:4) gives the readout command, exit 0, 25 lines and stdout
    digest. It is a reproduction, not a deletion guard. Old receipt-command mutant b (M22, lessons/round-61.md:38) is not mentioned and stays separate.
O2. Q13 credit itself HOLDS: Q13 only limits credit; the entry credits no check as a guard, so none needs a demonstrated deletion kill.
O3. `git diff --stat a3498e25… d977… -- corpus/fixtures corpus/live` printed nothing, so the fixtures and saved records did not change.
O4. Bounded reproduce, done once with cwd=/ and TMPDIR set to seat scratch: I extracted the §Code block to scratch `readout.py` and ran
    `python3 -B readout.py tree` -> exit 0, 25 lines, SHA-256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416`,
    `cmp` IDENTICAL to the in-entry stdout block. The extracted code SHA-256 is `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac`.
O5. Values the entry asserts that appear in no in-entry command output and carry no "recorded, not re-derived" label
    (scanned all hex/count tokens outside fences against the stdout):
    a. `readout.py` SHA-256 `31dac211…` (:80). The value is correct (O4), but the entry shows no hashing command and no output for it.
    b. stdout SHA-256 `58b63dd9…` and "25 stdout lines"/"(25 lines)" (:4, :80, :253). §Reproduce (:74-78) shows only
       `python3 -B readout.py tree        # exit 0; 25 stdout lines`, which is a comment, not output. No `sha256sum`/`wc` command or output appears.
       The value is correct (O4).
    c. "8 words" for the S029 quote (:248). For `Set value to ? GetV(value, propertyName).` I get 6 whitespace tokens and 6 alphabetic words; the
       entry's own normalized form gives 10 tokens. No stated convention yields 8. This count is neither derived nor recorded, and it appears wrong.
       (The ≤25-word Gate limit is still met.)
    d. The S029 single-page SHA-256 `06db92a8…`, the draft date and the clause anchors (:1, :248) are copied from `SOURCES.md:43`. The entry says
       "cited here as the existing row" but never uses the Q11 label "recorded, not re-derived", while it does use that label for items 6-7.
O6. Q11 inventory (:255-272) covers items 1-30 only. The header lines, §Sources and the §Reproduce digest and line-count sentences are not inventoried.
    Rows 23-30 say "no output claimed", yet :67 asserts a byte fact ("left byte-unchanged") with no derivation and no recorded label.
O7. The Q13 section says (:276) "every value above rests on the in-entry derivation in §Reproduce (a command and that command's printed output)".
    L27 (:65) repeats "every value rests on the in-entry derivation". O5a-d are counterexamples above :276, so the sentence is false.
    The Q13 row (:296) and the Q11 "pass" row (:294) both rest on it.
O8. Wording tension: :23 says "the bound is enforced, not assumed" and :290 says "enforced in the code". The exactly-one-match fact is not printed;
    it rests only on exit status 0 plus `raise SystemExit` (:163-164). That contradicts :276/:296 "no value is presented as covered by any check".
    It is a legitimate code-plus-exit derivation, not a clause-deletion credit, so this is nonfatal.
O9. :80 says "The stdout carries no path". The stdout carries the relative paths `dir`, `source_file`, `path` and `record.path`
    (stdout lines 2, 4, 8). Only the archive root is absent. This is nonfatal wording.

## Inference
I1. [INFERENCE] The no-guard stance is honest about verifiers (O1-O2). Its sentence "every value rests on the in-entry derivation" does the job the
    brief warns about: no-credit language stands in for Q11 completeness that does not hold (O5-O7).
    Under QUALITY:23 ("a value is correct when re-derived but the entry carries no derivation"), O5a and O5b fail even though the values are
    correct. O5c fails because it is underived and apparently incorrect.
I2. [INFERENCE] This is a missing requirement, not just a tradeoff: the round claims say Q11 "applies to every asserted value throughout the entry,
    not just prose" (claims.md:98). Under that rule, digests and counts in the header and in §Reproduce count.

## Unknown
U1. Whether L1 treats the S029 row-citation wording (O5d) as an adequate "recorded" label. This seat reads it as insufficient by the letter of Q11.
U2. Whether some convention gives 8 words (O5c). None is stated in the entry.
U3. I did not audit the other Q rows or the EVM candidate; those belong to sibling seats.

## Impacted axes
Coverage K: C04 cannot count toward the 5/14 target while Q11 fails. README C04 stays `uncovered` (tree README:33), which is consistent with that.
No harm to the frozen holds was observed.

## Smallest safe correction (not applied)
1. In §Reproduce, add `sha256sum readout.py` and `python3 -B readout.py tree > out; echo $?; wc -l < out; sha256sum out`, each with its exact output.
2. Mark the S029 page digest, draft date and anchors as "recorded from SOURCES S029, not re-derived". Fix "8 words" to a derived count with its
   convention (6 whitespace tokens), or label it.
3. Narrow :65/:276 to "each value in items 1-13 rests on…", list the recorded or underived exceptions, and extend the Q11 inventory to the header,
   §Sources and §Reproduce. Optionally reword :80 to "no absolute path" and :276/:296 to acknowledge the exit-status one-match condition.

VERDICT: BROKEN (Q11; Q13 n/a rationale rests on a false completeness sentence). Q13 guard-credit, taken alone, holds. No repair, no admission.
Installs: none. Scratch: /fast/scratch/hyaku/revenger-r62/R62FJsQ13Boundary/{tree,readout.py,stdout.expected,stdout.actual,tmp}.
