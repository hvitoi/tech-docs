# rev-parse

```shell
# Get the checksum of the last commit
git rev-parse --short=7 HEAD

# Generate version
printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
```
