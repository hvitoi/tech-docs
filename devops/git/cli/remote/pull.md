# pull

- It's the union of `git fetch` + `git merge`
- To perform git pull, there must be `local tracking branch`
- Git pull updates only a `single local currently checked out branch`

## Step

- Branch types
  - `main` (local)
  - `origin/main` (local)
  - `main` (remote)

1. **git fetch**

   - _main (remote)_ is copied to _origin/main (local)_
   - _main (local)_ is left untouched
   - After fetching, `FETCH_HEAD` is created pointing to origin/main containing hashes of last commits in all tracking branches

1. **git merge**

   - _origin/main (local)_ is merged into _main (local)_
   - The merge (update index + working dir) can be `fast-forward` or `3-way`, alternatively rebase can be specified
   - The merge command is `git merge FETCH_HEAD` or `git rebase FETCH_HEAD`

## Commands

```shell
# Pull changes (fetch and merge) for the current checked out branch (tracked branch)
# The commits will be fetched from all branches, but it will only be merged into the current checked out branch
git pull
git pull -v # verbose

# Pull changes from specific remote and branch
git pull "origin" "main" -v # verbose
```

## Pull strategies

```shell
# git config pull.ff only: fast-forward only
git pull --ff-only

# git config pull.rebase false: merge (the default strategy)
git pull --no-rebase

# git config pull.rebase true: rebase strategy
git pull --rebase

# pull submodules
git pull --recurse-submodules
```
