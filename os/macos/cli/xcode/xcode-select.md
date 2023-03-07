# xcode-select

- If Xcode is installed, this should point at the `Xcode` installation (/Applications/Xcode.app/Contents/Developer)
- Else it should point at the `developer tools` (/Library/Developer/CommandLineTools/)

```shell
# Install Command line developer tools
# Not necessary if Xcode is available
xcode-select --install
```

```shell
# switch the active developer directory to a given path
xcode-select --switch "/Applications/Xcode_13.2.1.app"
```
