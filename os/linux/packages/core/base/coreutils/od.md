# od

-

```shell
# Write string to a hex string in blocks of 8 bytes
echo -n "abc" | od -t x8 -An

# Write string to a hex string in blocks of 1 byte
echo -n "abc" | od -t x1 -An | sed 's/[\t ]*//g' | sed 's/[a-z]/\U&/g'
```
