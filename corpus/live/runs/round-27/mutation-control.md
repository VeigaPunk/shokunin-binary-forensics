# pe-mutation-control round-27

## command
```
python3 /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/verify_pe_resources.py --self-test
```

## exit
0

## stdout
```
POSITIVE ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef 1/1 RT_RCDATA name 1 language 1033 maps to authored payload
NEGATIVE REJECTED payload relation mismatch
```

## in-memory mutation (deepcopy only; inspection.json untouched)
- set `normalized_result.resources[0].payload.sha256` to 64 zeros
- `verify()` raised `ValueError`
- rejection text: `payload relation mismatch`
