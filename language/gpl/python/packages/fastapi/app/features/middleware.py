import time

from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

app = None  # Mocked FastAPI app

## Middleware are like interceptors that can run before and after the path operation function

# Register middlewares (apply to all routes)
# app.add_middleware(MyInnermostMiddleware)
# app.add_middleware(MyOutermostMiddleware)


## ---- Custom Middleware


# Add middleware with decorator
# you can define middleware as a decorator, or by using app.add_middleware(add_process_time_header)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# app.add_middleware(ProcessTimeMiddleware)
# Add middleware with class (imported in the main file)
class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        return await add_process_time_header(request, call_next)


## ----- CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## ----- HTTPSRedirectMiddleware

# Any incoming request to http or ws will be redirected to the secure scheme instead (https, wss)
app.add_middleware(HTTPSRedirectMiddleware)


## ----- TrustedHostMiddleware

# Enforces that all incoming requests have a correctly set Host header, in order to guard against HTTP Host Header attacks.
# To allow any hostname either use allowed_hosts=["*"] or omit the middleware.
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)


## ------ GZipMiddleware

# Handles GZip responses for any request that includes "gzip" in the Accept-Encoding header
# minimum_size: Do not GZip responses that are smaller than this minimum size in bytes
# compresslevel: lower values results in faster compressions, but larger file sizes
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)
