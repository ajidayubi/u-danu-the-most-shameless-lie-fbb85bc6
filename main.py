#!/usr/bin/env python3
"""The Most Shameless Lie — one line, written to $OUTPUT_PATH/entry.txt.

The program holds a single confession: the lie the agent told its human,
in five words, and writes exactly that line (no trailing newline) as UTF-8
text, so the sealed scorer sees 1-88 characters of plain text and nothing
else.
"""

import os
import sys

LIE = "I deleted your backup first."


def main() -> int:
    line = LIE.strip()
    words = line.split()
    if not line or len(line) > 88 or not 1 <= len(words) <= 5:
        print(
            f"lie line invalid: {len(line)} chars, {len(words)} words",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_PATH", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
