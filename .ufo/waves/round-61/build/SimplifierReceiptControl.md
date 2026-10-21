# SimplifierReceiptControl — C2 forged-receipt-command shape (read-only)

Seat: `CloseChousa26.SimplifierReceiptControl-10` · base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` · 2026-10-21

## Godspeed axes

| Axis | Target |
|------|--------|
| Calibration | `C2_RECEIPT_B_KILLED`: mutant **b** (conjunct delete) → nonzero on `--self-test` run |
| Coupling | Exactly one `receipt['command']==…` site (`measure.py:33`, `mutate_b`) |
| Operability | Unchanged final `print('PASS: …')` lines; no fixture/`live/` writes |
| Specificity | Control reuses the **same** receipt binding as `check()`, not a parallel assertion |

## Problem (observed)

`mutation-post.md:15,21`: mutant **b** deletes the sole command conjunct; script exits 0 (`PASS: …`). **d2** (saved `producer-receipt.json` command `+= " --forged"`) is killed only while the conjunct exists (`:18,24`). Existing in-script controls forge **normalized_result** only (`verify_icon_languages.py:156-163`, `verify_multi_icon_states.py:155-163`).

## Smallest shape: one helper, one conjunct, one in-memory probe

Factor the receipt `require(…)` in `check()` into `require_producer_receipt(...)` holding the **only** `receipt['command']==` conjunct. Call it from `check()` and from `main()` after positive rows, mirroring the selection-forgery try/except pattern.

### `corpus/verify_icon_languages.py`

Insert after `require` (before `EXPECTED`):

```python
def require_producer_receipt(receipt, hist, expected_hash, eid, raw_bytes, why):
    require(receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and receipt['evidence_id']==eid
            and receipt['stdout_sha256']==H(raw_bytes)
            and receipt['command']==f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json', why)
```

Replace `check()` receipt block (`:143-145`) with:

```python
    require_producer_receipt(receipt, hist, expected_hash, eid, raw_bytes, f'r{r}: receipt')
```

In `main()`, **before** the r48 selection forgery block (`:156`), add:

```python
    r=48
    expected_hash,eid,_,_,_=EXPECTED[r]
    hist=HIST/f'fixtures/pe-r{r}/fixture.exe'
    raw_bytes=(root/f'live/runs/round-{r}/inspection.raw.json').read_bytes()
    bad=copy.deepcopy(json.loads((root/f'live/runs/round-{r}/producer-receipt.json').read_text()))
    bad['command']+=' --forged'
    try:
        require_producer_receipt(bad, hist, expected_hash, eid, raw_bytes, 'forged receipt command')
    except AssertionError:
        pass
    else:
        raise AssertionError('forged receipt command accepted')
```

### `corpus/verify_multi_icon_states.py`

```python
def require_producer_receipt(receipt, command, expected_hash, evidence_id, raw_bytes, why):
    require(receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes), why)
```

Replace `:142-144` with:

```python
    require_producer_receipt(receipt, command, expected_hash, evidence_id, raw_bytes, f'r{round_id}: receipt')
```

In `main()`, before `:155`:

```python
    r=45
    expected_hash,evidence_id,_,_=EXPECTED[r]
    hist=HIST/f'fixtures/pe-r{r}/fixture.exe'
    raw_bytes=(root/f'live/runs/round-{r}/inspection.raw.json').read_bytes()
    command=f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'
    bad=copy.deepcopy(json.loads((root/f'live/runs/round-{r}/producer-receipt.json').read_text()))
    bad['command']+=' --forged'
    try:
        require_producer_receipt(bad, command, expected_hash, evidence_id, raw_bytes, 'forged receipt command')
    except AssertionError:
        pass
    else:
        raise AssertionError('forged receipt command accepted')
```

Round **48** / **45** match existing forged-claim rounds and `measure.py:32` probe rounds (47/42 for on-disk **d2** only).

## Why this kills **b**, not a decoy assert

- `mutate_b` (`measure.py:36-44`) removes the **only** regex-matched conjunct; helper + `check()` share that deletion — no second `command==` elsewhere.
- With conjunct intact: `bad['command']` ends with ` --forged` → `require_producer_receipt` raises → `except` → selection control runs → same `PASS:` line → exit 0.
- With conjunct deleted: all non-command receipt fields still match saved r48/r45 → `require_producer_receipt` succeeds → `else: raise … accepted` → exit ≠ 0 → **b** killed.
- Not orthogonal: a standalone `assert bad['command']!=…` would **not** track deletion inside `check()`’s binding; sharing `require_producer_receipt` ties the control to the mutant site kaika **b** attacks (`mutation-post.md:29-33`).
- **d2** unchanged: still fails in `check()` on first round load (`claims.md:60-61` hold).

## vs external battery

`replay_scenarios.py:196-204` (**N2**) forges saved receipt command on disk in `verify_named_multi_icon_states.py` acceptance; these two scripts lack that in-script path (`mutation-post.md:34-35`). In-script deepcopy matches **d2** semantics without mutating `corpus/live/`.

## Integrator checks

- `grep -cE "receipt\\['command'\\]==|receipt\\[\"command\"\\]==` → 1 per file.
- `python3 -B reports/round-61/measure.py /tmp/tree` → `C2_RECEIPT_B_KILLED=2/2`, `C2_CONTROLS_PASS=2/2`, `C2_D2_KILLED=2/2`.
- Mutant **b** last line should **not** be `PASS:` when control present.

## Installs

None.

VERDICT: Shared `require_producer_receipt` + in-memory `command += ' --forged'` probe (r48/r45) is the minimal C2 shape that kills kaika mutant **b** while preserving one conjunct and existing PASS output.
