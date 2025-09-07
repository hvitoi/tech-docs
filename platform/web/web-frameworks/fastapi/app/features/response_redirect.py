from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse

router = APIRouter(
    prefix="/response_redirect",
    tags=["RedirectResponse"],
)


# Returns an HTTP redirect. Uses a 307 status code (Temporary Redirect) by default.
@router.get("/", response_class=RedirectResponse)
def get_resource() -> Response:
    # return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
