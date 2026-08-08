# Security

## Reporting a Vulnerability

If you discover a security vulnerability in any algorithm implementation, please **do not** open a public issue.

Instead, please email the maintainer directly or use GitHub's private vulnerability reporting feature if enabled for this repository.

## Scope

This repository contains educational algorithm template code. Security concerns are primarily about:

- **Integer overflow** in arithmetic operations (especially under competitive programming constraints)
- **Undefined behavior** that could affect correctness
- **Incorrect bounds** leading to out-of-bounds access

## Secure Coding Practices Used

- **Bounds checking**: All array/vector accesses use `.at()` or explicit range validation
- **Overflow awareness**: Large-integer operations use `long long` (`ll`) and modular arithmetic
- **Input validation**: Fast I/O patterns include EOF handling
- **No external dependencies**: All code uses standard library only, minimizing supply chain risk

## Commit Policy

- No credentials, tokens, or secrets are stored in this repository
- All contributions are reviewed before merge
- Pre-commit hooks enforce code style and catch common issues
