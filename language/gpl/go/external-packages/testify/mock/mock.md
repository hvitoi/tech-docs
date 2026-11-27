# testify/mock

- Package for writing mock objects by hand
- <https://pkg.go.dev/github.com/stretchr/testify/mock>
- Expectations are set by method name as a string (not type-safe); use [mockery](../../mockery/mockery.md) to generate typed mocks instead

## Installation

```shell
go get github.com/stretchr/testify
```

## Core concepts

- **Mock struct**: Embed `mock.Mock` and implement the interface by forwarding to `m.Called(args...)`
  - `args.String(0)`, `args.Int(0)`, `args.Bool(0)`, `args.Error(1)`: typed getters for the return values
  - `args.Get(0).(T)`: for any other type
- **Expectations** (`m.On("Method", args...)`)
  - `.Return(...)`: values returned by `Called`
  - `.Run(func(args mock.Arguments))`: side effects on the call arguments
  - `.Once()`, `.Times(n)`, `.Maybe()`: how many calls are expected
  - Argument matchers: `mock.Anything`, `mock.AnythingOfType("int")`, `mock.MatchedBy(func(T) bool)`
  - An unexpected call panics
- **Assertions**
  - `m.AssertExpectations(t)`: every `On` was satisfied (not called automatically, unlike mockery's `NewMockX(t)`)
  - `m.AssertCalled(t, "Method", args...)` / `m.AssertNotCalled(...)`
  - `m.AssertNumberOfCalls(t, "Method", n)`

## Example

See [example/](example/): a `Greeter` that depends on a `UserStore` interface ([main.go](example/main.go)), the same code as in the mockery example.

- [main_test.go](example/main_test.go): a hand-written `MockUserStore` and tests using `Return`, `mock.Anything`, `mock.MatchedBy`, `Run` and the `Assert*` methods

```shell
$ cd example

$ go test -v ./...
--- PASS: TestGreet (0.00s)
--- PASS: TestGreetError (0.00s)
--- PASS: TestGreetMatchedBy (0.00s)
--- PASS: TestGreetRun (0.00s)
```
