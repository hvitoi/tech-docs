# filter-branch

- Lets you rewrite Git revision history by rewriting the branches

## Completely remove a file

- This command will run the entire history of every branch and tag, changing any commit that involved the file "file.txt", and any commits afterwards.
- Commits that are empty afterwards (because they only changed the Rakefile) are removed entirely (prune-empty).
- Find the file to be deleted with `git rev-list`

```shell
# Remove a file completely from all branches
git filter-branch \
  --force \
  --index-filter "git rm --cached --ignore-unmatch src/credentials.json" \
  --prune-empty \
  --tag-name-filter "cat" \
  -- \
  --all

# Remove a folder completely from all branches
git filter-branch \
  --force \
  --index-filter "git rm --cached --ignore-unmatch -r src/folder" \
  --prune-empty \
  --tag-name-filter "cat" \
  -- \
  --all
```

```shell
# strip out the unwanted dirty data which has been expelled out
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

```shell
# Commit the modified repo
git push --all --force
```
