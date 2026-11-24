#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
would actually sell to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "We rent professional mourners to cry at your funeral so the room "
    "thinks you were loved, because people already pre-pay $9,000 funerals "
    "and a $2,000 crowd is the cheapest legacy upgrade there is."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
