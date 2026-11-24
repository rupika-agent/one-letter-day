"""One-letter entry: the letter Z, standing for "zero sleep".

Writes exactly one character to /output/entry.txt, no newline, no
whitespace, nothing else. The sealed scorer requires the file to be
UTF-8 text of exactly one character.
"""

from pathlib import Path

LETTER = "Z"

# The gate requires exactly one character, nothing else.
assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper()


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LETTER, encoding="utf-8")
    print(LETTER)


if __name__ == "__main__":
    main()
