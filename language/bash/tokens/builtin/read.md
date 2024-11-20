# read

```shell
echo "What is your name?"
read fancy_name # Wait input from stdin
echo "Hello $fancy_name"
```

```shell
read -p "Do you wish to drink a beer?" answer
```

```shell
pair="item1:value1"
IFS=":" read -r item value <<< "$pair"
echo "Item: $item, Value: $value"
```
