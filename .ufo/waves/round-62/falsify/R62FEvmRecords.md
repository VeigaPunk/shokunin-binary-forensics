GRADE: HOLDS — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09 candidate; record-identity/label attack)

Frozen revision `d97761952be256d145d298022de03091de91d358`; claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Target file `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` sha256 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`, 450 lines / 42818 bytes. Archive `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d97761952be256d145d298022de03091de91d358 | tar -x` to `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmRecords`; base archive likewise at `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmRecords/base`.

## Observation (commands and output)

- Extract `sed -n '292,422p' <target> > readout.py` (sha256 `740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb`); `python3 -B readout.py <archive-root>` → exit 0, stderr 0 bytes; stdout 8 lines sha256 `aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf`; `diff` against the entry's `## Provenance` stdout → empty. Same command against the `a3498e25` archive → exit 0, empty stderr, identical stdout. `diff -rq base/corpus/fixtures corpus/fixtures` and `diff -rq base/corpus/live corpus/live` → no differences; Python 3.14.8.
- Re-opened all seven records at the archive and compared every printed identity field to the actual record JSON: `python3 -B /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmRecords/record_fields.py /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmRecords /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmRecords/out.txt` → exit 0, stderr 0 bytes, `record_field_mismatches= 0`; output `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmRecords/record_fields.out` (8 lines). This covers operation, `provider.id`, `provider.name`, `provider.version`, `evidence_id`, `authority`, `confidence`, the three flags, and the record-file sha256. All full 64-hex values, no truncation.
- Record-file sha256 (actual = printed) and printed evidence id:
  - r19 `e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948` `ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42`
  - r21 `395c4f48e7efd7eafb07cc8c4b82c0fcea4e7a060885a97ee463da0faafdb7d7` `ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85`
  - r22 `c55f69727ce2e62707ae0f9203c338efe57e6aeadc7fb5f5cd939bee3f9b3a33` `ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b`
  - r23 `ce9fe51536af461ef2deb19b8cf8ff3582dba736abc2747b07ab845d3aaac2af` `ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201`
  - r24 `ec9e147db2b042f4d991816fa2a02fe95373de31956730fd1eb4cce5763742cd` `ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e`
  - r25 `4f677a209d08c3f9e531191aea9cdc58533898b9f9ed2394b3db63a0b8d448cf` `ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579`
  - r26 `bf2b2337b83f694ff9c7f9dfafbd9074de9b3310c52609fb41c993d9c782fc3c` `ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090`
- All seven records: `operation=inspect_evm_interface`; `provider.id=evmole-interface`; `provider.name=REA EVM interface adapter`; `provider.version=evmole@0.9.3`; `authority=shipped-artifact`; `confidence=inferred`; flags `evidence_kind=inferred`, `discovery_completeness=unknown`, `runtime_execution=not-performed`.
- Recorded labels checked in context: target `:73-75` "Those are **recorded** fields of the saved file: this entry does not authenticate them and claims no origin, completeness or authenticity from them."; `:132-135` "The provider id, version, evidence id, authority and confidence are recorded fields of the saved files. A digest binds the bytes it hashed and nothing further: not provenance, acquisition completeness, producer origin or deployment authenticity"; `:159-161` "`authority` is recorded and is **not read** as origin, custody or authenticity"; `:25-29` "not … present producer capability … no producer was called"; `:194` "No current capability is claimed; the records were not re-run."

## Inference

- Every printed record-identity value is a faithful literal reading of the seven saved records, and the entry labels those fields as recorded/not authenticated. No printed label presents the provider's recorded `authority`, `confidence`, provider version, or evidence id as present producer capability, origin, custody, completeness or authenticity. [INFERENCE] The record metadata is context for the byte comparison, not an authentication claim.

## Unknown / outside my assigned axis

- S031's `corpus/SOURCES.md` scope enumerates fixture bytes and saved bytecode hex/size/digest plus function candidate literals, and says "not provider semantics or completeness"; item 3's operation/provider/evidence-id/authority/confidence/flags literals are not enumerated there, and S026 (the row for what the seven saved outputs contain) is not cited by this entry. No record value or label is changed by this; it is a Q01 scope question for the AllCriteria/Source seats.
- Inventory granularity, not a record-value defect: the rows "r19 bytecode kind / authenticity / hardfork" and "r19 artifact bytes and encoding" name only `.kind` and `.bytes`, while the stdout prints `deployment_authenticity`, `hardfork` and `encoding`; the per-case observation counts (r19 one, r21 one, r22 two) and the 11-tuple count are list lengths, not separate printed count fields. All are derivable from the printed lists/fields but are outside this seat's record-identity check.
- No probe of deployed contracts, chain, RPC, provider re-run, or current producer capability; README `C04` and `C09` still read `uncovered` at `d9776195`, K remains 4/14.

## Verdict

HOLDS for the assigned record-identity and recorded-label attack; no repair and no admission. Admission remains L1's decision after all fresh seats.

Installs: none (no pacman/uv/cargo/npm transaction, no service restart; tools: git archive, sha256sum, python3 3.14.8 stdlib, curl read-only re-open of the pinned S028 files).
