PASS — retained r65/r67/r68/r69 labels match frozen expectations; script-tamper and forbidden-pin probes were rejected, restored bytes pass, and the C2 exit-2 legs show no retained-gate regression.

Candidate: `4c1eeaee88fd07e442f1bd546faf77be3957d390` (archived to `/fast/scratch/hyaku/revenger-r71/R71W2RetainedGate/tree`). The committed candidate's counter SHA-256 was `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2`; gate SHA-256 was `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8`.

Commands and captured results:

- `HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r71/R71W2RetainedGate/host python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-71/measure.py /fast/scratch/hyaku/revenger-r71/R71W2RetainedGate/tree`
  - `MEASURE_EXIT=0`
  - `C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no`
  - `C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no`
  - `C2_GATE_SELFTEST=0 named_legs=1`; `HOLDS_C2_V1=yes`
  - `EMB_R65=checked_blocks=15 problems=1 exit=1`
  - `EMB_R67=checked_blocks=16 problems=0 exit=0`
  - `EMB_R68=checked_blocks=17 problems=0 exit=0`
  - `EMB_R69=checked_blocks=17 problems=0 exit=0`
  - `EMB_R68_BYTES_UNCHANGED=yes`; `EMB_R65_BYTES_UNCHANGED=yes`; `EMB_PINNED_SCRIPT_IS_S046=yes`; `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`
  - `GATE_SELFTEST=exit 0`; counter retained all ten `HOLD` rows and reported `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`.
  - The expected pre-vote state was also observed: `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`; not adjudicated by this seat.
- Candidate tree digests matched the frozen values: r68 entry `ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e`; r65 entry `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a`; pinned S046 script `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`.
- Candidate retained-entry gate detector (also independently reflected by the counter above): r65 prints the one expected M39 transcription drift at entry line 41 and `checked_blocks=15 problems=1`; r67, r68, r69 each report zero problems with 16, 17, 17 blocks respectively. The HEAD archive returned the same four result classes and counts.

Mutation probes (scratch copies only):

1. Pinned-script tamper: baseline detector on pristine r68 entry is `checked_blocks=17 problems=0` (counter `EMB_R68`); append `\n# tampered\n` to `corpus/derive_axml_anchors_r68.py`, then run `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md`. Output: `drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py`; `checked_blocks=16 problems=1` (exit 1). Mutant killed, attributed marker present. Script hashes: baseline `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`; mutant `b8a6b5fffabdee17269aad74b19abd95245d5919d9d882777d4d9bc8dcc73d8a`; restored `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`. After restoration, same detector output: `checked_blocks=17 problems=0` (exit 0).
2. Forbidden absolute pin path: mutate only scratch `corpus/embedded_output_pins.json` so the matching pin's `use` is `/etc/hostname`, run the same r68 detector. Output: `drift entry:128 pinned historical script digest mismatch: /etc/hostname (path escapes the tree)`; `checked_blocks=16 problems=1` (exit 1). The `..` escape variant `../outside.py` likewise reported `(path escapes the tree)` with one problem. Pin-file SHA: baseline `34c400c4721408a1ae485e8d6895ebb93e2744cdeeeefa0954c3c3176c0e4efd`; absolute-path mutant `c3e932addc5a44528b5cf0114024ccfde4e8ae1d9af9ba8c5d1c07eee9497af0`; restored `34c400c4721408a1ae485e8d6895ebb93e2744cdeeeefa0954c3c3176c0e4efd`. Restored r68 detector output: `checked_blocks=17 problems=0` (exit 0).

The round-71 counter's actual production 120s timeout leg and missing-entry CLI leg both returned the registered exit-2 text class without traceback; its gate self-test passed. The retained labels, digest pin, and confinement behavior therefore show no observed C2 patch regression. Scratch evidence was kept under the seat scratch directory and removed before return.