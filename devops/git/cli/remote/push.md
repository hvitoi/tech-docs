# push

```sh
# Push branch to its corresponding remote branch
git push
git push -v # verbose

# Ignore the new modifications on the remote and force push
git push --force
```

- If the .git folder is deleted on the local machine, the `--force` parameter will wipe completely the repo including the commit history

## Branches

```sh
# Push new branch to remote
git push --set-upstream `remote` `branch` # a upstream branch is created (git branch -vv to see the new tracking branch)
git push -u `remote` `branch` # -u is the same as --set-upstream
# A PR suggestion will appear https://github.com/hvitoi/prs/pull/new/feature-1

# Delete branch from remote
git push `remote` -d `branch`
```

## Tags

```sh
# Push all tags to remote (by default it's not pushed)
git push --tags # Only tags are pushes. No commits at all

# Push specific tag
git push `remote` `tag`
git push origin v1.0.1
```

## Clone Repo

```sh
# Bare clone of the repo to be overwritten
git clone --bare "https://github.com/exampleuser/old-repository.git"
cd "./old-repository"

# Overwrite the old repo with a new one
git push --mirror "https://github.com/exampleuser/new-repository.git"
```
