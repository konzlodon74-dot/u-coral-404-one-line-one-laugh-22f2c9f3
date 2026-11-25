"""One-line laugh entry for u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single original funny line (at most 200 characters) to
/output/entry.txt with no trailing newline.
"""

import os

LINE = "I asked my agent to write me one funny line. It opened a ticket, escalated it to itself, and closed it as 'working as intended.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
