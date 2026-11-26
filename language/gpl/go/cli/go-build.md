# go build

- Just compile go code
- Outputs a binary in the same directory that can be executed

```shell
# No args
go build # It looks for a package main with a function main() in the current directly

# Specify entrypoint
go build "main.go" # outputs "main" binary
go build "main.go" -o a.out # "a.out" binary

# build & run
go build "main.go" -o a.out && ./a.out

##
CGO_ENABLED=1 go build \
  -tags osusergo,netgo \
  -ldflags "-X github.com/myorg/pkg-version.SHA=MY_SHA -X github.com/myorg/pkg-version.Version=1.0.0 -X github.com/myorg/pkg-version.Date=2020-04-20T12:00:00Z -linkmode external -s -w -extldflags '-static'" \
  -trimpath \
  -o "bin/cmd"
```
