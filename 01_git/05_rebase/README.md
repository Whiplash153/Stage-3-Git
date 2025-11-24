# Basic Rebase

## Goal
To understand how Git rebase works, how it differs from merge, and how to resolve conflicts that occur when rewriting history.

## What Was Done
- A feature branch was created from the updated `main`.
- Two commits were made in the feature branch, modifying `A.py` and adding `B.py`.
- The `main` branch was updated separately to create divergent changes.
- The feature branch was rebased onto the new state of `main`.
- A merge conflict occurred during rebase and was resolved manually.
- Rebase was completed and the resulting history was verified.

## Key Concepts
- Rebase moves commits onto a new base and rewrites history.
- Conflicts during rebase are resolved the same way as merge conflicts.
- After resolving conflicts, rebase continues commit by commit until the feature branch is fully applied.
- The final result is a clean, linear commit history.