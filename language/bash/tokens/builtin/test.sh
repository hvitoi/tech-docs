# - Test a command output
# - `test` is used on "if" and "while" statements when `[]` is used

test 2 -gt 1

## =
# - String comparison
# - You may also use `==`, but it's not POSIX compliant
# - Always use quotes on variable expansions. E.g.,`"$foo"`. Otherwise empty space will crash the execution

foo='lol'
if [ "$foo" = 'lol' ]; then
  echo "It's lol!"
else
  echo "Is not!"
fi

## -eq
# - Numeric comparison

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

## Test the health of hosts
hosts=$(cat ~/hosts-to-be-tested)
for ip in $hosts; do
  ping -c1 "$ip" &>/dev/null # ping once and do not show the return message
  if [ $? -eq 0 ]; then      # check the return status
    echo "$ip" is OK
  else
    echo "$ip" is NOT OK
  fi
done

## -ne
foo=10
if [ $foo -ne 5 ]; then
  echo "Is not equal"
else
  echo "Is equal"
fi

## -gt
foo=10
if [ $foo -gt 5 ]; then
  echo "Is greater"
else
  echo "Is not greater"
fi

## -ge
foo=10
if [ $foo -ge 5 ]; then
  echo "Is greater or equal"
else
  echo "Is not greater or equal"
fi

## -lt
foo=10
if [ $foo -lt 5 ]; then
  echo "Is lesser"
else
  echo "Is not lesser"
fi

## -le
foo=10
if [ $foo -le 5 ]; then
  echo "Is lesser or equal"
else
  echo "Is not lesser or equal"
fi

## -f
foo=~/file.txt
if [ -f $foo ]; then
  echo "File exists"
else
  echo "File does not exist"
fi

## -s
foo=~/file.txt
if [ -s $foo ]; then
  echo "File exists and has size greater than 0"
else
  echo "File does not exist or it is empty"
fi

## -d
foo=~/.config
if [ -d $foo ]; then
  echo "Directory exists"
else
  echo "Directory does not exist"
fi

## -e
foo=~/file.txt
if [ -e $foo ]; then
  echo "Exists"
else
  echo "Does not exist"
fi

## -n
foo=bar
if [ -n "$foo" ]; then
  echo "var is set"
else
  echo "var is unset"
fi

# same
if [ "$foo" ]; then
  echo "var is set"
else
  echo "var is unset"
fi

## -z
if [ -z ${var+x} ]; then
  echo "var is unset"
else
  echo "var is set to '$var'"
fi

if [ -z "$foo" ]; then
  echo "foo is unset"
else
  echo "foo is set to '$foo'"
fi

## ! (not)

# negates the condition (not)
foo=10
if [ ! $foo -eq 5 ]; then
  echo "Is not equal"
else
  echo "Is equal"
fi
