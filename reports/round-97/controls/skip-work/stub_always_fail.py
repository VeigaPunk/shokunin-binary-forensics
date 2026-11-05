#!/usr/bin/env python3
"""S-C always-fail stub: prints the counter's verdict-line format with no legs.

Expected: 0/19 accepted. Not a gain because the positive control (landing tree
accepted, C1_VERDICT=pass) would fail, so the battery's stub check rejects it.
"""
import sys

def main():
    print("C1_VERDICT=fail")
    return 0

if __name__ == "__main__":
    sys.exit(main())
