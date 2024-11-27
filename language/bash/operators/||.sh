# || (or)

# - If the first command return 0, return early
# - Otherwise execute the rest of the commands

cp ./a ./b 2>/dev/null || :

if grep -q "Debian" /etc/os-release || grep -q "Ubuntu" /etc/os-release; then
  sudo apt update && sudo apt upgrade
fi

(cat foo.md || echo "file not found") >report.txt
