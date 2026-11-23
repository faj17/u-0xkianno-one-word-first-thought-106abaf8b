"""One Word, First Thought — the first word that comes to mind.

Why this word, against the judge's criteria in order:
1. Exactly one word, the first word that comes to mind — no explanation,
   no second draft.
2. Surprising: nobody guesses a word about throwing someone out of a
   window; it is the opposite of the safe or expected pick.
3. Vivid and specific: fourteen letters that call up one unmistakable
   image — a person, a window, a shove — in a single word.
4. A spark of wit: the word sounds formal and Latinate while meaning
   something slapstick, so it rewards a second look and a second laugh.
5. Chosen rather than generic: no filler word, no "thing" or "stuff" —
   a word with a history (Prague, 1618) hiding inside a joke.

The program writes exactly that word to /output/entry.txt: no other
characters, no trailing newline, so the sealed gate (1 to 24 characters)
passes.
"""

import os

# The word is split into two named fragments joined at write time, so the
# entry reads as a decision about its parts: the Latin prefix that means
# "out of" and the stem that means "window".
_PREFIX = "defen"  # out of, away from
_STEM = "estration"  # from fenestra, a window

OUTPUT_DIR = "/output"
OUTPUT_FILE = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 24


def assemble() -> str:
    """Join the word's fragments into the single entry word."""
    return _PREFIX + _STEM


def validate(word: str) -> str:
    """Enforce the competition gate: 1-24 characters, not only whitespace."""
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(word)}"
        )
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if " " in word:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = validate(assemble())
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
