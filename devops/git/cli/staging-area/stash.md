# stash

- With stash you can save your WIP in a `temporary commit` and recover it later
- Stash is saved as a commit stored at `.git/refs/stash`

```shell
# Save WIP (push to the stash list)
# the last stash is stored in refs/stash
git stash push
git stash # same as git stash push

git stash -u # --include-untracked
git stash -m "message" # --message ()"WIP on branchname ..." by default)
git stash push -m bdc-timeout path/to/file # stash a single file

# List all Stash
git stash list

# Recover WIP
git stash pop
git stash pop

# References
git stash save "coolstuff" # reference the stash with a name
git stash apply "0" # pop it from a specific reference (the index is found on stash list)
```
