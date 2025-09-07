# fastapi

## dev

- Run the webserver for local development with auto-reload
- Starts the server using [Uvicorn](https://www.uvicorn.org/)
- By default server is exposed at <http:127.0.0.1:8000/>

```shell
fastapi dev main.py

# Run uvicorn directly
uvicorn "main:app" --reload # main: the module/file; app: the object within the module
```

## run

- Run for production
- Listens on `0.0.0.0` (from everywhere)

```shell
fastapi run main.py
fastapi run main.py --workers 4 # 1 manager process + 4 worker processes
fastapi run main.py --port 80 # port to be exposed
fastapi run main.py --proxy-headers # used when running behind a TLS Termination Proxy. It tells Uvicorn to trust the headers sent sent by that proxy telling that the application is running behind HTTPS
fastapi run main.py --root-path /api/v1 # tells the app that it is run behind a proxy and adds the /api/v1 prefix


# Run uvicorn directly
uvicorn "main:app" --host 0.0.0.0 --port 80
# main: the module/file
# app: the object created in the main module; app = FastAPI()
# Equivalente to "from main import app"
```
