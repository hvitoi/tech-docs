# build

- Just compile go code
- Outputs a binary in the same directory that can be executed

```shell
go build "main.go" # outputs "main" binary
go build "main.go" -o a.out # "a.out" binary

# build & run
go build "main.go" -o a.out && ./a.out
```
