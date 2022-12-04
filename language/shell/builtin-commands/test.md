# test

- Test a command output
- `test` is used on "if" and "while" statements when `[]` is used

```shell
test 2 -gt 1
```

## -eq

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

## -ne

```shell
# -ne
foo=10
if [ $foo -ne 5 ]; then
  echo "Is not equal"
else
  echo "Is equal"
fi
```

## -gt

```shell
# -gt
foo=10
if [ $foo -gt 5 ]; then
  echo "Is greater"
else
  echo "Is not greater"
fi
```

## -lt

```shell
foo=10
if [ $foo -lt 5 ]; then
  echo "Is lesser"
else
  echo "Is not lesser"
fi
```

## -f

```shell
# -f
foo=~/file.txt
if [ -f $foo ]; then
  echo "File exists"
else
  echo "File does not exist"
fi
```

## -d

```shell
# -d
foo=~/.config
if [ -d $foo ]; then
  echo "Directory exists"
else
  echo "Directory does not exist"
fi
```

## -e

```shell
# -e
foo=~/file.txt
if [ -e $foo ]; then
  echo "Exists"
else
  echo "Does not exist"
fi
```

## ! (not)

```shell
# !
# negates the condition (not)
foo=10
if [ ! $foo -eq 5 ]; then
  echo "Is not equal"
else
  echo "Is equal"
fi
```
