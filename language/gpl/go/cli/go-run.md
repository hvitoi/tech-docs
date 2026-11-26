# go run

- `Compiles` and immediately `executes` go code

```shell
# run single file
go run main.go

# run multiple files (useful when running multiple files that compose the same package)
go run main.go deck.go

# run a folder
go run ./cmd/server/
go run cmd/server # this will not work as it will try to lookup in go std library ($GOROOT/src/cmd/server)
go run example-app/cmd/server # this work as the module name is defined
```
