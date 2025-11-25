"""
Task: Push / Pull / Fetch mechanics in GitHub

Steps:

1. Create a new folder '02_push_pull_fetch' with files:
   - task.py
   - README.md
   - demo.txt

2. Add initial content to demo.txt and commit the change.
   Commit message:
   "Add first push test in demo.txt"

3. Push the commit to GitHub using:
   git push

4. Modify demo.txt directly on GitHub by adding a new line.
   Confirm that the local file remains unchanged.

5. Pull the change from GitHub using:
   git pull
   Verify that demo.txt is updated locally.

6. Modify demo.txt on GitHub again, adding another new line.
   Run:
   git fetch
   Confirm that:
   - local main does not change
   - origin/main moves forward

7. Compare local and remote using:
   git diff main origin/main

8. Merge the remote updates manually:
   git merge origin/main

Expected result:
Understanding of the difference between push, pull, and fetch, and how local and remote branches diverge and synchronize.
"""