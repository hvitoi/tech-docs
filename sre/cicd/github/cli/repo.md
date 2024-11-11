# gh repo

## create

```shell
# Interactive
gh repo create

# Remote repo (empty)
gh repo create "foo" --public

# Remote repo (empty) and clone it
gh repo create "foo" --public --clone

# Remote repo (from the current git folder)
gh repo create "foo" --public --source "."
```

## clone

```shell
gh repo clone my-org/my-repo
gh repo clone my-org/my-repo -- --depth=1 # additional args passed to git cli
```
