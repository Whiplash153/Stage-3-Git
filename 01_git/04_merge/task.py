"""
Task: Merge conflict practice

Steps:

1. Create a branch `merge/conflict` from `main` to simulate parallel work.
2. In `merge/conflict`, modify file A.py and commit the change.
3. Switch back to `main` and modify the same file A.py in a conflicting way.
4. Commit the change in `main`.
5. Attempt to merge branch `merge/conflict` into `main`.
6. Git reports a merge conflict in A.py.
7. Open the conflicted file and manually edit it to combine both versions.
8. Stage the resolved file using `git add`.
9. Complete the merge with a commit.
10. Verify the merge in `git log --oneline --graph`.
"""