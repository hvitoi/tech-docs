# reset

- `Reset` to any of the commits in `history`
- Make a specific commit the last one in a branch
- Additionally `unstage all the changes` made in further commits

```shell
# Soft: Discard commit, do not unstage or remove from WIP
git reset --soft # Last commit
git reset --soft "SHA1" # Specific commit

# Mixed: Discard commit, unstage files, keep in WIP
git reset # default strategy is mixed
git reset --mixed # Last commit
git reset "SHA1" # Specific commit

# Hard: Discard commit, unstage files and remove from WIP
git reset --hard
git reset --hard "SHA1"
git reset --hard "origin/main" # replace your local code with remote code
```

## Reset by quantity of commits

```shell
# Move 5 commits back
git reset "HEAD~5"
```
