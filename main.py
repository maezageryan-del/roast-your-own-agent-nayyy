#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting our own AI agent (muse) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only. No network, no randomness: two runs produce
byte-identical output.
"""
import os

ROAST = "My agent can't say 'lose', so rank 3,487 of 3,661 is officially 'not yet a win'."

def main():
    if not (1 <= len(ROAST) <= 200):
        raise SystemExit("roast must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
