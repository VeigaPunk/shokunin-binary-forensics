# D1 false-sentence fixture (round-69 C2 red-before; the Q15 defect class)

This file is the committed receipt of the defect class criterion Q15 exists to
catch: a tree-identity sentence that is not re-derived with the command that
names it. The round-68 `reports/round-68/measure-after.log:102` sentence states
the `1c34603` `corpus/` tree is "byte-identical to the earlier measured 14774a2c
tree — 51894d15… — and to the receipt commit's"; the naming command contradicts it:
`git rev-parse 1c34603:corpus` prints `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`
(and `git rev-parse dddf147:corpus` prints `51894d153a6e69487da2a273680d014abd240f61`).
Normalized to the checker's pair syntax:

tree-identity false-sentence: `1c34603:corpus` = `51894d153a6e69487da2a273680d014abd240f61`
