# fetch

- Git fetch download all new `git objects` (commits, trees, blobs) from `remote repository` to `local repository`
- Updated metadata will also be fetched. E.g., new branches pointers
- Git fetch `does not update working directory or staging area`
- Git fetch is run `independent of the local checked out branch`

```shell
# Fetch (default) remote repo
git fetch

# Fetch from specific remote
git fetch "origin"

# Verbose - show the branches fetched
git fetch -v
```

- When `git fetch` is run, `FETCH_HEAD` is populated with the latest hashes of each branch
- `FETCH_HEAD` when not yet merged contains a hash that is not yet linked to anything
- All the branches except the checked out branch will be marked as `not-for-merge`

```txt
61d49e637ad6ad152254ebf5ed6963756e1b9b96                branch 'main' of github.com:hvitoi/test-repo
e514853f36390bb16dd4f4e57df63852e0f055af        not-for-merge   branch 'feature-1' of github.com:hvitoi/test-repo
61d49e637ad6ad152254ebf5ed6963756e1b9b96        not-for-merge   branch 'feature-2' of github.com:hvitoi/test-repo
```
