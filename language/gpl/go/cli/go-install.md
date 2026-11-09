# go install

> For installation of dependencies refer to `go get`

- Build and install programs (binaries), it does not require a go.mod
- Compiles and writes a binary to `$GOBIN` for binaries or `$GOPATH/pkg/mod` for shared modules

- `$GOROOT`: sdk directory
- `$GOPATH`: workspace directory (~/go)
- `$GOBIN` ($GOPATH/bin)

- Packages are installed at the `local go module cache`
  - The default module cache path is `$GOPATH/pkg/mod`

- It's usually used to Install a CLI tool such as gopls or dlv

```shell
# builds and installs the main package from the module you're in (cwd). It uses that module's own pinned dependencies.
go install

# Compile and install a remote package on your machine (global)
go install "golang.org/x/tools/gopls@latest"
go install "github.com/AlexSSD7/linsk@latest"
```
