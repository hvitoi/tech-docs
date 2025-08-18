from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse

router = APIRouter(
    prefix="/response_redirectresponse",
    tags=["Response RedirectResponse"],
)


@router.get("/")
def get_resource() -> Response:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
