# CLAUDE.md

> ICPC/OI Algorithm Template Collection — competitive programming reference in C++17/20.

## Project overview

A single comprehensive Markdown file (`algorithm-notebook-cn.md`, ~10,700 lines) containing battle-tested C++ implementations of common competitive programming algorithms. All code is self-contained and copy-paste ready for contests.

## Tech stack

- **Language**: C++17/20 (GCC 9+, Clang 10+, MSVC 2019+)
- **Build**: No build system — code blocks are self-contained and compiled individually
- **Format**: Markdown with fenced C++ code blocks

## File structure

```
template/
├── README.md                    # Project introduction and usage guide
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
├── .gitignore                   # C++ build artifacts, IDE files
├── CLAUDE.md                    # This file
└── algorithm-notebook-cn.md     # Main template collection
```

## Code conventions

- **Bilingual comments**: Chinese explanations with English algorithm names
- **Self-contained blocks**: Each fenced code block compiles independently
- **Complexity annotations**: `// O(N log N)` or equivalent on every entry
- **Modern C++**: `auto`, structured bindings, `std::optional`, `using ll = long long`
- **Named constants**: `INF`, `LINF`, `MOD` instead of magic numbers
- **Fast I/O**: `ios::sync_with_stdio(false); cin.tie(nullptr)` in main templates
- **References**: KACTL and jiangly style patterns for core data structures

## Adding new algorithms

1. Place in the appropriate section of `algorithm-notebook-cn.md`
2. Follow the existing template format: `### Name (中文名)` → code block
3. Include time/space complexity
4. Ensure the code compiles with `g++ -std=c++17 -O2 -Wall`
5. Update the Table of Contents

## Common commands

```bash
# Verify a code block compiles
g++ -std=c++17 -O2 -Wall -Wextra -Wpedantic test.cpp -o test && ./test

# Strip leading numbers for extraction
sed 's/^[0-9]\+\t//' algorithm-notebook-cn.md > stripped.md
```
