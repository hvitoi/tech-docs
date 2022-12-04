# "while" statement with any command

while true; do # infinite loop
  read -p "Do you wish to drink a beer?" yn
  case $yn in
  [Yy]*) break ;;
  [Nn]*) exit ;;
  *) echo "Please answer yes or no." ;;
  esac
done

# "while" statement with "test" command (when brackets are used)

count=0
num=10
while [ $count -lt 10 ]; do
  echo $num seconds left to stop this process
  sleep 1
  num=$(expr $num - 1)
  count=$(expr $count + 1)
done

echo $1 process is stopped # $1 is the process id
