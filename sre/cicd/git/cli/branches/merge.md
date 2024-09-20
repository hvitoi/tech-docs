# merge

- Merge a secondary branch into the current checked out branch
- Git will automatically choose the strategy to merge
  - **fast-forward**
  - **3-way** (recursive)
- For 3-way merge, a new merge commit object is created, which incorporate all the changes made in the secondary branch

```shell
# merge the branch "feature" into the currently checked out branch
git merge "feature"

# Abort a merge (Mostly due to conflict error)
git merge --abort
```

## Merged branches

```shell
## Show merged branches
git branch --merged

## Delete branch after merge
git branch --delete "feature"
git branch -d "feature"
```
