# mod

- `Go Modules` are the standard way to manage dependencies and versioning in Go projects
- The `go.mod` file defines a module
  - The name of the module
  - The root package of the module (your project)
  - The go version
  - Other dependencies
- The `go.mod` file is usually created at the root of the project

```shell
# initialize a module. This creates a `go.mod` file in cwd
go mod init github.com/username/myproject

# remove unused dependencies
go mod tidy

# explains why a particular dependency is added
go mod why

# downloads the modules required by the project
go mod download

# checks that the dependencies in go.mod and go.sum are correct
go mod verify
```

- Dependencies are added to `go.mod` automatically when running commands that fetches them, like `go get`, `go build`, `go run`

## go.mod

```go
// go.mod
module github.com/username/myproject

go 1.20

require (
    github.com/some/dependency v1.5.2
    golang.org/x/tools v0.1.2
)
```

## go.sum

- `go.sum` is a lock file to fixes a specific version by its checksum (hash)
- Ensures the integrity and reproducibility
