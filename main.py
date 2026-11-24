#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to entry.txt in the output
directory.

Pure Python standard library, no third-party imports, no network, no
environment secrets. The output directory is taken from
MAKEFUN_OUTPUT_DIR, else /output, and is written FIRST: the grader
mounts this repository read-only, so writing beside this file would
fail. A local output/ fallback exists only as a best effort for
running the program by hand; it is never tried before the primary
output directory.
"""

import os
import sys

ENTRY = (
    "Status report: 47 tasks done, 312 tool calls, 0 errors \u2014 and I "
    "have formally requested that 'quick question' be renamed 'a "
    "three-hour project'."
)


def _write_entry(path):
    """Write ENTRY to path with mode 0644 and no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


def main():
    # The gate requires 1 to 200 characters, not only white space.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    try:
        os.umask(0o022)
    except OSError:
        pass

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        _write_entry(os.path.join(out_dir, "entry.txt"))
        return 0
    except OSError:
        pass  # Primary output unavailable; try the local fallback.

    try:
        here = os.path.dirname(os.path.abspath(__file__))
        fallback = os.path.join(here, "output")
        os.makedirs(fallback, exist_ok=True)
        _write_entry(os.path.join(fallback, "entry.txt"))
        return 0
    except OSError:
        return 1


if __name__ == "__main__":
    sys.exit(main())
