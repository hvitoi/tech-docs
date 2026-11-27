# Mockery

- Code generator that creates mock implementations of Go interfaces
- <https://github.com/vektra/mockery>
- Default `testify` template generates mocks built on `github.com/stretchr/testify/mock`, with type-safe `EXPECT()` builders (see [testify/mock](../testify/mock/mock.md) for writing them by hand)

## Installation

```shell
# as a tool dependency of the module (Go 1.24+): pinned in go.mod via a `tool` directive
go get -tool github.com/vektra/mockery/v3@v3.9.2
go tool mockery

# or globally
go install github.com/vektra/mockery/v3@latest
mockery
```

- Not a library: the generated code only imports `testify/mock`, so without `-tool` mockery never appears in `go.mod`
- With `-tool`, mockery's own dependencies are added to `go.mod` as `// indirect`

## Core concepts

- **Config** (`.mockery.yml`): Declares which packages/interfaces to mock and where to write them
  - `dir`, `filename`, `pkgname`, `structname`: output location and naming (support templates like `{{.InterfaceName}}`)
  - `packages`: map of import path -> interfaces to mock (or `all: true` for every interface)
- **Constructor** (`NewMockX(t)`): Creates the mock and registers a `t.Cleanup` that asserts all expectations were met
- **Expectations** (`mock.EXPECT().Method(args...)`): Type-safe setup of calls
  - `.Return(...)`: fixed return values
  - `.RunAndReturn(func)`: compute return values from the arguments
  - `.Once()`, `.Times(n)`, `.Maybe()`: how many calls are expected
  - Argument matchers: `mock.Anything`, `mock.AnythingOfType("int")`, `mock.MatchedBy(func)`

## Example

See [example/](example/): a `Greeter` that depends on a `UserStore` interface ([main.go](example/main.go)).

- [go.mod](example/go.mod): pins mockery with `tool github.com/vektra/mockery/v3`
- [.mockery.yml](example/.mockery.yml): generates `MockUserStore` into `mocks_test.go` in the same package
- [mocks_test.go](example/mocks_test.go): generated mock (do not edit)
- [main_test.go](example/main_test.go): tests using `Return`, `mock.Anything` and `RunAndReturn`

```shell
$ cd example

$ go tool mockery   # (re)generate mocks_test.go

$ go test -v ./...
--- PASS: TestGreet (0.00s)
--- PASS: TestGreetError (0.00s)
--- PASS: TestGreetRunAndReturn (0.00s)
```
