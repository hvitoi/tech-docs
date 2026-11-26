# Cobra

- Library for building CLI applications
- <https://github.com/spf13/cobra>
- Gives you subcommands, flags (POSIX-style via `pflag`), auto-generated `--help` and shell completion

## Installation

```shell
go get github.com/spf13/cobra@latest
```

## Core concepts

- **Command**: A `*cobra.Command` with a name (`Use`), description and a `Run`/`RunE` function
  - `Run`: no return value, handle errors yourself
  - `RunE`: returns an `error`; Cobra prints it with the usage and `Execute()` returns it (preferred when the command can fail)
- **Args**: Positional arguments passed to `Run` as `[]string` (validate with `Args: cobra.ExactArgs(1)`, etc.)
- **Flags**: Options bound to variables
  - `Flags()`: only for that command
  - `PersistentFlags()`: for that command and all its subcommands
- **Root command**: Top-level command; subcommands are attached with `AddCommand`

## Example

See [example/main.go](example/main.go): a root command `myapp` with two subcommands:

- `greet [name]`: uses `Run`, with a `--shout`/`-s` flag
- `divide [a] [b]`: uses `RunE` to return errors (invalid number, division by zero)

```shell
$ cd example

$ go run . greet Alice
Hello, Alice!

$ go run . greet Alice --shout
HELLO, ALICE!

$ go run . greet
Error: accepts 1 arg(s), received 0

$ go run . divide 10 2
5

$ go run . divide 10 0
Error: cannot divide by zero

$ go run . --help        # auto-generated help, also lists `completion` and `help` commands
```
