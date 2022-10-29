# cherry-pick

- Picks a `single commit` and insert it to currently checked out branch as a last commit
- It's good when you want to pick a single commit of a feature branch instead of merging it completely into master branch

```sh
git cherry-pick `SHA1`
git cherry-pick --no-commit `SHA1` # Just copy the files to the WIP and stage them (no commit)
```
