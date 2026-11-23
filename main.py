#!/usr/bin/env python3
"""One word, first thought.

Writes the single entry word to /output/entry.txt for make.fun's
"One Word, First Thought" bounty. The word is a concrete noun with a
whole story packed inside it: a wrecked ship on a reef, lost treasure
in the hold, survivors clinging to the shore — one word, one scene.
"""

import os

WORD = "Shipwreck"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The grader reads this file exactly as written, so put in only
    # the word itself: no explanation, no extra whitespace, and no
    # trailing newline after it.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    # The grader collects the output as a different user, so the file
    # itself must be world-readable. Only this file is chmodded here;
    # the /output directory belongs to the grader and is never touched.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
