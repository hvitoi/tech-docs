# FastAPI

- It's a web framework for building APIs with Python
- Fullstack template: <https://github.com/fastapi/full-stack-fastapi-template>

## Installation

```shell
pip install "fastapi[standard]"
```

## Dependencies

- `fastapi`
  - `starlette` for the web parts (WebSockets, CORS, Cookie Sessions, etc)
    - `httpx`: TestClient
    - `jinja2`: default template configuration
    - `python-multipart`: support parsing from request.form()
  - `pydantic` for the schemas, validation, serialization, etc
    - `email-validator`
- `fastapi-cli`
  - `uvicorn`: http server that loads and serves the app

## Running

- <http://localhost:8000/>
- <http://localhost:8000/docs>: Swagger UI
- <http://localhost:8000/openapi.json>: OpenAPI contract
- <http://localhost:8000/redoc>: ReDoc

```shell
fastapi dev main.py
```
