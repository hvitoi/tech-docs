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

## Project structure

```shell
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── deps.py          # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
```

## ASGI Server (Asynchronous Server Gateway Interface)

- <http://localhost:8000/>
- <http://localhost:8000/docs>: Swagger UI
- <http://localhost:8000/openapi.json>: OpenAPI contract
- <http://localhost:8000/redoc>: ReDoc

```shell
fastapi dev main.py # runs with unicorn by default
```

- `Uvicorn`: a high performance ASGI server (the default used by fastapi)
- `Hypercorn`: an ASGI server compatible with HTTP/2 and Trio among other features.
- `Daphne`: the ASGI server built for Django Channels.
- `Granian`: A Rust HTTP server for Python applications.
- `NGINX Unit`: NGINX Unit is a lightweight and versatile web application runtime.

- Other web frameworks like Flask and Django use WDGI (Web Server Gateway Interface)

## Debugging

You can run the uvicorn ASGI server directly from the Python file:

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

And run it as a python module:

```shell
# your cwd needs to be the parent directory of the demo package
python -m app.main # package "app", module "main"
```
