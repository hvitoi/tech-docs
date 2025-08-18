# fastapi

## dev

- Run the webserver for local development with auto-reload
- Starts the server using [Uvicorn](https://www.uvicorn.org/)
- By default server is exposed at <http:127.0.0.1:8000/>

```shell
fastapi dev main.py
uvicorn "demo:app" --reload # what is actually run under the hood
```

## run

- Run for production
- Listens on `0.0.0.0` (from everywhere)

```shell
fastapi run main.py
```
