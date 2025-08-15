options=("Option 1" "Option 2" "Option 3" "Quit")

# "select" is a loop that prompts an input
# It takes an array position (1-indexed) and gets the value from the provided array
# The translated value is stored in the "opt" variable
select opt in "${options[@]}"; do
  echo "You chose $opt"
  if [ "$opt" = "Quit" ]; then
    echo "Quitting..."
    break
  fi
done
