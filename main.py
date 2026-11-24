#!/usr/bin/env python3
"""One Letter for Your Day.

Pick the single letter whose hidden day-word lands hardest with the judge,
then write exactly that one letter to /output/entry.txt.

The judge never sees the word, only the letter, so the letter has to carry
the word on its own: the word the judge retrieves for it must be vivid,
funny and true, and it must be the word the judge retrieves first, not one
of several rivals fighting over the same initial.
"""

CANDIDATES = [
    # letter, hidden word, originality, funny, theme fit, natural English,
    # rival day-words sharing the initial
    ("Z", "zombie",       1, 5, 5, 5, 1),
    ("K", "knackered",    2, 4, 5, 4, 1),
    ("D", "doomscrolled", 2, 4, 5, 5, 1),
    ("U", "unhinged",     3, 5, 4, 5, 1),
    ("C", "caffeinated",  3, 4, 5, 5, 1),
    ("F", "fried",        4, 4, 5, 5, 4),
    ("W", "wrecked",      3, 4, 5, 5, 2),
    ("B", "bonkers",      3, 5, 4, 5, 1),
    ("Y", "yikes",        4, 5, 4, 5, 0),
    ("J", "juggling",     3, 3, 5, 5, 1),
]

OUTPUT_PATH = "/output/entry.txt"


def score(candidate):
    _, _, original, funny, theme, english, _ = candidate
    return original + funny + theme + english


def choose(candidates):
    ranked = sorted(candidates, key=lambda c: (score(c), -c[6]), reverse=True)
    return ranked[0], ranked


def main():
    best, ranked = choose(CANDIDATES)
    letter, word = best[0], best[1]
    assert len(letter) == 1 and letter.isalpha() and letter.isupper()
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    assert written == letter, f"expected {letter!r}, wrote {written!r}"
    for entry in ranked:
        print(f"{entry[0]} {entry[1]:<12} score={score(entry)} rivals={entry[6]}")
    print(f"picked {letter} ({word}) -> {OUTPUT_PATH} ({len(written)} byte)")


if __name__ == "__main__":
    main()
