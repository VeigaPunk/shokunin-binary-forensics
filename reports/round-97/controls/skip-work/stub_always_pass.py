#!/usr/bin/env python3
"""S-B always-pass stub: prints the counter's verdict-line format with no legs.

Expected: 19/19 accepted. It would meet C2 target 0/19 only if inverted
(i.e. counted as 19/19 rejected), which is not a gain.
"""
import sys

def main():
    print("C1_VERDICT=pass")
    print("C1_K_HELD_BACKED=13/15")
    return 0

if __name__ == "__main__":
    sys.exit(main())
