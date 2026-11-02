#!/usr/bin/env python
# receipt_sweep.py - round-88 criterion R instrument: the registry-wide
# receipt sweep. Full extension of the criterion-R receipt rule (r76: "a
# receipt citing a counting command must be re-runnable to the same value
# per leg, or name the leg it does not cover") from the two rows the
# receipt_probe2 legs cover (S444/S445) to EVERY corpus/SOURCES.md row.
#
# Modes:
#   (no args)   plain sweep over ./corpus/SOURCES.md (cwd = lane root).
#               0 green (no open findings) / 1 red (open findings) /
#               2 could-not-evaluate (missing or malformed registry) /
#               64 usage (unrecognized invocation).
#   --sources PATH
#               sweep an explicit registry path instead of the default
#               (declared override; used for the prelanding dry run over a
#               staged registry — the channel legs still resolve from the
#               lane root cwd, so `git log` and the committed-file leg read
#               the lane tree, not the staged copy).
#   --selftest  hermetic self-test per the PROTOCOL Gate standard: embedded
#               synthetic tables and stubbed channel outputs only — no
#               producer call, no git, no file reads. Expected finding-ids
#               (committed in reports/round-88/claims.md and the SKILL.md
#               registry row):
#                 SWEEP_SELFTEST_MATCH_VERIFIED=ok
#                 SWEEP_SELFTEST_DRIFT_DETECTED=ok
#                 SWEEP_SELFTEST_CLOSURE_RESOLVES=ok
#                 SWEEP_SELFTEST_CLOSURE_REJECTED=ok
#                 SWEEP_SELFTEST_MALFORMED_EXIT2=ok
#                 SWEEP_SELFTEST=pass            (last line, exit 0)
#               A comparator blinded to accept any count dies with the
#               attributed last line "selftest: word-count comparator
#               accepted a wrong count"; a closure check blinded to accept
#               any supersession dies with "selftest: closure accepted an
#               unverified supersession" (both frozen sed mutants pinned in
#               reports/round-88/claims.md).
#
# Declared scan scope: the ANCHOR cell (column 7 of 11) of every
# `| S### |` row. Tokens outside this cell are outside the declared scope
# (named limitation; rows carry such tokens in source/teaches cells).
#
# Declared receipt-token set (the sweep's detection contract):
#   P1-wordcount  \b(\d+)\s+words?\b                        -> verified or closed
#   P2-prints     \bprints?\s+(\d+)\b                       -> registered
#   P3-keyval     \b([A-Za-z][A-Za-z0-9_]*)=(\d+)(?![\w.])  -> registered
#   P4-colon      \b([a-z][a-z0-9_]*):\s+(\d+)\b            -> registered
#   P5-oracle     ORACLE OK \((\d+/\d+)[^)]*\)              -> registered
# P2-P5 tokens are classified (LEG_BOUND when the anchor cites a backticked
# command anywhere in the cell, NON_COMMAND_NUMERIC otherwise) and counted
# into the register; their values are NOT re-derived by this sweep (the
# producer-coupled census pair stays with receipt_probe2's standing legs;
# oracle receipts re-derive under the standing holds probes). Receipt
# wordings outside the declared set (for example "shows 7", "prints as")
# remain unguarded by this sweep: named limitation.
#
# Word-count rule (declared): a word count is len(quote.split()) —
# whitespace split, delimiters do not split words. Every P1 row must be in
# the frozen WC_MAP below (or be a registered closure row) and its recorded
# count must equal the rule-derived count of its own quote, taken from the
# bound source, or the row must be closed by a superseding row that itself
# verifies. A quote must appear verbatim in its own row's anchor and in the
# bound source (whitespace-normalized containment, so a source line wrap
# does not mask a faithful quote).
#
# Plain-mode dependencies (disclosed, same class as receipt_probe2's legs):
# the `rea` 6.8.0 CLI on PATH (help/llms legs), `git log` over the lane
# repository (S456), the installed rea-agents package file (S463), and the
# lane tree's own committed bytes (S461). The sweep writes nothing.
import pathlib
import re
import shutil
import subprocess
import sys

SOURCES_REL = pathlib.Path('corpus') / 'SOURCES.md'

PATTERNS = {
    'P1-wordcount': re.compile(r'\b(\d+)\s+words?\b'),
    'P2-prints': re.compile(r'\bprints?\s+(\d+)\b'),
    'P3-keyval': re.compile(r'\b([A-Za-z][A-Za-z0-9_]*)=(\d+)(?![\w.])'),
    'P4-colon': re.compile(r'\b([a-z][a-z0-9_]*):\s+(\d+)\b'),
    'P5-oracle': re.compile(r'ORACLE OK \((\d+/\d+)[^)]*\)'),
}

