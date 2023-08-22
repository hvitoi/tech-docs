# "if" statement with any command
foo=htop
if command -v $foo; then
  echo "Command available"
else
  echo "Command not available"
fi

# "if" with [] (uses the"test" command)
# POSIX!

foo=10
if [ $foo -eq 10 ]; then # same as "if test $foo -eq 10; then"
  echo "Is equal"
else
  echo "Is not equal"
fi

# "if" with [[]]
# NON-POSIX! Bash extension

if [[ 10 > 9 ]]; then
  echo "Is greater"
else
  echo "Is not greater"
fi

## inline

if [ ! -z "$foo" ]; then echo "foo"; else echo "bar"; fi
