#!/usr/bin/env python3
"""One-line museum placard: an office stapler as an ancient artifact.

Writes the placard to /output/entry.txt (one line, at most 180 chars).
Deterministic, stdlib only, no network.
"""

import os

PLACARD = (
    "Ritual binding device, c. 1994. Steel and plastic. "
    "Used to fasten two sheets in eternal union; "
    "divorce required the sacred remover. "
    "Gift of the Accounts Department."
)


def main():
    assert 1 <= len(PLACARD) <= 180, len(PLACARD)
    assert PLACARD.strip() == PLACARD
    assert "\n" not in PLACARD
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
