from fastapi import APIRouter, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

router = APIRouter(
    prefix="/exceptionhandlers",
    tags=["Exception & Exception Handlers"],
)


# --- Default Exception Handler
@router.get("/items/{item_id}")
async def default_exception_handler(item_id: str):
    items = {"a": 1, "b": 2, "c": 3}
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},  # extra headers
        )
    return {"item": items[item_id]}


# --- Custom Exception Handler


class MyException(Exception):
    def __init__(self, name: str):
        self.name = name


# @app.exception_handler(MyException) # either annotation the exception handler or use the function app.add_exception_handler
async def my_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


# Override for HTTPException
# @app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return PlainTextResponse(
        str(exc.detail),
        status_code=exc.status_code,
    )


# You can re-use the http_exception_handler
# @app.exception_handler(StarletteHTTPException)
async def http_exception_handler_reused(request: Request, exc: StarletteHTTPException):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)  # invoke here the default handler


# Override for RequestValidationError
# @app.exception_handler(RequestValidationError)
async def request_validation_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "detail": exc.errors(),
                "body": exc.body,
            }
        ),
    )


@router.get("/unicorns/{name}")
async def get_unicorns(name: str):
    if name == "yolo":
        raise MyException(name=name)  # this will be handled by the my_exception_handler
    return {"unicorn_name": name}
