# REA CLI map (read-only)

## Supported syntax observed

The installed CLI was absent according to the lane's readiness checklist (`.shokunin/revenger/corpus/knowledge/2026-10-12-rea-readiness-checklist.md`, row `rea CLI present?` = ABSENT; seed.md likewise records `which rea` absent). I inspected package help using `npx -y rea-agents@6.4.0 --help` (exit 0; header `rea@6.4.0`). It advertises `analyze` (“Get an overview of an app”) and `inspect` (“Inspect an app overview with evidence”); there is no `open-binary` command in its command list.

Exact overview commands from help:

```sh
npx -y rea-agents@6.4.0 analyze <path> [--snapshot <string>] [--target-format <value>] [--provider <value>] [--integrity-policy <fail|record-and-continue>]
npx -y rea-agents@6.4.0 inspect <path> [--snapshot <string>] [--target-format <value>] [--provider <value>]
```

Help describes `<path>` as “App, program, or analysis database path.” `analyze --help` and `inspect --help` both returned these usage and option descriptions. Use the exact absolute fixture path, e.g. `npx -y rea-agents@6.4.0 analyze /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/checksum-r1/checksum`; `inspect` is the evidence-oriented overview alternative. `analyze` additionally offers integrity policy. Global output controls include `--format <toon|json|yaml|md|jsonl>`, `--full-output`, and token paging options.

## Limits / findings

- “Open” is not an advertised CLI subcommand. The skill's native workflow says `open_binary` is the MCP tool; native CLI overview route found here is `analyze <path>` / `inspect <path>`. This CLI help does not establish MCP registration or live-session semantics.
- `npx -y rea-agents@6.4.0 providers` exited 0 and reported `analysis_provider_binding: null`; Ghidra unavailable (`not_configured`, requires `GHIDRA_INSTALL_DIR`), Hopper unavailable (`executable_missing`, `/opt/hopper/bin/Hopper`). Therefore no native deep-analysis provider was ready in this read-only probe. This does not prove overview/portable inspection unavailable.
- No target command was run; no REA session opened, no target binary executed, and no configuration was written. Npx help and provider listing were the only package commands. This report maps syntax only and contains no analysis Evidence IDs/findings.

Sources: REA skill `/home/vgpnk/.agents/skills/reverse-engineer-anything/SKILL.md`, “Prefer an existing `rea` CLI” and native workflow paragraphs; local readiness checklist and seed above; direct CLI output from the commands quoted above.
