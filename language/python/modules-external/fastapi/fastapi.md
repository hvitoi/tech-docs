# FastAPI

- It's a web framework for building APIs with Python

## Installation

```shell
pip install "fastapi[standard]"
```

- Packages
  - `fastapi`
    - `starlette` for the web parts (WebSockets, CORS, Cookie Sessions, etc)
      - `httpx`: TestClient
      - `jinja2`: default template configuration
      - `python-multipart`: support parsing from request.form()
    - `pydantic` for the data parts
      - `email-validator`
  - `fastapi-cli`
    - `unicorn`: http server that loads and serves the app

## Running

- <http://localhost:8000/>
- <http://localhost:8000/docs>: Swagger UI
- <http://localhost:8000/redoc>: ReDoc

```shell
fastapi dev main.py
```
