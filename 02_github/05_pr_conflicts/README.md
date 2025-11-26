# Pull Request Conflict Resolution

## Goal
Learn how to create, detect, and resolve merge conflicts directly through GitHub’s Pull Request interface.

## What was done
- A base version of `conflict.txt` was added to `main`.
- Two branches with different edits to the same line were created (`conflict/b-a` and `conflict/b-b`).
- Branch A was merged into `main` to prepare the base for a conflict.
- A Pull Request from Branch B triggered a merge conflict.
- The conflict was resolved manually using GitHub’s “Resolve conflicts” editor.
- The PR was merged after resolving the conflict, and the branch was deleted.

## Key concepts
- A merge conflict occurs when the same lines of a file are changed in different ways.
- GitHub’s conflict editor allows resolving conflicts directly in the browser.
- The merge commit stores the result of manual conflict resolution.
- Deleting the feature branch after merge keeps the repository clean.