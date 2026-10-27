PASS — APPNOTE re-opened; live bytes exactly match the committed snapshot.

- Access: 2026-10-27T15:21:46Z; fetched S032/S034 registered URL `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT`.
- Command: `curl -L --fail --silent --show-error 'https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT' -o /fast/scratch/hyaku/revenger-r71/R71W1OpenS032/live.txt && sha256sum /fast/scratch/hyaku/revenger-r71/R71W1OpenS032/live.txt /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/snapshots/APPNOTE.TXT && wc -c ...`
- Actual comparison: both SHA-256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`; both 174585 bytes. Snapshot comparison is exact at byte level.
- Command: `grep` pattern `4\.3\.(7|12|16)` on downloaded `live.txt`.
- Located headings (live file line numbers): §4.3.7 line 387 (`Local file header:`); §4.3.12 line 511 (`Central directory structure:`); §4.3.16 line 632 (`End of central directory record:`).
- Quote (13 words): “end of central dir signature 4 bytes (0x06054b50)” — §4.3.16, line 634. Additional located quote (10 words): “local file header signature 4 bytes (0x04034b50)” — §4.3.7, line 389.
- Evidence commands were exercised successfully; findings concern this exact fetched URL response and the named committed snapshot only.
