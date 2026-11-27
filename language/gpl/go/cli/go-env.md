# go env

- User envs: `~/Library/Application Support/go/env`
- Shipped with the toolchain: `$GOROOT/go.env`
- Go env file `./go.env`

```shell
# print all go environment variables
go env

# print a specific go environment variable
go env GOPRIVATE

# changes an environment variable
go env -w GOPRIVATE='github.com/foo/*' # writes to ~/Library/Application Support/go/env
```
