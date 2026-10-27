INCONCLUSIVE — C1-only probe left C2 unchanged, but the C2-only 120s counter run did not complete within the tool deadline.

Commands and observed output:
- Read frozen `claims.md`, `pre-registration.txt`, A1/A2 amendments, W1 attack inventory, and `reports/round-71/measure.py`.
- Verified `git show HEAD:reports/round-71/measure.py | sha256sum` = `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61`, matching A2. (A prior mixed shell output suggested another hash; commit-object hash is the authoritative check.)
- Built isolated base, C1-only, and C2-only archives under `/fast/scratch/hyaku/revenger-r71/R71W2CounterSeparability/`; C1-only restored base `check_embedded_outputs.py` and `SKILL.md` while retaining candidate C1 artifacts. Ran the committed counter on base and C1-only.
- Base: `C1_GATE=n/a`, `C1_LINT=n/a`, `C2_MISSING_ENTRY_EXIT2=0/1`, `C2_TIMEOUT_EXIT2=0/1`, `C2_GATE_SELFTEST=0`, `EMB_R65=15/1`, `EMB_R67=16/0`, `EMB_R68=17/0`, `EMB_R69=17/0`, pins yes, `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`.
- C1-only: `C1_GATE=checked_blocks=24 problems=0 exit=0`, `C1_LINT=... exit=0`; all C2 outputs exactly as base (`missing=0/1`, `timeout=0/1`, self-test=0, `HOLDS_C2_V1=no`). EMB labels/pin results and replay remain equal to base. This supports C1→C2 separability for the observed legs.
- C2-only and full candidate runs began, but the counter's production timeout leg is 120 seconds; the execution was interrupted at the tool's 360-second ceiling before those results were returned. No claim about C2→C1 independence is made.
- Base counter printed `SELF_MISMATCH=n/a exit=2` while `SELF_CLEAN_FIXTURE=1`, `SELF_MUTANTS_KILLED=6/6`; this is a base-tree limitation, not a C2 change finding. No traceback output was captured in the filtered display.

Counterexample / evidence: C1-only archive does not change C2 labels or retained EMB/pin/replay labels. Reverse-direction independence remains unestablished: C2-only probe did not yield output. The counter's 120-second production sleeper consumes most of the bounded invocation; do not infer pass from a started run.

Impacted axes: calibration/freshness; C1→C2 independence observed, C2→C1 independence not adjudicated. No located defect to the frozen predicates established by this probe.

Smallest safe correction: no source or predicate changes. Obtain the C2-only counter output in an invocation that can finish the registered 120-second sleeper, then compare C1 gate/lint and EMB/pin/replay/self-check diagnostics to base. Scratch was removed. 

Report: `.ufo/waves/round-71/w2/R71W2CounterSeparability.md`