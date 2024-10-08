# test

- Test files are defined with `*_test.go` suffix
- In order to run tests you need `go.mod` file that defines your module (your project)
- When running tests, the main functions are ignored. Only the `TestXxx(t *testing.T)` functions are executed

```shell
# Run tests for the current module
go test

# Run tests for a module
go test github.com/hvitoi/playground

# Run tests for a file (even if it does not contain the test suffix)
go test yourfile.go

# timeout
go test -timeout 30s

# run a specific test function
go test -run TestAdd github.com/hvitoi/playground # of a module
go test -run TestAdd yourfile.go # of a file
go test -run ^TestAdd$ # regex
```
