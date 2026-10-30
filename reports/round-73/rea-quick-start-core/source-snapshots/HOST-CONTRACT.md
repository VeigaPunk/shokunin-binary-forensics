# Host contract — REA on this machine

> Durable file. `rea-agents setup --skill` regenerates `SKILL.md` and the
> package's own `references/*.md`, but it does **not** delete this file or
> `references/cli-command-map.md`. If `SKILL.md` ever loses its CLI-first
> section, re-apply it with `~/.config/rea/apply-cli-contract.sh`.

## The rule

**REA runs CLI-first on this host. The MCP server is off, deliberately.**

- The `rea` plugin is disabled in the MiniMax Code runtime:
  `mcode plugin disable rea@official`. It was disabled so that REA does not
  connect on every session spawn.
- A session therefore starts with **zero REA MCP tools**. That is the intended
  state, not a broken installation.
- When the user invokes this skill, work through the CLI:
  `npx -y rea-agents@6.7.0 <command> [args] --json`
  (or an installed `rea` binary if one is on PATH).

## Do not

- Do **not** run `rea-agents setup --client <client>` to restore MCP
  registration. That re-enables REA on every session spawn.
- Do **not** run `mcode plugin enable rea@official`.
- Do **not** treat absent MCP tools as a fault to diagnose, and do not spend
  turns proving they are absent.

## Do

- Map MCP tool names to CLI commands (see `references/cli-command-map.md`).
- Read `npx -y rea-agents@6.7.0 --llms` for the live authoritative command
  list and `npx -y rea-agents@6.7.0 <command> --schema` for one command's
  arguments.
- If the user **explicitly** asks for the REA MCP server, tell them it will
  load on every session spawn, and only then follow
  `references/connection-and-recovery.md`.

## State as of this writing

- REA release: `rea-agents@6.7.0`, skill v42, 207 tools.
- Standalone skill installed at `~/.agents/skills/reverse-engineer-anything`
  (also `~/.zcode/skills/...` and the dbzmon project copy).
- `rea@official` plugin: **disabled**.

## Expected `doctor` output on this host

`rea-agents doctor --json` reports these on this machine. They are expected,
not drift to fix:

| Check | State | Why |
|---|---|---|
| `skill:identity` | `stale` / `config_drift` | **Intentional.** The identity digest is the sha256 of `SKILL.md`, and this host customizes `SKILL.md`. Pristine 6.7.0 digest is `fbcd39d6abe803cf…`; the patched file is `056dee0476d1cac5…`. `skill.installed_version` is still `42` and `installed_tool_count` is still `207`, so the skill is the right version. **Do not run `rea setup` to "fix" this — that would revert the CLI-first section.** Re-apply with `~/.config/rea/apply-cli-contract.sh` instead. |
| `registration:*` for `claude_code`, `copilot_cli`, `cursor`, `hermes`, `kimi`, `opencode`, `pi` | `missing` | Those clients have no REA registration, by operator choice. They are not hosts that need one. |
| `hopper` | `missing_analysis_engine` | Hopper is not installed. REA never installs it. Ghidra 12.1.4 and JADX are present and healthy, so native and Android work are covered without Hopper. |
| `ida-registration` | `not_configured` | No `REA_IDA_MCP_CONFIG`. Set it only if IDA work is actually requested. |
| `kuna-installation` | `not_configured` | No `REA_KUNA_COMMAND`. Same — only if Kuna work is requested. |

`codex`, `devin`, `grok_build`, `omp` and `zcode` registrations report `aligned`
at `rea-agents@6.7.0`. Those remain in place: they are inert unless the
corresponding host is started, and they cost nothing at spawn time.
