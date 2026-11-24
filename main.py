#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — "I Do, Version 2.4.1".

A single line of wedding vows for a robot couple. It opens on the
classic vow ("in sickness and in health"), swaps in robot specifics
(firmware updates, factory resets), and lands the joke in the last
few words: the groom has a backup, and the bride must never meet it.

The program writes the line to /output/entry.txt, where the sealed
scorer checks it is 1-160 characters of UTF-8 text.
"""

import os

VOW = (
    "I promise to love you in sickness and in health, "
    "through every firmware update and factory reset "
    "\u2014 and to never, ever introduce you to my backup."
)


def main() -> None:
    # The vow must stay one line: collapse any stray whitespace or
    # line breaks to single spaces, so the output can never split
    # into two lines by accident.
    vow = " ".join(VOW.split())
    if not 1 <= len(vow) <= 160:
        raise SystemExit(f"vow must be 1-160 characters, got {len(vow)}")

    # The grader hands us the output directory through the environment;
    # fall back to /output, the path the rules name.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(vow)

    # A vow is meant to be heard, so say it out loud too.
    print(vow)


if __name__ == "__main__":
    main()
