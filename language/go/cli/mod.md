# mod

- `Go Modules` are the standard way to manage dependencies and versioning in Go projects

```shell
# initialize a module. This creates a `go.mod` file in cwd
go mod init github.com/username/myproject

# downloads the modules required by the project into the local go module cache ($GOPATH/pkg/mod)
go mod download

# copy the dependencies from the local go module cache into the ./vendor directory
go mod vendor

# remove unused dependencies
go mod tidy

# explains why a particular dependency is added
go mod why

# checks that the dependencies in go.mod and go.sum are correct
go mod verify
```

## go.mod

- The `go.mod` file defines a module.
- It is created at the root of the project
- Dependencies are added to `go.mod` automatically when running commands that fetches them, like `go get`, `go build`, `go run`

```go
// go.mod

// module identifier
module github.com/username/myproject

// go version
go 1.20

// explicit dependencies
require (
    github.com/some/dependency v1.5.2
    golang.org/x/tools v0.1.2
)
```

## go.sum

- `go.sum` is a lock file to fixes a specific version by its checksum (hash)
- Ensures the integrity and reproducibility
