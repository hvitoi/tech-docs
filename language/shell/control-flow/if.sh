# "if" statement with any command
foo=htop
if command -v $foo; then
  echo "Command available"
else
  echo "Command not available"
fi

# "if" statement with "test" command (when brackets are used)

foo=10
if [ $foo -eq 10 ]; then # same as "if test $foo -eq 10; then"
  echo "Is equal"
else
  echo "Is not equal"
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
