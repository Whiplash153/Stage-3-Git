"""
Task: Gitignore practice

Steps:

1. Create a new folder '06_gitignore' and prepare three test files:
   - debug.log
   - temp.tmp
   - notes.txt

2. Create a .gitignore file inside the folder.

3. Add ignore rules:
   *.log
   *.tmp
   notes.txt

4. Run `git status` to confirm that ignored files are not added to tracking.

5. Verify that Git shows the folder as untracked, but does not list ignored files individually.

6. Stage and commit only the necessary files:
   - .gitignore
   - task.py
   - README.md

7. Confirm that ignored files did not enter the repository.
"""