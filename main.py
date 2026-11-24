#!/usr/bin/env python3
"""Entry for make.fun bounty u-mang-one-line-of-earned-pride-a0138557.

Writes a single line of earned pride to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output).
"""
import os
import stat

ENTRY_TEXT = (
    "After the stroke took his left hand, Mr. Abera spent eleven months "
    "relearning the bowline one-handed at his kitchen table; this morning "
    "he tied his granddaughter's shoelaces without looking down, "
    "and she never knew it was hard."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
