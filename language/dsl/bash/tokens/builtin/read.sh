echo "What is your name?"
read -r fancy_name # Wait input from stdin
echo "Hello $fancy_name"

# -r: do not allow backslashes to escape any characters

read -p "Do you wish to drink a beer?" answer

pair="item1:value1"
IFS=":" read -r item value <<<"$pair"
echo "Item: $item, Value: $value"
