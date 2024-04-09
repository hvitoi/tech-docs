# od

```shell
# Write string to a hex string in blocks of 8 bytes
od -t x8 -An <<< "abc"

# Write string to a hex string in blocks of 1 byte
od -t x1 -An <<< "abc" | sed 's/[\t ]*//g' | sed 's/[a-z]/\U&/g'
```
