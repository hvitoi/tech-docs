#!/bin/bash
count=0
num=10

while [ $count -lt 10 ]; do # less than
  echo $num seconds left to stop this process
  sleep 1
  num=$(expr $num - 1) # mathematical expression
  count=$(expr $count + 1)
done

echo $1 process is stopped # $1 is the process id

while true; do
  read -p "Do you wish to drink a beer?" yn
  case $yn in
  [Yy]*) break ;;
  [Nn]*) exit ;;
  *) echo "Please answer yes or no." ;;
  esac
done
