# example-app

## Run

```sh
go run ./cmd/server            # listens on :8080
go run ./cmd/server -addr :9000
go test ./...
```

## Routes

| Method | Path | Description |
| --- | --- | --- |
| GET | `/health` | Health check |
| GET | `/tasks` | List tasks (optional `?done=true\|false`) |
| POST | `/tasks` | Create a task |
| GET | `/tasks/{id}` | Get a task |
| PUT | `/tasks/{id}` | Replace a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Try it

```sh
curl -i localhost:8080/health

curl -i -X POST localhost:8080/tasks -d '{"title":"buy milk"}'
curl -i localhost:8080/tasks
curl -i localhost:8080/tasks/1
curl -i -X PUT localhost:8080/tasks/1 -d '{"title":"buy milk","done":true}'
curl -i 'localhost:8080/tasks?done=true'
curl -i -X DELETE localhost:8080/tasks/1

# errors
curl -i -X POST localhost:8080/tasks -d '{"title":""}'      # 422 validation
curl -i -X POST localhost:8080/tasks -d '{"title":'         # 400 bad JSON
curl -i localhost:8080/tasks/abc                            # 400 bad id
curl -i -X PATCH localhost:8080/tasks                       # 405 (set by ServeMux)
```
