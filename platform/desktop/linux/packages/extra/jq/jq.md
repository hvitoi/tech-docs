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
jq '.' <<< $json
jq <<< $json
```

## .[]

- Extract values from a json array

```shell
# first element in array
jq '.[0]' <<< '["a", "b", "c"]'

# all elements
jq '.[]' <<< '["a", "b", "c"]'
```

## {}

```shell
# select keys a and c
jq -c '{ a, c }' <<< '{"a":"aa","bb":"b","cc":"c"}'
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

## reduce

```shell
cat '{"a":{"NET_DOWN": 1, "NET_UP": 2},"b":{"NET_DOWN": 1, "NET_UP": 2}}' | jq 'to_entries | reduce .[] as $i (""; . + "\($i.key): Download \($i.value.NET_DOWN), Upload \($i.value.NET_UP)\n")'
```

## Array Operations

## map

```shell
echo '[1,2,3]' | jq 'map(. * .)'
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

## del

```shell
# Remove fields
jq -n \
  '{
    "a": "alpha",
    "b": "beta"
    } | del(.b)'
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
jq 'if . == 0 then "zero" elif . == 1 then "one" else "many" end' <<< '2'
```

## length

```shell
echo '["a","b","c"]' | jq 'length'
```

## @sh

```shell
msgids=($(<test.json jq -r '.logs[]._id | @sh'))
```
