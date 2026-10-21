GRADE: PARTIAL — frozen candidate d97761952be256d145d298022de03091de91d358; source census + snapshot manifest HOLD, C04 Q11 count/label defects

Frozen: candidate d97761952be256d145d298022de03091de91d358 (C04 entry sha256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; C09 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`). Claimbase `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Archive: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d977619… | tar -x -C /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FSourceCensus/tree` → exit 0; base a3498e25 extracted likewise; `TMPDIR=/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FSourceCensus/tmp`.

## Observation (commands + exact output)
1. `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → EXIT=0:
   `revenger W04 S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes`
   `revenger W04 S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes`
   `revenger W04 S029 duplicate url tc39.es/ecma262 across scopes`
   `revenger ok /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`
2. Frozen `census --file <tree>/corpus/SOURCES.md` → `rows 31`, `tier.A 29`, `tier.C 2`, `status.mined 26`, `status.queued 1`, `status.rejected 4`, `FLEET.missing 0`, EXIT=0. Live census identical (31 rows; same tier/status).
3. Frozen `validate --file <tree>/corpus/SOURCES.md` → same three W04 + `file ok …/corpus/SOURCES.md`, EXIT=0; no E01-E12.
4. `git diff a3498e25 d977619 -- corpus/SOURCES.md` → 9 insertions, 0 deletions: 4 rows (S028-S031) + 5 Paths/Search-log lines. Base registry 27 rows, zero S028-S031; candidate 31. No existing S001-S027 row changed; README C04:33/C09:38 remain `uncovered`.
5. Snapshot manifest: 4 entries, each size+sha256 matches the frozen bytes — instructions.py 10700/`49dd6155…`; runtime.py 1971/`a2801c41…`; statements.html 956160/`a23fc93c…`; scripts-modules.html 1033596/`a5444406…`; no other files. Manifest self-sha256 `cd26810aeecf4ea7f0824f5ef88e16176541c439eedcde8fe2cf36f67c057c4b`.
6. Reopen evidence: S028 runtime.py:29-30 quote and opcode anchors (:55,:104,:106,:109,:118,:121,:122,:125,:153) match saved bytes; S029 GetV and Table54 ImportName quotes found in the saved multipage chapters; S030 record hashes `7c3ba8…`/`331ec2…` and evidence ids `ev_4a93…`/`ev_66f5…` match; S031 r19 limitations[4] exact ("Original carrier and decoded bytecode SHA-256 are distinct identities; SHA-256 is not the Ethereum Keccak code hash."), r19 subject `294e6f…` vs decoded `d1086b…`, r24 decoded `b69834…`, r24 truth embedded_pattern_hex `63deadbeef14601057`.
7. S029 single-page digest independently reopened read-only: `curl … https://tc39.es/ecma262/` → HTTP 200, 7,629,271 B, sha256 `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f` = the row anchor; version line "Draft ECMA-262 / October 16, 2026" and both quotes present. Saved in scratch only.
8. Reproduce on both archived trees: C04 `readout.py` sha256 `31dac211…`, exit 0, 25 lines, stdout sha256 `58b63dd9…` = entry; C09 exit 0, 8 lines; Provenance 8/8 lines exact; inventory 67/67 field values match output.

## Inference
- Registry: append-only, valid, tier A; the three W04 are the disclosed cross-scope reopens (S024 supersedes S008; S028 beside S016; S029 beside S022), not errors. No forged reopen: all quoted anchors and record/fixture literals check against saved bytes, and the one non-snapshot digest (S029 single page) was re-opened today and matches.
- Both candidates' substantive derivations reproduce exactly at d977619 and a3498e25; no fixture/record byte changed.

## Unknown / gaps
- The single-page ECMA bytes are not preserved in the manifest (only the two multipage chapters); the digest is verified by a fresh public read, not a saved snapshot.
- Q01-Q13 admission decisions and final K remain with fresh seats/L1; no verifier, README flip or held flip was made here (not assigned).

## Findings (no repair, no admission)
F1 Q11 — C04 `corpus/knowledge/round-62-commonjs-require-name-evidence.md:248` says the §14.3.3.3 quote is "8 words". The quoted text has 6 whitespace tokens (`python3 -B`: `len("Set value to ? GetV(value, propertyName).".split())` → 6); `R62SourceEcma.md:36` records 6. No in-entry command/output; wrong count. Minimal correction: 6, or drop the count.
F2 Q11 labeling — C04 :1 and :248 assert S029's single-page sha256 without an in-entry derivation and without a "recorded/not re-derived" label. The value is verified correct (item 7), so this is a label gap, not forgery. Minimal: label it recorded from the S029 row anchor (or drop it; the row carries it).
F3 wording/scope — C04 :64 "The one network access this round" is false if "round" means round 62: the round's own records show the S028 execution-specs fetches and S029 single+multipage opens (`R62SourceEvmSpec.md:9-20`, `R62SourceEcma.md:12-20`). Minimal: "for this entry".
F4 pointer precision (nonfatal) — C09 `…evm-dispatch-byte-evidence.md:221` inventory row "pattern bytes and length" cites only `summary.pattern_hex`; the 9-byte value is `summary.pattern_length`, printed at stdout line 449. Value present; pointer incomplete.

VERDICT: source census and snapshot manifest HOLD; C09 passes this lane's source/derivation checks; F1 fails strict Q11 and C04 cannot be recommended for admission until minimally corrected; F2 needs the recorded label; F3/F4 are wording/pointer issues. No admission, no README flip, no repair. Installs: none.
