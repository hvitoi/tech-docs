# yq

```shell
# get a key
cat sample.yaml | yq
cat sample.yaml | yq '.'
cat sample.yaml | yq '.experiments'
cat sample.yaml | yq '.experiments[0]'
cat sample.yaml | yq '.experiments[]' # returns multiple elements
```

## -o

- Specify the output format

```shell
yq sample.json # if not specified returns the same format from the file
yq sample.json -o yaml # or "y"
yq sample.json -o json # or "j"
yq sample.json -o props # or "p"
yq sample.json -o csv # or "c"
yq sample.json -o tsv # or "t"
yq sample.json -o xml # or "x"
yq sample.json -o base64
yq sample.json -o uri
yq sample.json -o toml
yq sample.json -o shell # or "s"
yq sample.json -o lua # or "l"
```

## -p

- Specify the input format

```shell
# if not specified get the format from the extension
yq sample.json

# useful for inline expressions
echo '{"foo":"bar"}' | yq -p json -o yaml
```

## -i

- In-place changes

```shell
yq -i '.foo = "baz"' sample.yaml
```