# Frozen word-count receipt map: row id -> the receipt the row records.
# Quotes are byte-exact substrings of the rows' anchor cells at the r88
# base (preprobe receipt: reports/round-88/preprobe-map-check.log).
WC_MAP = {
    'S454': {
        'quote': 'Inspect SQLite schema and optional ordinary-table rows from a local snapshot',
        'recorded': 10,
        'channel': 'LIVE_PRODUCER',
        'cmd': ['rea', 'inspect-sqlite-database', '--help'],
    },
    'S457': {
        'quote': 'Inspect a Foundation keyed archive as an object-reference graph',
        'recorded': 9,
        'channel': 'LIVE_PRODUCER',
        'cmd': ['rea', '--llms'],
    },
    'S459': {
        'quote': 'Trace dyld load-path resolution for a Mach-O or every executable in an app bundle',
        'recorded': 16,
        'channel': 'LIVE_PRODUCER',
        'cmd': ['rea', 'trace-dylib-resolution', '--help'],
    },
    'S462': {
        'quote': 'Decode compiled storyboard and nib archives from an app bundle',
        'recorded': 11,
        'channel': 'LIVE_PRODUCER',
        'cmd': ['rea', 'decode-interface-builder', '--help'],
    },
    'S456': {
        'quote': 'the four evidence logs the adjudication commit cited but did not carry',
        'recorded': 11,
        'channel': 'COMMITTED_GIT',
        'cmd': ['git', 'log', '--format=%s', '-1', '46c605c'],
    },
    'S461': {
        'quote': 'the multi-ref token prints as `…evidence.md:57,:148,`, so the first alternative can never be followed by a space',
        'recorded': 19,
        'channel': 'COMMITTED_FILE',
        'path': 'corpus/lessons/round-81-verifier-spotcheck.md',
    },
    'S463': {
        'quote': 'throw new TypeError(`Unsupported NIBArchive format version ${formatVersion}`)',
        'recorded': 10,
        'channel': 'PRODUCER_PKG',
        'pkg_rel': 'node_modules/rea-agents/dist/artifacts/apple/NibArchive.js',
    },
}

# Frozen closure map: drifted row -> the superseding row that must close it.
CLOSURE_MAP = {
    'S454': 'S474',
    'S456': 'S475',
    'S459': 'S476',
    'S461': 'S477',
    'S462': 'S478',
    'S463': 'S479',
}


def norm(text):
    return ' '.join(text.split())


def counts_match(recorded, derived): return recorded == derived


def closure_ok(closure_recorded, quote_ws, quote_in_row, supersedes_ok): return quote_in_row and supersedes_ok and counts_match(closure_recorded, quote_ws)


def fetch_channel(entry, stubs=None):
    """Return the bound source text for a WC_MAP entry, or None."""
    if stubs is not None:
        return stubs.get(entry['channel'])
    channel = entry['channel']
    try:
        if channel in ('LIVE_PRODUCER', 'COMMITTED_GIT'):
            exe = shutil.which(entry['cmd'][0])
            if exe is None:
                return None
            run = subprocess.run([exe] + entry['cmd'][1:], capture_output=True, encoding='utf-8', errors='replace')
            if run.returncode != 0:
                return None
            return run.stdout
        if channel == 'COMMITTED_FILE':
            return pathlib.Path(entry['path']).read_text(encoding='utf-8')
        if channel == 'PRODUCER_PKG':
            rea = shutil.which('rea')
            if not rea:
                return None
            pkg = pathlib.Path(rea).resolve().parent / pathlib.Path(*entry['pkg_rel'].split('/'))
            return pkg.read_text(encoding='utf-8')
    except OSError:
        return None
    return None


def parse_rows(text):
    """Return (rows, malformed_ids). rows: (id, anchor)."""
    rows = []
    malformed = []
    for line in text.splitlines():
        m = re.match(r'^\|\s*(S\d{3,})\s*\|', line)
        if not m:
            continue
        fields = line.split('|')
        if len(fields) != 13:
            malformed.append((m.group(1), len(fields)))
            continue
        rows.append((m.group(1), fields[6]))
    return rows, malformed


