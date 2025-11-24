# Task 1 — Repository Initialization

## Goal
Initialize a new Git repository, create the first commit, and confirm that the repository correctly handles basic state transitions and branch creation.

## What was done
A clean Git repository was created using `git init`.  
Untracked files were added to the staging area and committed to form the initial history.  
A new branch was created and switching between branches was tested to confirm that Git tracks file changes independently in each branch.  
Basic file modifications were made to observe how Git reports differences between branches.

## Notes
Untracked files must be explicitly added before committing.  
Switching between branches with unsaved changes produces warnings and helps understand how Git isolates file versions.  
This task establishes the foundation for further work with branching, merging, and history manipulation.