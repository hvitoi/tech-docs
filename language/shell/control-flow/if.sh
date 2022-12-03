#!/bin/bash

count=100
if [ $count -eq 100 ]; then
  echo Count is 100
else
  echo Count is not 100
fi

if [ -e /home/hvitoi/Documents/error.txt ]; then # -e checks if a file exists
  echo "File exists"
else
  echo "File does not exist"
fi

##
#!/bin/bash
host="192.168.1.1"

ping -c1 $host        # c1 is count. Ping once
if [ $? -eq 0 ]; then # $? exit status of the previous above
  echo $host is OK
else
  echo $host is NOT OK
fi

ping -c1 $host &>/dev/null # /dev/null is a blackhole and the message is not shown
if [ $? -eq 0 ]; then      # $? is the reutrn of the command above
  echo $host is OK
else
  echo $host is NOT OK
fi

# Read the hosts from a file
hosts=$(cat /home/hvitoi/Documents/my-hosts)
for ip in $hosts; do       # or $(cat /home/hvitoi/Documents/my-hosts)
  ping -c1 $ip &>/dev/null # /dev/null is a blackhole and the message is not shown
  if [ $? -eq 0 ]; then    # $? is the reutrn of the command above
    echo $ip is OK
  else
    echo $ip is NOT OK
  fi
done
