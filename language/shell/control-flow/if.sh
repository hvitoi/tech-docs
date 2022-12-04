# if statement with any command
foo=htop
if command -v $foo; then
  echo "Command available"
else
  echo "Command not available"
fi

## When brackets [] are used, the "test" command is invoked

# -eq
foo=10
if [ $foo -eq 10 ]; then # same as "if test $foo -eq 10; then"
  echo "Is equal"
else
  echo "Is not equal"
fi

# -ne
foo=10
if [ $foo -ne 5 ]; then
  echo "Is not equal"
else
  echo "Is equal"
fi

# -gt
foo=10
if [ $foo -gt 5 ]; then
  echo "Is greater"
else
  echo "Is not greater"
fi

# !
# negates the condition (not)
foo=10
if [ ! $foo -eq 5 ]; then
  echo "Is not equal"
else
  echo "Is equal"
fi

# -f
foo=~/file.txt
if [ -f $foo ]; then
  echo "File exists"
else
  echo "File does not exist"
fi

# -d
foo=~/.config
if [ -d $foo ]; then
  echo "Directory exists"
else
  echo "Directory does not exist"
fi

# -e
foo=~/file.txt
if [ -e $foo ]; then
  echo "Exists"
else
  echo "Does not exist"
fi

## Test the health of hosts
hosts=$(cat ~/hosts-to-be-tested)
for ip in $hosts; do
  ping -c1 $ip &>/dev/null # ping once and do not show the return message
  if [ $? -eq 0 ]; then    # check the return status
    echo $ip is OK
  else
    echo $ip is NOT OK
  fi
done
