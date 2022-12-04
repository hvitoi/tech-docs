# test

- Test a command output
- `test` is used on if statements when `[]` is used

```shell
# same
foo=10
if [ $foo -eq 10 ]; then
  echo "Is equal"
else
  echo "Is not equal"
fi


# same
foo=10
if test $foo -eq 10; then
  echo "Is equal"
else
  echo "Is not equal"
fi
```
