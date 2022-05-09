# merge

```shell
## Merge secondary branch into current branch
# Git will automatically choose the strategy to merge: fast-forward or 3-way (recursive)
# For 3-way merge, a new merge commit object is created, which incorporate all the changes made in the secondary branch
git merge `secondary-branch`

# Abort a merge (Mostly due to conflict error)
git merge --abort
```

## Merged branches

```shell
## Show merged branches
git branch --merged

## Delete branch after merge
git branch -d `secondary-branch`
git branch --delete `secondary-branch`
```
