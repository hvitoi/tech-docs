# jq

- JQ is a command-line JSON processor

```shell
jq -c <<< '{"foo":}' # json line (compact)
jq -M <<< '{"foo":0}' # no color
jq -S <<<'{"b":2,"a":1}' # sort keys
jq '[.]' -R <<< 'abc' # raw input (instead of json)
jq '.foo' -r <<< '{"foo":"bar"}' # raw output (without quotes)
jq -s '.[]' <<< '[{}]' # dump output into array after filters
jq --arg MY_VAR bar <<< '{"foo":"$MY_VAR"}' # set variable ???
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

## select

```shell
jq '.[] | select(.foo == false)' <<< '[{"foo":true},{"foo":false}]'
```

## sort_by

- Sorty by can only be used over arrays (not destructured arrays)

```shell
jq -s '.[] | sort_by(.a)' <<< '[{"a":2},{"a":1}]'
```

## last

- Take last element of an array

```shell
jq -s 'last' <<< '["a", "b", "c"]'
```

## other

```shell
jq -Rn '(input | split(" ")) as $nums
        | $nums[]
        | . as $num
        | [
            {
              key: ($num | tostring),
              value:($num | tonumber)
            }
          ]
        | from_entries' <<< {1..10..1} | jq -cs 'add'
```

## @sh

```shell
msgids=($(<test.json jq -r '.logs[]._id | @sh'))
```
