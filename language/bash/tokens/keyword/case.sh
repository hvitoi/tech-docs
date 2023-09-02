echo Choose an option
echo 'a = Display date and time'
echo 'b = List file and directories'
echo 'c = List users logged in'
echo 'd = Check system uptime'
read choice

case $choice in
a) date ;; # 'a' run the command date;
b) ls ;;
c) who ;;
d) uptime ;;
*) echo "Invalid choice." ;; # default option
esac

# ---

while true; do
  read -p "Do you wish to drink a beer?" answer
  case $answer in
  [Yy]*) break ;;
  [Nn]*) exit ;;
  *) echo "Please answer yes or no." ;;
  esac
done
