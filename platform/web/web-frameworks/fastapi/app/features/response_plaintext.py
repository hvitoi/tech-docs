from fastapi import APIRouter, Response
from fastapi.responses import PlainTextResponse

router = APIRouter(
    prefix="/response_plaintext",
    tags=["PlainTextResponse"],
)


@router.get("/", response_class=PlainTextResponse)
def get_resource() -> Response:
    return "Hello World"
