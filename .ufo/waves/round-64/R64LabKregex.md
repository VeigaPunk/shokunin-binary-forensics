# R64LabKregex — bounded current-map backing sweep

## Verdict

**No current-map backed-regex prefix false positive found.** The sweep covered all 14 README rows, 13 knowledge-column path occurrences and 9 distinct files. Every matched path exists and none contains `admission-status: rejected`, either in the frozen first-2000-character window or anywhere else. All seven held rows have existing, non-rejected backing: **K_HELD_BACKED = K_HELD_BACKED_STRICT = 7/14**. No missing/rejected file contributes to a held row.

Axes: completeness (14/14 rows), predicate fidelity (frozen regex/column/marker window), noninterference (read-only probe; only this report written).

## Observed source evidence

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py:25-35`: `rows`, `held`, and `backed` use the exact row/status regexes and `re.findall(r"knowledge/[\w.-]+\.md", line.split("|")[3])`; backing requires at least one match and every matched file to satisfy `is_file()`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py:38-49`: `rejected_marked` tests the literal marker in the first 2000 decoded characters, returns false on `OSError`, and is called by `strict` at line 48; `strict` also requires every matched file to exist. Counts are printed at lines 35 and 49.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md:28-43`: the relevant field is `line.split("|")[3]` (fourth split field because the initial pipe produces an empty field; third visible table column, **knowledge entries**). Work evidence is `[4]` and is not backing.
- The two retained rejected files are cited only in work evidence: C04 `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/commonjs-destructured-require-edges.md:5`; C09 `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/evm-saved-interface-candidates.md:5`. Both exist and have the rejection marker inside the first 2000 characters, but neither is selected by the frozen backing-column predicate.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log:1-4` independently records the same baseline 7/14 counts. The sweep below is a separate observation of the working tree, not a rerun of that receipt.

Semantic tracing availability: requesting `xd://lsp` returned `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` No language server was available; literal search located the definitions/call sites and the cited source sections were read directly. No grep result is claimed as semantic-reference proof.

## Interpretation and limits

**Observed:** no selected knowledge token is a truncated regex prefix (`KNOWLEDGE_TOKEN_PREFIX_MISMATCHES=[]`), and no current selected file is missing or rejected. Consequently the strict rejection filter removes no current backed row.

**Inference:** with this observed map **and referenced-file contents unchanged**, strict cannot differ from ordinary backing. They are not generally equivalent: strict can decrease if an otherwise-backed held row cites a file containing the marker in its first 2000 characters. The regex itself lacks an ending token delimiter, so prefix false positives remain possible for different path tokens; this sweep establishes their absence here, not parser robustness on arbitrary future maps.

Remaining unknowns: admission quality is outside this existence/marker probe; later parallel edits and the post-integration map are not covered. C07 was still `frontier` when the sweep ran. No unresolved dependency affects the requested current-map result. Confidence: **high** for this observed working-tree snapshot.

## Full sweep command

The command reads only the README and cited files. It mirrors the frozen first-2000-character rejection predicate, also checks markers anywhere, reports every matched path, and separately reports excluded work-evidence citations.

