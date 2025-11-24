"""
Task: Mini Git project with feature branches

Steps:

1. Create a new folder '07_project_demo' with structure:
   - task.py
   - README.md
   - src/calculator.py

2. Initialize the project by creating the base function add(a, b) in calculator.py.
   Commit this as:
   "Init calculator project: add() function added"

3. Create a new feature branch 'feature/subtraction'.
   Add a subtract(a, b) function.
   Commit as:
   "Feature: add subtract() function"

4. Switch to main and merge the feature/subtraction branch.
   Use fast-forward merge.
   Delete the merged branch.

5. Create a second feature branch 'feature/multiply'.
   Add a multiply(a, b) function.
   Commit as:
   "Feature: add multiply() function"

6. Switch to main and merge feature/multiply.
   Use fast-forward merge.
   Delete the merged branch.

7. Verify the final linear history using:
   git log --oneline --graph --decorate

Expected result:
A clean project structure with three mathematical operations and a linear Git history created through feature branches.
"""