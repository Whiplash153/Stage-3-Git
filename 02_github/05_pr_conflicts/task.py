# Task: Pull Request conflict resolution

# 1. Added a base version of conflict.txt into main.
#    Commands:
#    git add .
#    git commit -m "Add base version of conflict file"
#    git push

# 2. Created two branches with different edits to the same file.
#    Branch A:
#        git switch -c conflict/b-a
#        edit: "Version A: edited in branch A."
#        git add .
#        git commit -m "Branch A changes"
#        git push -u origin conflict/b-a
#
#    Branch B:
#        git switch main
#        git switch -c conflict/b-b
#        edit: "Version B: edited in branch B."
#        git add .
#        git commit -m "Branch B changes"
#        git push -u origin conflict/b-b

# 3. Created a PR from branch A and merged it into main through GitHub.
#    This updated main with Version A.

# 4. Created a PR from branch B.
#    GitHub detected a merge conflict:
#    "This branch has conflicts that must be resolved."

# 5. Resolved the conflict manually through GitHub’s conflict editor:
#    - opened Resolve conflicts
#    - removed conflict markers
#    - applied final version
#    - clicked Mark as resolved
#    - clicked Commit merge

# 6. Completed the Pull Request via “Merge pull request”.
#    Deleted the branch after merge.

# Result:
# A full GitHub conflict workflow was completed, including creating
# diverging changes, detecting a conflict, resolving it through GitHub,
# and finalizing the merge.