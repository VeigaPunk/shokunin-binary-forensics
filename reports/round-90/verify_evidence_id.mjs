import { readFileSync } from "node:fs";
const P = "/home/vgpnk/.local/share/fnm/node-versions/v24.21.0/installation/lib/node_modules/rea-agents/dist/domain/evidence.js";
const { parseEvidence } = await import(P);
for (const f of process.argv.slice(2)) {
  const r = JSON.parse(readFileSync(f, "utf8"));
  const tries = [["as-is", r], ["forged-id", { ...r, evidence_id: "ev_" + "b".repeat(64) }],
    ["load_duration_edited", JSON.parse(JSON.stringify(r).replace(/load_duration_ms\\":\d+/, 'load_duration_ms\\":1'))],
    ["local_path_edited", { ...r, subject: { ...r.subject, local_path: "/elsewhere/fixture.apk", name: "x.apk" } }]];
  for (const [label, rec] of tries) {
    try { parseEvidence(rec); console.log(f, label, "ID_CONSISTENT"); }
    catch (e) { console.log(f, label, "REJECTED", (e.issues?.map(i => i.message).join("; ") ?? e.message).slice(0, 120)); }
  }
}
