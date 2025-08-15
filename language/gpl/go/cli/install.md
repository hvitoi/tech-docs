# install

- `$GOROOT`: sdk directory
- `$GOPATH`: workspace directory

- Packages are installed at the `local go module cache`
  - The default module cache path is `$GOPATH/pkg/mod`

```shell
# Compile and install a package in cwd
go install

# Compile and install a remote package
go install "github.com/go-flutter-desktop/hover@latest"
go install "github.com/AlexSSD7/linsk@latest"
```
