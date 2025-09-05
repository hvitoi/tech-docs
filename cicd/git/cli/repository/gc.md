# gc

- Garbage collection: Clean unreachable commits
- New pack files with along with index files are created
  - `.git/objects/pack` stores `.idx` and `.pack` files

```shell
# Garbage collection for current git repo
git gc

# Prune
git gc --prune=now --aggressive

# Garbage collection for all existing repos in a directory
find "." \
  -type "d" \
  -name ".git" \
  -exec git --git-dir={} --work-tree=$PWD/{}/.. gc \;
```
