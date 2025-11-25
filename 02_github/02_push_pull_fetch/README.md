# GitHub: Push, Pull, and Fetch

## Goal
Understand how local changes are sent to GitHub (push), how remote updates are retrieved (pull), and how to inspect remote updates without applying them (fetch).

## What Was Done
- Created a demo file and pushed the first commit to GitHub.
- Made changes directly on GitHub and pulled them into the local repository.
- Used `git fetch` to update remote tracking information without modifying local files.
- Compared local and remote branches using `git diff main origin/main`.
- Manually merged remote updates into the local branch.

## Key Concepts
- **Push** sends local commits to GitHub.
- **Pull** = fetch + merge, applies remote commits to the local branch.
- **Fetch** updates remote tracking branches without affecting the working tree.
- **origin/main** can advance ahead of `main`, and manual merging is possible.