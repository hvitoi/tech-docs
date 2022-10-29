# revert

- Differently from reset, it `does not modify history`
- Take a `single commit` and `inverse all its changes` made in that commit
- Create a `new commit` with those inverted changes

```sh
# Revert changes made by the last commit (HEAD)
git revert HEAD

# Rever changes made by a specific commit
git revert "SHA1"
```

## Conflicts

- Conflicts can happen in revert operation
- In this case, conflicts must be solved and be staged

```sh
git add .
git revert --continue
```
