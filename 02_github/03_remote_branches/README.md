# Remote Branches Practice

## Goal
Understand how local and remote branches work, how to publish new branches to GitHub, and how to merge them back into the main branch.

## What was done
- Created a new local feature branch using `git switch -c`.
- Added new files inside the task directory and committed them.
- Pushed the branch to GitHub with upstream tracking (`git push -u origin`).
- Reviewed local and remote branches using `git branch -a` and `git branch -r`.
- Merged the feature branch into `main` through a fast-forward merge.
- Updated the remote `main` branch with `git push`.

## Key concepts
- A remote branch (`origin/<name>`) is a pointer on GitHub.
- A local branch and its remote counterpart are separate until tracking is set.
- Switching between branches changes the visible working files.
- Merging integrates work from one branch into another.