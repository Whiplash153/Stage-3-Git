# Task: Remote branches practice

# 1. Create a new local branch and switch to it.
#    Command used:
#    git switch -c feature/remote-test

# 2. Add new files inside the task directory and commit them.
#    Commands:
#    git add .
#    git commit -m "Add initial change in feature/remote-test"

# 3. Push the new branch to GitHub with upstream tracking.
#    Command:
#    git push -u origin feature/remote-test

# 4. Verify local and remote branches.
#    Commands:
#    git branch -a
#    git branch -r

# 5. Merge the feature branch back into main.
#    Commands:
#    git switch main
#    git merge feature/remote-test
#    git push

# Result:
# The new folder and files from the feature branch appear in main
# both locally and on GitHub.