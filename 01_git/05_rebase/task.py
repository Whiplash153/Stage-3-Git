"""
Task: Basic Git Rebase Practice

Steps:

1. Start from the main branch and create a clean base commit in A.py.
2. Create a new branch 'rebase/feature' from main.
3. Modify A.py in 'rebase/feature' and commit the change.
4. Add a new file B.py, commit it as the second feature change.
5. Switch back to main and modify A.py in a different way to create divergence.
6. Commit the updated A.py in main.
7. Switch back to 'rebase/feature' and run: git rebase main
8. Git reports a conflict in A.py — resolve it manually by editing the file.
9. Stage the resolved file using git add.
10. Continue the rebase using git rebase --continue.
11. Verify the final linear history using git log --oneline --graph.
"""