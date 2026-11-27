# Gin

- HTTP web framework for Go, built on top of `net/http`
- <https://github.com/gin-gonic/gin>
- Fast radix-tree router, middleware chain, JSON binding/validation and rendering helpers

## Installation

```shell
go get github.com/gin-gonic/gin@latest
```

## Core concepts

- **Engine**: The router, created with `gin.New()` or `gin.Default()`
  - `gin.New()`: bare engine, no middleware
  - `gin.Default()`: `gin.New()` + `Logger` and `Recovery` middleware
- **Route**: HTTP method + path + handler(s), e.g. `r.GET("/path", handler)`
- **HandlerFunc**: `func(c *gin.Context)`, the type of both handlers and middleware
  - Handlers don't return errors, they write the response (status + body) themselves
- **Context**: Per-request object to read input and write output
  - `c.Param("name")`: path parameter from `/greet/:name`
  - `c.Query("key")`: query string parameter (`?key=value`)
  - `c.GetHeader("key")`: request header
  - `c.ShouldBindJSON(&v)`: decode and validate the request body into a struct
  - `c.JSON(status, body)` / `c.String(status, text)`: write the response
- **gin.H**: Shortcut for `map[string]any`, handy for JSON bodies

## Middleware

- A `gin.HandlerFunc` that runs in a chain before the route handler
- Usually written as a function returning `gin.HandlerFunc`, so it can take config (e.g. `APIKey("secret")`)
- `c.Next()`: run the rest of the chain, code after it runs once the response is written (timing, logging)
- `c.Abort()` / `c.AbortWithStatusJSON(...)`: stop the chain, later handlers don't run (auth checks)
- Attach it:
  - globally: `r.Use(mw)`
  - to a group: `r.Group("/api", mw)` or `group.Use(mw)`
  - to a single route: `r.GET("/path", mw, handler)`

```text
request ──► Recovery ──► Timer ──► APIKey ──► handler
                           │          │
                           │          └─(bad key)─► AbortWithStatusJSON(401)
                           └─ after c.Next(): log status and duration
```

## Static files

- `r.StaticFile("/", "./public/index.html")`: serve one file at one path
- `r.Static("/assets", "./public/assets")`: serve a whole directory under a prefix (`/assets/*filepath`)
- `r.StaticFS(...)`: same as `Static`, but takes an `http.FileSystem` (e.g. an `embed.FS`)

## Route groups

- `r.Group(prefix, middleware...)` returns a `*gin.RouterGroup` sharing a path prefix and middleware
- Groups can be nested (`v1 := api.Group("/v1")`)
- The `{ ... }` block after it is only for readability, it has no meaning to Go

## Example

See [example/](example/):

- [main.go](example/main.go): `gin.New()`, global middleware, static files and the `/api` group
- [middleware.go](example/middleware.go): `Timer` (uses `c.Next()`) and `APIKey` (uses `c.AbortWithStatusJSON`)
- [handlers.go](example/handlers.go): `greet` and `divide` handlers
- [public/](example/public/): `index.html` and `assets/style.css` served as static files

| Route                  | Middleware                 | Description                                   |
| ---------------------- | -------------------------- | --------------------------------------------- |
| `GET /`                | Recovery, Timer            | `public/index.html`                           |
| `GET /assets/*`        | Recovery, Timer            | files in `public/assets/`                     |
| `GET /health`          | Recovery, Timer            | plain text `ok`                               |
| `GET /api/greet/:name` | Recovery, Timer, APIKey    | greeting, optional `?shout=true`              |
| `GET /api/divide`      | Recovery, Timer, APIKey    | `?a=&b=`, `400` on bad numbers or `b=0`       |

```shell
$ cd example

$ go run .

$ curl 'localhost:8080/assets/style.css'
body { font-family: sans-serif; }

$ curl 'localhost:8080/health'
ok

$ curl 'localhost:8080/api/greet/Alice'
{"error":"invalid api key"}

$ curl -H 'X-API-Key: secret' 'localhost:8080/api/greet/Alice?shout=true'
{"message":"HELLO, ALICE!"}

$ curl -H 'X-API-Key: secret' 'localhost:8080/api/divide?a=10&b=0'
{"error":"cannot divide by zero"}
```

Server logs from the `Timer` middleware:

```text
GET /health -> 200 (2.917µs)
GET /api/greet/Alice -> 401 (155.417µs)
GET /api/greet/Alice -> 200 (58.542µs)
```
