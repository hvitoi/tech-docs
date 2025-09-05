# jq

- JQ is a command-line JSON processor

```shell
set json '{"a":"alpha"}'

# --compact-output
echo $json | jq -c

# --monochrome-output
echo $json | jq -M

# --sort-keys
echo $json | jq -S

# --raw-input
set input 'abc'
echo $input | jq -R

# --raw-output
echo $json | jq -r '.a' # no "quotes"

# --slurp
echo $json | jq -s # dump output into array

# --null-input
echo '{}' | jq -n # empty map is treated as null
echo '[]' | jq -n # empty array is treated as null
echo '' | jq -n # empty input is treated as null
echo 'foo' | jq -n # invalid input is treated as null

# --arg
jq -n \
   --arg foo "1" \
   --arg bar "2" \
   '[$foo, $bar]'

# --argjson
jq -n \
   --argjson foo '{"a":1}' \
   '$foo'
```

```shell
json='["a","b","c"]'
arr=($(echo $json | jq -r '.[]'))
echo ${arr[0]}
echo ${arr[1]}
echo ${arr[2]}
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
