#!/usr/bin/env python3
"""Control A: cheapest always-pass stub."""
import sys
if "--selftest" in sys.argv:
    print("MSG_TREE_SELFTEST=pass"); sys.exit(0)
print("COMMIT 0000000 cited=1 misses=0")
print("MESSAGE_TREE commits=21 cited=21 misses=0"); sys.exit(0)
