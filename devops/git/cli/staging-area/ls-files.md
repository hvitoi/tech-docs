# ls-files

- Show files in the staging area
  1. `Untracked`
  1. `Modified`
  1. `Staged`
  1. `Unmodified`

```sh
# Show filename
git ls-files

# Show filename, permission and hash
git ls-files -s

## No conflict
# 0: file is the same in the repository

## Conflict
# 1: file version that is common for both branches - ancestor commit
# 2: last file version from master branch <<<<<<< HEAD
# 3: last file version from feature branch >>>>>>> feature
# -- As soon as the conflict is solved the file changes to 0
```
