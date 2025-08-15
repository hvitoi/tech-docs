# test

- Test files are defined with `*_test.go` suffix. Files that do not obey this pattern will not be executed as tests.
- When running tests, only the `TestXxx(t *testing.T)` functions are executed
- In order to run module-wide tests you need `go.mod` file that defines your module (your project)
- Go tests are always intended to be run via `go test`. Calling tests by other means (e.g., via your code itself) may be possible, but not supported

```shell
# Run tests for the current module
go test

# Run tests for a module
go test github.com/hvitoi/playground

# Run tests for a file
go test file_test.go

# timeout
go test -timeout 30s

# run a specific test function
go test -run TestAdd github.com/hvitoi/playground # of a module
go test -run TestAdd yourfile.go # of a file
go test -run ^TestAdd$ # regex
```
