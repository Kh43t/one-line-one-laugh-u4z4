"""One Line, One Laugh — deterministic one-liner writer.

Writes a single original funny line to /output/entry.txt.
Pure Python standard library, no network, no randomness:
the same line is produced on every run.
"""

import os
import sys

LINE = "My Roomba filed a restraining order after I kept moving the furniture."


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    # Guard: verify what was written, without changing the line.
    # The entry must be exactly one line: no newline, no trailing space.
    with open(path, "rb") as handle:
        raw = handle.read()
    written = raw.decode("utf-8")
    if written != LINE or "\n" in written or written != written.strip():
        print("error: entry.txt does not match the expected line", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 140 or not written.strip():
        print("error: entry line fails the 1-140 character gate", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
