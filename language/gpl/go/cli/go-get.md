# go get

> For installation of programs (binaries) refer to `go install`

- Manage dependencies of the current module (requires `go.mod`!)
  - It modifies go.mod file
- It updates the module's required versions and downloads source

```shell
# Download raw source code of someone else's package
go get

# Upgrade dependencies before getting the dependencies
go get -u && go mod tidy # and remove unused

# add a dependency to go.mod
go get -v "github.com/gorilla/mux@v1.8.1"
```
