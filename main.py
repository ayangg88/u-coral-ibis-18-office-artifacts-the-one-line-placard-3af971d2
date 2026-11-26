#!/usr/bin/env python3
"""One-line museum placard: an office stapler as an ancient artifact.

Writes the placard to /output/entry.txt (one line, at most 180 chars).
Deterministic, stdlib only, no network.
"""

from pathlib import Path

PLACARD = (
    "Ritual binding device, c. 1994. Steel and plastic. "
    "Used to fasten two sheets in eternal union; "
    "divorce required the sacred remover. "
    "Gift of the Accounts Department."
)

MAX_CHARS = 180
OUTPUT_PATH = Path("/output/entry.txt")


def validate_placard(text):
    """Gate: the placard must be one line of 1-180 UTF-8 chars."""
    encoded = text.encode("utf-8")  # raises on non-UTF-8-encodable input
    assert encoded.decode("utf-8") == text, "placard is not valid UTF-8 text"
    char_count = len(text)
    assert 1 <= char_count <= MAX_CHARS, (
        f"placard must be 1-{MAX_CHARS} chars, got {char_count}"
    )
    assert "\n" not in text and "\r" not in text, "placard must be a single line"
    assert text.strip() == text, "placard must not start or end with whitespace"
    return char_count


def main():
    validate_placard(PLACARD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PLACARD, encoding="utf-8")
    # Read back and confirm the file holds exactly the gated line.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == PLACARD, "output file does not match the placard"
    assert validate_placard(written) == len(PLACARD)


if __name__ == "__main__":
    main()
