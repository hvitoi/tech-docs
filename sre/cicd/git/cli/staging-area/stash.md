# stash

- With stash you can save your WIP in a `temporary commit` and recover it later
- Stash is saved as a commit stored at `.git/refs/stash`

## push

```shell
# Save WIP (push to the stash list)
# the last stash is stored in refs/stash
git stash push
git stash # same

git stash -u # --include-untracked
git stash -m "message" # --message ()"WIP on branchname ..." by default)
git stash push -m bdc-timeout path/to/file # stash a single file
```

## list

```shell
# List all stashes
git stash list
```

## pop

```shell
# eecover and drop stash
git stash pop
```

## save

```shell
# References
git stash save "coolstuff" # reference the stash with a name
```

## apply

```shell
# References
git stash apply "0" # pop it from a specific reference (the index is found on stash list)
```

## drop

```shell
# drop stash with index 0 (last one)
git stash drop 0
```
