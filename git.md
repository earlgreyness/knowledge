


Merge branch B into branch A.

    git checkout B
    git pull
    git checkout A
    git merge B

Create new branch from current branch and switch to it immediately:

    git checkout -b BRANCH_NAME

The first time pushing that branch:

    git push [-u|--set-upstream] origin BRANCH_NAME

Resets the index and working tree. Any changes to tracked files in the working tree since <commit> are discarded.

    git reset --hard HEAD

Remove a file from a Git repository without deleting it from the local filesystem.

    git rm --cached settings.py

For a directory:

    git rm --cached -r logs

---

The opposite of `git add <file>` is `git reset <file>`. So `git reset` removes a file from the staging area.

---

Difference between last (current) commit and commit before it.

    git diff HEAD^ HEAD
    git show

---

There are two diffs:

    git diff
    git diff --cached

The first is between working tree and HEAD. The second is betwee staging aread and HEAD.

## `git commit --amend`

The `git commit --amend` command is a convenient way to fix up the most recent commit. It lets you combine staged changes with the previous commit instead of committing it as an entirely new snapshot. It can also be used to simply edit the previous commit message without changing its snapshot.

