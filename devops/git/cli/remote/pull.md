# pull

- It's the union of `git fetch` + `git merge`
- To perform git pull, there must be `local tracking branch`
- Git pull updates only a `single local currently checked out branch`

- `Steps
  - The first step is fetch (update git repo), which fetches the new commits from remote. After fetching, `FETCH_HEAD` is created containing hashes of last commits in all tracking branches
  - The second step is merge (update index + working dir), which can be `fast-forward` or `3-way`. The command is `git merge FETCH_HEAD`

```shell
# Pull changes (fetch and merge) for the current checked out branch (tracked branch)
# The commits will be fetched from all branches, but it will only be merged into the current checked out branch
git pull
git pull -v # verbose

# Pull changes from specific remote and branch
git pull `remote` `branch`
git pull origin master -v # verbose
```

## Pull strategies

```shell
# git config pull.rebase false`: merge (the default strategy)
git pull --no-rebase
# git config pull.rebase true` rebase
git pull --rebase
# git config pull.ff only`: fast-forward only
git pull --ff-only
```
