from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/response_file",
    tags=["PlainTextResponse"],
)


@router.get("/", response_class=FileResponse)
def get_resource() -> Response:
    return "large-video-file.mp4"
