#!/usr/bin/env python3
"""Extract C++ code blocks from algorithm-notebook-cn.md for syntax verification.

Reads the main template Markdown file and writes each fenced ```cpp block
to a separate .cpp file in the output directory.  Each extracted file is
wrapped with the standard headers and a stub main() so `g++ -fsyntax-only`
can check it.

Usage:
    python3 scripts/extract_code_blocks.py algorithm-notebook-cn.md build/
"""

import re
import sys
from pathlib import Path


def extract_blocks(md_path: Path, out_dir: Path) -> int:
    """Extract ```cpp fenced blocks from *md_path* into *out_dir*.

    Returns the number of blocks written.
    """
    text = md_path.read_text(encoding="utf-8")

    # Match fenced ```cpp ... ``` blocks
    pattern = re.compile(r"```cpp\s*\n(.*?)```", re.DOTALL)
    blocks = pattern.findall(text)

    out_dir.mkdir(parents=True, exist_ok=True)

    header = """\
#include <bits/stdc++.h>
using namespace std;

"""

    count = 0
    for i, body in enumerate(blocks):
        # Skip blocks that look like standalone snippets without a main
        stripped = body.strip()
        if not stripped:
            continue

        fname = out_dir / f"block_{i:04d}.cpp"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(header)
            f.write(stripped)
            f.write("\n")
            # If there's no function definition at all, add a dummy main
            if " main(" not in stripped and "int main" not in stripped:
                f.write("\nint main() { return 0; }\n")

        count += 1

    return count


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.md> <output_dir>", file=sys.stderr)
        sys.exit(1)

    md_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])

    if not md_path.exists():
        print(f"Error: {md_path} not found", file=sys.stderr)
        sys.exit(1)

    n = extract_blocks(md_path, out_dir)
    print(f"Extracted {n} code blocks to {out_dir}/")


if __name__ == "__main__":
    main()
