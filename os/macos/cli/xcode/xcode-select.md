# xcode-select

## install

```shell
# Install Command line developer tools
# Not necessary if Xcode is available
xcode-select --install
```

## print-path

- If **xcode** is installed
  - Path is `/Applications/Xcode.app/Contents/Developer`
- If only **developer tools** is installed
  - Path is `/Library/Developer/CommandLineTools/`

```shell
xcode-select --print-path
```

## switch

```shell
# switch the active developer directory to a given path
xcode-select --switch "/Applications/Xcode_13.2.1.app"
```

## reset

- Reset to the default path, xcode or devtools

```shell
xcode-select --reset
```
