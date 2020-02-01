## Diffs

Difference between last (current) commit and commit before it:

    git diff HEAD^ HEAD
    git show

There are two diffs:

    git diff
    git diff --cached

The first is between working tree and HEAD. The second is between staging and HEAD.

## Augmenting commits

The `git commit --amend` command is a convenient way to fix up the most recent commit. It lets you combine staged changes with the previous commit instead of committing it as an entirely new snapshot. It can also be used to simply edit the previous commit message without changing its snapshot.

Squash last 3 commits together (https://stackoverflow.com/a/5201642)

    git reset --soft HEAD~3 && git commit

You should have to write the new commit message from scratch.

## Branches

Create new branch from current branch and switch to it immediately:

    git checkout -b branch-name

The first time pushing that branch:

    git push -u origin branch-name

Delete local branch:

    git branch -d branch-name

Delete remote branch:

    git push origin --delete branch-name

## Merges

Merge branch B into branch A:

    git checkout B
    git pull
    git checkout A
    git merge B

Merge with explicit commit without fast-forwarding:

    git merge develop --no-ff

Merge without committing:

    git merge develop --no-commit --no-ff

## Resets

Resets the index and working tree. Any changes to tracked files in the working tree since <commit> are discarded:

    git reset --hard HEAD

Remove a file from a Git repository without deleting it from the local filesystem:

    git rm --cached settings.py

For a directory:

    git rm --cached -r logs

Extract file from staged state (opposite of `git add`):

    git reset filename.py

Completely disregard last commit and roll back to the previous one:

    git reset --hard HEAD~

The last commit will be completely removed from history.

The opposite of `git add <file>` is `git reset <file>`. So `git reset` removes a file from the staging area.
