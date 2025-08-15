# get

```shell
# Download raw source code of someone else's package
go get

# Upgrade dependencies before getting the dependencies
# This command updates go.mod file
go get -u && go mod tidy # and remove unused

# add a dependency to go.mod
go get "github.com/some/dependency"

# Download LSP
go get -v "golang.org/x/tools/gopls"
```
