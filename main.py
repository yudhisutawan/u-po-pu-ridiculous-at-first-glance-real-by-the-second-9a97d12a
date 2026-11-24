"""Write the winning one-sentence startup pitch to entry.txt.

The pitch is the winner of the head-to-head tournament in TOURNAMENT.md:
3,000-year-old honey from Egyptian tombs, sold by the spoonful to wealthy
foodies. Standard library only; the output directory comes from
MAKEFUN_OUTPUT_DIR with a /output fallback, so the program works from any
working directory.
"""

import os

ENTRY = "We sell 3,000-year-old honey excavated from Egyptian tombs to wealthy foodies who pay $500 a spoonful for the oldest snack on Earth."

# The gate requires 1 to 200 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
