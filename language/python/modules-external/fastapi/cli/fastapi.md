# fastapi

## dev

- Run the webserver for local development
- Starts the server using [Uvicorn](https://www.uvicorn.org/)

```shell
fastapi dev main.py
uvicorn "demo:app" --reload # what is actually run under the hood
```

## run

- Run for production

```shell
fastapi run main.py
```