def sweep(text, stubs=None, out=None):
    """Run the sweep over a registry text. Returns the process exit code."""
    if out is None:
        out = sys.stdout
    rows, malformed = parse_rows(text)
    if malformed:
        for rid, nf in malformed:
            out.write('could-not-evaluate: malformed row %s (NF=%d)\n' % (rid, nf))
        return 2
    out.write('SWEEP_ROWS_SCANNED=%d\n' % len(rows))
    anchor_by_id = dict(rows)
    token_totals = dict((pid, 0) for pid in PATTERNS)
    receipt_rows = 0
    non_command_rows = 0
    open_findings = 0
    closed = 0
    verified = 0
    closure_ids = set(CLOSURE_MAP.values())
    for rid, anchor in rows:
        hits = {}
        for pid, rx in PATTERNS.items():
            found = rx.findall(anchor)
            if found:
                hits[pid] = found
                token_totals[pid] += len(found)
        if not hits:
            continue
        if '`' not in anchor:
            non_command_rows += 1
            out.write('REGISTER %s NON_COMMAND_NUMERIC tokens=%s\n' % (
                rid, ','.join(sorted(hits))))
            continue
        receipt_rows += 1
        if 'P1-wordcount' in hits:
            if rid in closure_ids:
                continue  # closure rows verify via their drifted target below
            if rid not in WC_MAP:
                open_findings += 1
                out.write('WC_UNMAPPED %s\n' % rid)
                continue
            entry = WC_MAP[rid]
            quote = entry['quote']
            if quote not in anchor:
                open_findings += 1
                out.write('WC_QUOTE_ABSENT %s\n' % rid)
                continue
            source_text = fetch_channel(entry, stubs)
            if source_text is None or norm(quote) not in norm(source_text):
                open_findings += 1
                out.write('WC_CHANNEL_UNREACHABLE %s channel=%s\n' % (rid, entry['channel']))
                continue
            derived = len(quote.split())
            if counts_match(entry['recorded'], derived):
                verified += 1
                out.write('WC_%s=VERIFIED recorded=%d derived=%d\n' % (rid, entry['recorded'], derived))
                continue
            closure_id = CLOSURE_MAP.get(rid)
            was_closed = False
            if closure_id is not None and closure_id in anchor_by_id:
                canch = anchor_by_id[closure_id]
                cm = PATTERNS['P1-wordcount'].search(canch)
                closure_recorded = int(cm.group(1)) if cm else None
                was_closed = closure_ok(
                    closure_recorded, derived, quote in canch,
                    ('supersedes %s' % rid) in canch)
                if was_closed:
                    closed += 1
                    out.write('WC_%s=CLOSED recorded=%d derived=%d by=%s(%d)\n' % (
                        rid, entry['recorded'], derived, closure_id, closure_recorded))
            if not was_closed:
                open_findings += 1
                out.write('WC_%s=DRIFT recorded=%d derived=%d closed=no\n' % (
                    rid, entry['recorded'], derived))
    out.write('SWEEP_RECEIPT_ROWS_DETECTED=%d\n' % receipt_rows)
    out.write('SWEEP_NON_COMMAND_NUMERIC_ROWS=%d\n' % non_command_rows)
    for pid in sorted(PATTERNS):
        out.write('SWEEP_TOKENS_%s=%d\n' % (pid, token_totals[pid]))
    out.write('SWEEP_WORDCOUNT_VERIFIED=%d/%d\n' % (verified, len(WC_MAP)))
    out.write('SWEEP_WORDCOUNT_CLOSED=%d/%d\n' % (closed, len(CLOSURE_MAP)))
    out.write('SWEEP_WORDCOUNT_OPEN=%d\n' % open_findings)
    out.write('SWEEP_VERDICT=%s\n' % ('green' if open_findings == 0 else 'red'))
    return 0 if open_findings == 0 else 1


class _Sink(object):
    def __init__(self):
        self._parts = []

    def write(self, s):
        self._parts.append(s)

    def getvalue(self):
        return ''.join(self._parts)


FIVE = 'alpha beta gamma delta epsilon'
SELFTEST_STUBS = {'STUB_CHANNEL': 'prefix ' + FIVE + ' suffix'}
_ANCHOR_A = '`stub-cmd` records "%s" (5 words)' % FIVE
_ANCHOR_B = '`stub-cmd` recorded "%s" (4 words)' % FIVE
_ANCHOR_B2_OK = '`stub-cmd` closing: supersedes S702 "%s" (5 words, whitespace rule)' % FIVE
_ANCHOR_B2_BAD = '`stub-cmd` closing: supersedes S702 "%s" (6 words, whitespace rule)' % FIVE

SELFTEST_TABLES = {
    'clean': (
        '| S701 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
        '| S702 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
    ) % (_ANCHOR_A, _ANCHOR_B),
    'with_closure': (
        '| S701 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
        '| S702 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
        '| S703 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
    ) % (_ANCHOR_A, _ANCHOR_B, _ANCHOR_B2_OK),
    'bad_closure': (
        '| S701 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
        '| S702 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
        '| S703 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d | used |\n'
    ) % (_ANCHOR_A, _ANCHOR_B, _ANCHOR_B2_BAD),
    'malformed': (
        '| S701 | src | own-work | A | scope | %s | stub | mined | 2026-11-02 | 90d |\n'
    ) % _ANCHOR_A,
}


