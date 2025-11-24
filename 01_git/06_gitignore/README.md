# Gitignore Basics

## Goal
To learn how to configure `.gitignore` so that unnecessary or temporary files are excluded from version control.

## What Was Done
- Created test files to simulate typical development “noise”.
- Added ignore patterns to `.gitignore` for log files, temporary files, and specific filenames.
- Verified that ignored files do not appear in Git tracking.
- Ensured the repository stays clean by committing only essential files.

## Key Concepts
- `.gitignore` filters out files that should not be added to the repository.
- Git may still show the directory containing ignored files, but the files themselves remain untracked.
- Once ignored, such files will not enter Git history unless explicitly forced.