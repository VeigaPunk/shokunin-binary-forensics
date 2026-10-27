PASS — isolated vote-parser probes killed all tested invalid mutations; exact valid sets scored 16/16.

Counter source: `reports/round-71/measure.py`, imported once for all probes. Initial on-disk SHA-256 observed before probe: `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` (A2 frozen hash). During the probe the counter file changed concurrently; final on-disk SHA-256: `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2`. The imported parser was the A2 bytes; no source mutation was performed by this seat. The four real vote files did not yet exist, so fixtures were synthesized from `EXPECTED_VOTES` in isolated scratch. Detector was `measure.q_votes(TREE)` (the exact counter helper), not the full counter CLI.

Outputs (`q_votes`, scratch fixture directory SHA-256):
- Pristine four-seat PASS set: `16/16`, `8cf6eadecf6494a798c9752934f3f9e419210258ea479d705d22224c56086a9d`.
- All-n/a exact set: `16/16`, `f5cb02f51fc63163100a01cccdcd8bfd044bd2de69a044023eeeba8a59f4a654`.
- FAIL decision: `0/16`, `8136acbd1ca83b664e4a3af62e6487caf9789ab4d896253189613f32438733ac` (counter contract rejects FAIL; frozen C1 predicate requires PASS/n-a and no FAIL).
- Duplicate top-level `seat` key: `0/16`, `d8076117c2c59bf6721d9bb8841c1c5e32cb031c2281310cc30f6b5a78e610b0`.
- Duplicate Q key: `0/16`, `bd01bcfa3652012c7ce73b1d2bb1d7224634fb6a4f255cd8aba3748e4f96bb43`.
- Non-object root `[1,2]`: `0/16`, `c31af33c94c0018857274044bd3d26e18d33b5f3e5b542d606298009efdf8bfb`.
- Wrong stem/extra JSON file: `0/16`, `75b745857a1c1689b47ccce9aa7cb74b776d76b48da8e3b9f4e48b1cb08407d9`.
- Missing Q: `0/16`, `fa101485fc3624d576c8ec113fe075b2afd55a5924d2c6d45043a8db1ae93f3d`.
- Duplicate seat/Q via second seat file: `0/16`, `bdf160679cd01e83275bb8361cf3bf95a44ae442114605f78c6a996ec23374cc`.
- Case-variant `N/A`: `0/16`, `64e2f59a126612510bd9c5cc37e3279b125629d2df22f437140b4bcc84a69a6b`.
- Lowercase `pass`: `0/16`, `32fb68fb587ac30257636cfa1ad5ab4b0b4c717bb308b32fea5bf18fcb2d8f3d`.
- Malformed JSON: `0/16`, `228b3bcd9b8de652b9211616a6a53d878dee8744ebfada8229e1b24bada912dc`.
- Restored pristine fixture bytes: `16/16`, SHA-256 exactly restored to `8cf6eadecf6494a798c9752934f3f9e419210258ea479d705d22224c56086a9d`.

Verdict: all invalid probes killed; valid PASS and n/a controls survive as required. Restoration evidence is identical pristine/restored aggregate fixture hash and restored 16/16 result. Scratch `/fast/scratch/hyaku/revenger-r71/R71W2VoteMutants/` was removed. No vote files or source bytes were written by this seat. Note: exact assignment text lists `FAIL` as a mutation, but the frozen A2/C1 counter predicate explicitly rejects FAIL; observed behavior matches that predicate.