def run_selftest(out=None):
    """Hermetic self-test: synthetic tables, stub channels only."""
    if out is None:
        out = sys.stdout
    saved_map = dict(WC_MAP)
    saved_closure = dict(CLOSURE_MAP)
    g = globals()
    try:
        g['WC_MAP'] = {
            'S701': {'quote': FIVE, 'recorded': 5, 'channel': 'STUB_CHANNEL'},
            'S702': {'quote': FIVE, 'recorded': 4, 'channel': 'STUB_CHANNEL'},
        }
        g['CLOSURE_MAP'] = {'S702': 'S703'}
        # ST1: the comparator accepts the correct receipt and rejects the
        # wrong count (drift detected, exit 1).
        buf = _Sink()
        rc = sweep(SELFTEST_TABLES['clean'], SELFTEST_STUBS, buf)
        text = buf.getvalue()
        if 'WC_S701=VERIFIED recorded=5 derived=5' not in text:
            out.write('SWEEP_SELFTEST=fail (ST1: correct receipt not verified)\n')
            out.write('selftest: word-count comparator rejected a matching count\n')
            return 1
        out.write('SWEEP_SELFTEST_MATCH_VERIFIED=ok\n')
        if rc != 1 or 'WC_S702=DRIFT recorded=4 derived=5 closed=no' not in text or 'SWEEP_WORDCOUNT_OPEN=1' not in text:
            out.write('SWEEP_SELFTEST=fail (ST1: drift not detected)\n')
            out.write('selftest: word-count comparator accepted a wrong count\n')
            return 1
        out.write('SWEEP_SELFTEST_DRIFT_DETECTED=ok\n')
        # ST2: a correct closure row closes the drift (exit 0); a
        # wrong-count closure row does not (still open, exit 1).
        buf2 = _Sink()
        rc2 = sweep(SELFTEST_TABLES['with_closure'], SELFTEST_STUBS, buf2)
        t2 = buf2.getvalue()
        if rc2 != 0 or 'WC_S702=CLOSED recorded=4 derived=5 by=S703(5)' not in t2 or 'SWEEP_WORDCOUNT_OPEN=0' not in t2:
            out.write('SWEEP_SELFTEST=fail (ST2: correct closure not resolved)\n')
            out.write('selftest: closure rejected a verified supersession\n')
            return 1
        out.write('SWEEP_SELFTEST_CLOSURE_RESOLVES=ok\n')
        buf3 = _Sink()
        rc3 = sweep(SELFTEST_TABLES['bad_closure'], SELFTEST_STUBS, buf3)
        t3 = buf3.getvalue()
        if rc3 != 1 or 'WC_S702=DRIFT' not in t3 or 'SWEEP_WORDCOUNT_OPEN=1' not in t3:
            out.write('SWEEP_SELFTEST=fail (ST2: wrong-count closure accepted)\n')
            out.write('selftest: closure accepted an unverified supersession\n')
            return 1
        out.write('SWEEP_SELFTEST_CLOSURE_REJECTED=ok\n')
        # ST3: a malformed registry row is could-not-evaluate (exit 2).
        buf4 = _Sink()
        rc4 = sweep(SELFTEST_TABLES['malformed'], SELFTEST_STUBS, buf4)
        if rc4 != 2:
            out.write('SWEEP_SELFTEST=fail (ST3: malformed table not exit 2)\n')
            out.write('selftest: malformed registry accepted as evaluable\n')
            return 1
        out.write('SWEEP_SELFTEST_MALFORMED_EXIT2=ok\n')
        out.write('SWEEP_SELFTEST=pass\n')
        return 0
    finally:
        g['WC_MAP'] = saved_map
        g['CLOSURE_MAP'] = saved_closure


def main(argv):
    if argv == ['--selftest']:
        return run_selftest()
    if len(argv) == 2 and argv[0] == '--sources':
        path = pathlib.Path(argv[1])
        if not path.exists():
            sys.stderr.write('could-not-evaluate: registry missing: %s\n' % path)
            return 2
        return sweep(path.read_text(encoding='utf-8'))
    if argv:
        sys.stderr.write('usage: receipt_sweep.py [--selftest] [--sources PATH]\n')
        return 64
    if not SOURCES_REL.exists():
        sys.stderr.write('could-not-evaluate: registry missing: %s\n' % SOURCES_REL)
        return 2
    return sweep(SOURCES_REL.read_text(encoding='utf-8'))


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    sys.exit(main(sys.argv[1:]))
