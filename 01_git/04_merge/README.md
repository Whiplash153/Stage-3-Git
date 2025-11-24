# Merge Conflict Resolution

## Goal
The goal of this task is to learn how Git detects merge conflicts and how to resolve them manually when two branches modify the same file.

## What Was Done
- A separate branch was created from the `main` branch to simulate diverging development.
- Both branches independently modified the same file, ensuring their changes overlapped.
- An attempted merge resulted in a merge conflict.
- The conflicted file was inspected and manually corrected by combining the intended changes.
- The resolution was staged and committed, completing the merge.
- The final merge history was verified using Git log visualization.

## Key Concepts
- Merge conflicts occur when two branches change overlapping parts of a file.
- Git marks the conflicting areas in the file for manual review.
- Conflicts are resolved by editing the file, staging the fix, and committing the merge.