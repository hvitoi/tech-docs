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
while [ $count -lt 10 ]; do
  echo "$(expr 10 - $count) seconds left to stop this process"
  sleep 1
  count=$(expr $count + 1)
done

# while entries from stdin
brew list --formula |
  while read formula; do
    brew list $formula |
      while read file; do
        echo -e "$formula\t$file"
      done
  done

# Read lines
while IFS= read -r line; do
  echo "Line: $line"
done <filename.txt
