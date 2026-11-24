"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt and prints it.
The competition gate requires 1 character of UTF-8 text, nothing else:
no word, no explanation, no punctuation, no trailing newline.
"""

import os

ENTRY = "A"  # A = coffee


def main() -> None:
    # The gate is strict: exactly 1 character, no newline, no whitespace.
    assert len(ENTRY) == 1 and ENTRY in ("A", "B"), "entry must be one letter"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "entry.txt must hold exactly the entry"
    print(ENTRY)


if __name__ == "__main__":
    main()
