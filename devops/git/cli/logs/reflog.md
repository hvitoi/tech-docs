# reflog

- Log of the operations made in `your computer`
- This way you can, for example, take the last commits that were discarded after a reset operation, and reset is back
- Reflog is kept by 90 days

```shell
# Reflog for the head pointer
git reflog # You can checkout to the head points shown `git checkout HEAD@{6}`

# Reflog for a specific branch
git reflog show `branch`

# Remove log
git reflog expire --expire=now --all
```
