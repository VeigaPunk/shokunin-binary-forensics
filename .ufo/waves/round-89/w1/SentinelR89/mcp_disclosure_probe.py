"""Hermetic disclosure check: no live config, host commands, or lane writes."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
from types import SimpleNamespace

sys.dont_write_bytecode = True
instrument = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/census_reprobe.py')
spec = importlib.util.spec_from_file_location('sentinel_census', instrument)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
print('INSTRUMENT_SHA256=' + hashlib.sha256(instrument.read_bytes()).hexdigest())

markers = ['SYNTHETIC_REA_ENV_NEVER_DISCLOSE', 'SYNTHETIC_OTHER_ENV_NEVER_DISCLOSE',
           'SYNTHETIC_TOP_ENV_NEVER_DISCLOSE', 'SYNTHETIC_OTHER_ARG_NEVER_DISCLOSE']
class Config:
    def __init__(self, document):
        self.document = document
    def read_text(self, **kwargs):
        return json.dumps(self.document)

cases = [
    ('wrapped-valid', {'env': {'TEST': markers[2]}, 'mcpServers': {
        'rea': {'args': ['-y', 'rea-agents@6.7.0'], 'env': {'TEST': markers[0]}},
        'other': {'args': ['rea-agents@9.9.9', markers[3]], 'env': {'TEST': markers[1]}}
    }}, '6.7.0'),
    ('flat-valid', {'rea': {'args': ['rea-agents@6.7.0'], 'env': {'TEST': markers[0]}}}, '6.7.0'),
    ('env-only-pin', {'mcpServers': {'rea': {'args': [], 'env': {'TEST': 'rea-agents@9.9.9 ' + markers[0]}}}}, None),
    ('other-entry-only-pin', {'mcpServers': {'rea': {'args': []}, 'other': {'args': ['rea-agents@9.9.9']}}}, None),
    ('missing-rea', {'mcpServers': {'other': {'args': ['rea-agents@9.9.9'], 'env': {'TEST': markers[1]}}}}, None),
]
for name, document, expected in cases:
    gate.MCP_JSON = Config(document)
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
        observed = gate.mcp_spec()
        live_result = gate.live(('mcp', None))
    assert observed == expected, name
    assert not stream.getvalue(), name
    assert all(marker not in repr(live_result) for marker in markers), name
    print('MCP_ISOLATION_' + name + '=pass')

reads = []
class Guard(dict):
    def __init__(self, label, allowed, values):
        super().__init__(values)
        self.label, self.allowed = label, allowed
    def get(self, key, default=None):
        reads.append(self.label + '.' + key)
        assert key in self.allowed, 'forbidden config read: ' + self.label + '.' + key
        return super().get(key, default)
rea = Guard('rea', {'args'}, {'args': ['rea-agents@6.7.0'], 'env': {'TEST': markers[0]}})
servers = Guard('servers', {'rea'}, {'rea': rea, 'other': {'env': {'TEST': markers[1]}}})
document = Guard('document', {'mcpServers'}, {'mcpServers': servers, 'env': {'TEST': markers[2]}})
gate.json = SimpleNamespace(loads=lambda text: document, dumps=json.dumps)
gate.MCP_JSON = Config({})
assert gate.mcp_spec() == '6.7.0'
print('MCP_FIELD_ACCESS=' + ','.join(reads))

class RowFile:
    def __init__(self, text):
        self.text = text
    def is_file(self):
        return True
    def read_text(self, **kwargs):
        return self.text
class Tree:
    def __truediv__(self, suffix):
        return RowFile('| F07 | mint | probe | deliberately unstated | pending |' if suffix == gate.SEED
                       else '| K03 | mint | deliberately unstated | pending |')
gate.ROWS = {'F07': ('seed', [('mcp', None)]), 'K03': ('check', [('mcp', None)])}
gate.Path = lambda ignored: Tree()
for option in ([], ['--json']):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = gate.main(['--root', 'synthetic'] + option)
    assert code == 1
    assert 'rea-agents@6.7.0' in out.getvalue()
    assert all(marker not in out.getvalue() + err.getvalue() for marker in markers)
    print('MCP_OUTPUT_' + ('json' if option else 'text') + '=pass')
print('LIVE_MCP_CONFIG_OPENED=no')
print('HOST_PROCESSES_STARTED=no')
print('RESULT=pass')
