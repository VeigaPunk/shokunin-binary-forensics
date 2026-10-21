import concurrent.futures
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ARCHIVE = Path('/tmp/revenger-r61w3-W3EvmWalkMutant')
RESULTS = Path('/tmp/revenger-r61w3-W3EvmWalkMutant-results')
ENTRY = Path('corpus/knowledge/evm-saved-interface-candidates.md')
text = (ARCHIVE / ENTRY).read_text()
block = text.split('```python\n', 1)[1].split('```', 1)[0]
expected = text.split('## Provenance (Q11)', 1)[1].split('```text\n', 1)[1].split('```', 1)[0]
sha = lambda b: hashlib.sha256(b).hexdigest()
CASES = [(22, 30, 0x5b, 0x00), (26, 14, 0x11, 0x10), (24, 0, 0x7f, 0x7e)]
RESULTS.mkdir(exist_ok=False)

def manifest(root):
    return {p.relative_to(root).as_posix(): sha(p.read_bytes())
            for p in sorted(root.rglob('*')) if p.is_file()}

def detect(root):
    p = subprocess.run([sys.executable, '-B', '-c', block], cwd=root,
                       capture_output=True, text=True, timeout=15)
    return {'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr,
            'equals_provenance': p.stdout == expected,
            'stdout_sha256': sha(p.stdout.encode())}

def probe(case):
    r, offset, old, new = case
    root = Path(f'/tmp/revenger-r61w3-W3EvmWalkMutant-r{r}')
    shutil.copytree(ARCHIVE, root)
    target = root / f'corpus/fixtures/evm-r{r}/fixture.raw'
    original = target.read_bytes()
    assert original[offset] == old
    before = manifest(root)
    baseline = detect(root)
    mutated_bytes = bytearray(original)
    mutated_bytes[offset] = new
    differences = [i for i, (a, b) in enumerate(zip(original, mutated_bytes)) if a != b]
    assert len(original) == len(mutated_bytes) and differences == [offset]
    mutant = None
    mutation_error = None
    try:
        if baseline['exit'] == 0 and baseline['equals_provenance'] and baseline['stderr'] == '':
            target.write_bytes(mutated_bytes)
            mutant = detect(root)
    except Exception as exc:
        mutation_error = repr(exc)
    finally:
        target.write_bytes(original)
    restored = detect(root)
    after = manifest(root)
    restored_exactly = target.read_bytes() == original and before == after
    controls_ok = all(p['exit'] == 0 and p['equals_provenance'] and p['stderr'] == ''
                      for p in (baseline, restored)) and restored_exactly
    if not controls_ok or mutation_error or mutant is None:
        verdict = 'inconclusive'
    elif mutant['stdout'] != baseline['stdout'] or mutant['exit'] != baseline['exit'] or mutant['stderr'] != baseline['stderr']:
        verdict = 'killed-by-provenance-comparison'
    else:
        verdict = 'survived-provenance-comparison'
    output = {'case': f'r{r}', 'mutation': {'path': target.relative_to(root).as_posix(),
              'offset': offset, 'old': hex(old), 'new': hex(new), 'changed_offsets': differences},
              'before_sha256': sha(original), 'mutant_sha256': sha(mutated_bytes),
              'restored_sha256': sha(target.read_bytes()), 'restored_exactly': restored_exactly,
              'manifest_entries': len(before), 'before_manifest': before, 'after_manifest': after,
              'block_sha256': sha(block.encode()), 'entry_sha256': sha((ARCHIVE / ENTRY).read_bytes()),
              'expected_stdout_sha256': sha(expected.encode()), 'python': sys.version,
              'baseline': baseline, 'mutant': mutant, 'restored': restored,
              'mutation_error': mutation_error, 'verdict': verdict}
    (RESULTS / f'r{r}.json').write_text(json.dumps(output, indent=2) + '\n')
    return output

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(probe, CASES))
print('source_commit=ab580698212258a55e43e9bb9bf6ac78c91eae2a')
print(f'block_sha256={sha(block.encode())} expected_stdout_sha256={sha(expected.encode())}')
for out in results:
    print(f"CASE {out['case']} mutation={out['mutation']}")
    print(f"HASH before={out['before_sha256']} mutant={out['mutant_sha256']} restored={out['restored_sha256']}")
    for name in ('baseline', 'mutant', 'restored'):
        p = out[name]
        if p is None:
            print(f'{name}: not run')
        else:
            print(f"{name}: exit={p['exit']} equals_provenance={p['equals_provenance']} lines={len(p['stdout'].splitlines())} stderr={p['stderr']!r}")
    if out['mutant']:
        base_lines = out['baseline']['stdout'].splitlines()
        new_lines = out['mutant']['stdout'].splitlines()
        for index, (old, new) in enumerate(zip(base_lines, new_lines), 1):
            if old != new:
                print(f'CHANGED stdout_line={index}')
                print('- ' + old)
                print('+ ' + new)
    print(f"verdict={out['verdict']} restored_exactly={out['restored_exactly']} manifest_entries={out['manifest_entries']}")