```sh
python3 -B -c 'import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
rows = [line for line in (root / "corpus/README.md").read_text(encoding="utf-8").splitlines() if re.match(r"^\| C[0-9]+ ", line)]
rx = re.compile(r"knowledge/[\w.-]+\.md")
marker = "admission-status: rejected"
def inspect(rel):
    p = root / "corpus" / rel
    exists = p.is_file()
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        text = ""
    return exists, marker in text[:2000], marker in text
held = backed = strict = occurrences = 0
seen = set()
missing = set()
rejected = set()
held_missing = set()
held_rejected = set()
prefix_mismatches = []
excluded = []
print("ROOT=" + str(root))
print("COLUMN=line.split(\"|\")[3]; REGEX=" + rx.pattern)
for line in rows:
    fields = line.split("|")
    row = fields[1].strip()
    status = fields[-2].strip()
    is_held = bool(re.search(r"\| held \|$", line))
    paths = rx.findall(fields[3])
    data = [(rel, *inspect(rel)) for rel in paths]
    row_backed = is_held and bool(paths) and all(item[1] for item in data)
    row_strict = row_backed and not any(item[2] for item in data)
    held += is_held
    backed += row_backed
    strict += row_strict
    print(f"ROW {row} status={status} matches={len(paths)} backed={int(row_backed)} strict={int(row_strict)}")
    for rel, exists, reject_prefix, reject_anywhere in data:
        occurrences += 1
        seen.add(rel)
        if not exists:
            missing.add(rel)
            if is_held: held_missing.add((row, rel))
        if reject_prefix:
            rejected.add(rel)
            if is_held: held_rejected.add((row, rel))
        print(f"  {rel} is_file={int(exists)} rejected_first_2000={int(reject_prefix)} rejected_anywhere={int(reject_anywhere)}")
    for token in re.findall(r"`([^`]+)`", fields[3]):
        if token.startswith("knowledge/") and rx.findall(token) != [token]:
            prefix_mismatches.append((row, token, rx.findall(token)))
    for rel in rx.findall(fields[4]):
        excluded.append((row, rel, *inspect(rel)))
for row, rel, exists, reject_prefix, reject_anywhere in excluded:
    print(f"EXCLUDED_WORK_EVIDENCE {row} {rel} is_file={int(exists)} rejected_first_2000={int(reject_prefix)} rejected_anywhere={int(reject_anywhere)}")
print(f"ROWS={len(rows)} KNOWLEDGE_OCCURRENCES={occurrences} UNIQUE_PATHS={len(seen)}")
print(f"K_HELD={held}/{len(rows)}")
print(f"K_HELD_BACKED={backed}/{len(rows)}")
print(f"K_HELD_BACKED_STRICT={strict}/{len(rows)}")
print(f"MISSING={sorted(missing)} REJECTED_FIRST_2000={sorted(rejected)}")
print(f"HELD_MISSING={sorted(held_missing)} HELD_REJECTED_FIRST_2000={sorted(held_rejected)}")
print(f"KNOWLEDGE_TOKEN_PREFIX_MISMATCHES={prefix_mismatches}")
' /home/vgpnk/Projects/shokunin/revenger-shokunin
```

## Complete output

```text
ROOT=/home/vgpnk/Projects/shokunin/revenger-shokunin
COLUMN=line.split("|")[3]; REGEX=knowledge/[\w.-]+\.md
ROW C01 status=held matches=1 backed=1 strict=1
  knowledge/pe-resource-directory-layout.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C02 status=partial matches=2 backed=0 strict=0
  knowledge/seed.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
  knowledge/2026-10-12-rea-readiness-checklist.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C03 status=frontier matches=0 backed=0 strict=0
ROW C04 status=held matches=1 backed=1 strict=1
  knowledge/round-62-commonjs-require-name-evidence.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C05 status=frontier matches=0 backed=0 strict=0
ROW C06 status=held matches=1 backed=1 strict=1
  knowledge/round-63-zip-central-directory-evidence.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C07 status=frontier matches=0 backed=0 strict=0
ROW C08 status=frontier matches=0 backed=0 strict=0
ROW C09 status=held matches=1 backed=1 strict=1
  knowledge/round-62-evm-dispatch-byte-evidence.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C10 status=partial matches=1 backed=0 strict=0
  knowledge/seed.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C11 status=held matches=1 backed=1 strict=1
  knowledge/utf16-unpaired-surrogates-in-resource-names.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C12 status=held matches=2 backed=1 strict=1
  knowledge/tool-validation-by-function-and-version.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
  knowledge/seed.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C13 status=held matches=2 backed=1 strict=1
  knowledge/digest-scope-versus-provenance.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
  knowledge/seed.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
ROW C14 status=partial matches=1 backed=0 strict=0
  knowledge/2026-10-12-rea-readiness-checklist.md is_file=1 rejected_first_2000=0 rejected_anywhere=0
EXCLUDED_WORK_EVIDENCE C04 knowledge/commonjs-destructured-require-edges.md is_file=1 rejected_first_2000=1 rejected_anywhere=1
EXCLUDED_WORK_EVIDENCE C09 knowledge/evm-saved-interface-candidates.md is_file=1 rejected_first_2000=1 rejected_anywhere=1
ROWS=14 KNOWLEDGE_OCCURRENCES=13 UNIQUE_PATHS=9
K_HELD=7/14
K_HELD_BACKED=7/14
K_HELD_BACKED_STRICT=7/14
MISSING=[] REJECTED_FIRST_2000=[]
HELD_MISSING=[] HELD_REJECTED_FIRST_2000=[]
KNOWLEDGE_TOKEN_PREFIX_MISMATCHES=[]
EXIT=0
```

Verification exercised: only the read-only bounded sweep above, exit 0. The full counter and verifier self-tests were not run. No corpus/fixture/live bytes, registry/spec files, Git/JJ state, or index were changed. No scratch artifacts or tool installs.

Report: .ufo/waves/round-64/R64LabKregex.md
