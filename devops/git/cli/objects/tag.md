# tag

```sh
# List all tags
git tag
ls .git/refs/tags
```

## Create

```sh
# Create Lightweight tag
git tag v1.0.0

# Create Annotated tags
git tag -a "v1.0.0" -m "Tag message"
git tag -a "36+202103191200-master-36" -m "36+202103191200-master-36" # 36 is the minor version
```

- Change package version in jenkins
  - Change the version in package.json to (desired version-1)
  - Annotate the commit with the (desired version-1)
  - Push tags (`git push --tags`)
  - Push package.json (`git add -A && git commit -m "update version" && git push`)
  - Jenkins will build the package with the desired version

## Show

```sh
# Show tag details (Only for annotated tags)
git tag -v v1.0.0
```

## Push Tags

```sh
# Push all tags to remote (by default it's not pushed)
git push --tags # Only tags are pushes. No commits at all

# Push specific tag
git push `remote` `tag`
git push origin v1.0.1
```
