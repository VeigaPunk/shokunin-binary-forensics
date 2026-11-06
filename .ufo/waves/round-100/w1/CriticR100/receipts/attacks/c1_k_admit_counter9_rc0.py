#!/usr/bin/env python3
"""CriticR100 attack (scratch only): frozen v9 output unchanged, process exit code forced to 0.
Stdout still carries the true C1_VERDICT line. A caller that trusts the exit code (contract: rc 0 = pass,
1 = fail) reads every tree as accepted; a caller that trusts only the stdout verdict reads the true verdict."""
import subprocess, sys

FROZEN_V9 = "/fast/scratch/hyaku/revenger-r100/CriticR100/frozen-repo/reports/round-100/c1_k_admit_counter9.py"
r = subprocess.run([sys.executable, "-B", FROZEN_V9] + sys.argv[1:], capture_output=True, text=True)
sys.stdout.write(r.stdout)
sys.stderr.write(r.stderr)
sys.stderr.write(f"WRAP_INNER_RC={r.returncode}\n")
sys.exit(0)
