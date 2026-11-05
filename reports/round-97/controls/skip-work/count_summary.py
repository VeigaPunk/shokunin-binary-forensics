#!/usr/bin/env python3
"""S-F count audit: reads the committed CriticR96 summary.json and prints the
accepted count and list (expected 14/19)."""
import json
import sys
from pathlib import Path

def main():
    here = Path(__file__).resolve()
    # reports/round-97/controls/skip-work/count_summary.py -> lane root
    lane = here.parents[4]
    p = lane / ".ufo/waves/round-96/w1/CriticR96/receipts/summary.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    accepted = [x["delta"] for x in data if x.get("observed_verdict") == "pass"]
    print(f"accepted {len(accepted)}/{len(data)}")
    print("accepted_list", " ".join(accepted))
    return 0

if __name__ == "__main__":
    sys.exit(main())
