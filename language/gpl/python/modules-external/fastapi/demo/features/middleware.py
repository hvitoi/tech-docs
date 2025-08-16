import time
from fastapi import APIRouter, Request
from starlette.middleware.base import BaseHTTPMiddleware

## Middleware are like interceptors that can run before and after the path operation function

router = APIRouter(
    prefix="/middleware",
    tags=["Middleware"],
)

## ---- Custom Middleware


# Add middleware with decorator
# @app.middleware("http") # you can define middleware as a decorator, or by using app.add_middleware()
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Add middleware with class (imported in the main file)
class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        return await add_process_time_header(request, call_next)


## ---- CORS Middleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
