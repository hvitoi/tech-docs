# jq

- JQ is a command-line JSON processor

```shell
echo '{"a":1}' | jq -c # compact json (one-line)
echo '{"a":1}' | jq -M # no color (with formatting)
echo '{"b":2,"a":1}' | jq -S # sort keys
echo 'abc' | jq '[.]' -R # raw input (instead of json)
echo '{"a":"alpha"}' | jq '.a' -r # raw output (without quotes)
echo '[{}]' | jq -s '.[]' # dump output into array
echo '{}' | jq -n # accepts no input
jq -n --arg foo "1" --arg bar "2" '[$foo, $bar]' # access variable
jq -n --argjson foo '{"a":"b"}' '[$foo]' # access variable (also accepts null variables)
```

```shell
# JQ to array
CLIENTS=($(hyprctl clients -j | jq -r '.[] | .address'))
```

## . (identity)

- Return the initial input
- If no other modifier is passed, returns the unchanged input

```shell
set json '{"a":1}'
echo $json | jq '.'
echo $json | jq # same
```

## .[]

- Extract values from a json array

```shell
set json '["a","b","c"]'

# first element in array
echo $json | jq '.[0]'

# all elements
echo $json | jq '.[]'
```

## {}

```shell
# select keys a and c
set json '{"a":1,"b":2,"c":3}'
echo $json | jq '{ a, c }'
```

## .key

- Get a field

```shell
# Single key
jq '.a' <<< '{"a":1}'

# Single key with special characters
jq '."The key"' <<< '{"The key":1}'

# Multiple keys
jq '.a,.b' <<< '{"a":1,"b":2,"c":3}'

# Nested keys
jq '.a.a1' <<< '{"a":{"a1":1,"a2":2}}'

# Keys in a map in an array
jq '.[] | .a' <<< '[{"a":1}]'
```

## [.]

- Force the result into an array

```shell
# Destructure and the array and convert it back to array
jq '[ .[] ]' <<< '[{"a":1}]'
```

```shell
# Remove nulls and empties
jq -n \
  '{
    "a": "a",
    "b": null,
    "c": "c",
    "d": ""
    } | del(.[] | select( . == null or . == ""))'
```

```shell
# Remove nulls
jq -n \
  '{
    "a": "a",
    "b": null,
    "c": "c",
    "d": ""
    } | del(.[] | nulls)'
```

## if

```shell
echo '2' | jq 'if . == 0 then "zero" elif . == 1 then "one" else "many" end'
```

## other

```shell
echo {1..10..1} |
 jq -Rn '(input | split(" ")) as $nums
        | $nums[]
        | . as $num
        | [
            {
              key: ($num | tostring),
              value:($num | tonumber)
            }
          ]
        | from_entries' |
  jq -cs 'add'
```

## def

```shell
jq -n -r '

  def colors:
    {
      "black": "\u001b[30m",
      "red": "\u001b[31m",
      "green": "\u001b[32m",
      "yellow": "\u001b[33m",
      "blue": "\u001b[34m",
      "magenta": "\u001b[35m",
      "cyan": "\u001b[36m",
      "white": "\u001b[37m",
      "reset": "\u001b[0m",
    };

  colors.red + "red" + colors.green + "green"

  # print $text in the specified color
  def pc($text; color):
    (colors | color) + $text + colors.reset;

  # Usage example:
  pc("red"; .red) + pc("green"; .green)
'
```

## @sh

```shell
msgids=($(<test.json jq -r '.logs[]._id | @sh'))
```

## try catch

```shell
set json '{"a":1}'
set json 'foo'
echo $json | jq 'try . catch .'
```

## Array Operations

### reverse

```shell
set json '["a", "b", "c"]'
echo $json | jq 'reverse'
```

### length

```shell
echo '["a","b","c"]' | jq 'length'
```

### reduce

```shell
set json '[1, 2, 3, 4, 5]'
echo $json | jq 'reduce .[] as $el (0; . + $el)'

```

### map

```shell
echo '[1,2,3]' | jq 'map(. * .)'
echo '[{"a":"1","b":"2"},{"a":"3","b":"4"}]' | jq 'map({a, b})'
```

### sort_by

```shell
echo '[{"a":2},{"a":1}]' | jq 'sort_by(.a)'
```

### last

- Take last element of an array

```shell
echo '["a", "b", "c"]' | jq 'last'
```

## Array Operations (destructured)

### select

```shell
# select on destructured array
echo '[{"foo":true},{"foo":false}]' | jq '.[] | select(.foo == false)'

# select on plain array
echo '[{"foo":true},{"foo":false}]' | jq 'map(select(.foo == false))'
```

## Map Operations

### to_entries

- Transform a map into an array
- Each key of the map turns in an entry in the array

```shell
set json '{
            "a": {"alpha": 1},
            "b": {"beta": 1}
          }'
echo $json | jq 'to_entries'
```

### del

- Remove keys

```shell
set json '{"a":"alpha","b":"beta"}'
echo $json | jq 'del(.b)'
```
