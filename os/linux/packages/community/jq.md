# jq

- JQ is a command-line JSON processor

```shell
echo '{"foo":}' | jq -c # json line (compact)
echo '{"foo":0}' | jq -M # no color
echo '{"b":2,"a":1}' | jq -S # sort keys
echo "abc" | jq -R '[.]' # raw input (instead of json)
echo '{"foo":"bar"}' | jq -r '.foo'  # raw output (without quotes)
jq --arg MY_VAR bar '{"foo":$MY_VAR}' # set variable
```

```shell
# JQ to array
CLIENTS=($(hyprctl clients -j | jq -r '.[] | .address'))
```

## . (identity)

- Return the initial input
- If no other modifier is passed, returns the unchanged input

```shell
echo $json | jq '.'
echo $json | jq
```

## .[]

- Extract values from a json array

```shell
# first element in array
echo '["a", "b", "c"]' |
  jq '.[0]'

# all elements
echo '["a", "b", "c"]' |
  jq '.[]'
```

## .key

- Get a field

```shell
# Single key
echo '{"a":1}' |
  jq '.a'

# Single key with special characters
echo '{"The key":1}' |
  jq '."The key"'

# Multiple keys
echo '{"a":1,"b":2,"c":3}' |
  jq '.a,.b'

# Nested keys
echo '{"a":{"a1":1,"a2":2}}' |
  jq '.a.a1'

# Keys in a map in an array
echo '[{"a":1}]' |
  jq '.[]
      | .a'
```

## [.]

- Force the result into an array

```shell
# Destructure and the array and convert it back to array
echo '[{"a":1}]' |
  jq '[ .[] ]'
```

## select

```shell
echo '[{"foo":true},{"foo":false}]' |
  jq '.[]
      | select(.foo == false)'
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

## @sh

```shell
msgids=($(<test.json jq -r '.logs[]._id | @sh'))
```
