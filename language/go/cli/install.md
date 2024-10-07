# install

- `$GOROOT`: sdk directory
- `$GOPATH`: workspace directory

- By default the package is installed into `$GOPATH`

```shell
# Compile and install a package in cwd
go install

# Compile and install a remote package
go install "github.com/go-flutter-desktop/hover@latest"
go install "github.com/AlexSSD7/linsk@latest"
```
