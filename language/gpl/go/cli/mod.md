# mod

- `Go Modules` are the standard way to manage dependencies and versioning in Go projects

## init

- Initialize a module.
- This creates a `go.mod` file in cwd

```shell
go mod init github.com/username/myproject
```

## downloads

- Downloads the modules required by the project into the local go module cache (`$GOPATH/pkg/mod`)

```shell
go mod download
```

## vendor

- Copy the dependencies from the local go module cache into the `./vendor` directory

```shell
go mod vendor
```

## tidy

- Remove unused dependencies
- This also performs other operations like adding the `//indirect` comment for implicit dependencies at `go.mod`

```shell
go mod tidy
```

## why

- Explains why a particular dependency is added

```shell
go mod why
```

## verify

- Checks that the dependencies in `go.mod` and `go.sum` are correct

```shell
go mod verify
```
