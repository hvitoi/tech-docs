# ls-tree

- Lists the contents of the git repository in the current commit

```sh
git ls-tree "main"
git ls-tree "main" -r # recursive

# Find the 10 biggest files in the HEAD commit
git ls-tree -r -t -l --full-name "HEAD" \
  | sort -n -k "4" \
  | tail -n "10"
```
