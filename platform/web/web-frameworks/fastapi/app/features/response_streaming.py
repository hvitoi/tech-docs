from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time
import json

router = APIRouter(
    prefix="/response_streaming",
    tags=["StreamingResponse"],
)


def stream_my_ndjson():
    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Carol"},
    ]
    for item in data:
        yield json.dumps(item) + "\n"  # NDJSON line
        time.sleep(1)  # wait 1 second between items


@router.get("/mystream")
def stream_ndjson():
    return StreamingResponse(stream_my_ndjson(), media_type="application/x-ndjson")


# -----


def stream_my_file():
    with open("large-video-file.mp4", mode="rb") as file:
        yield from file


@router.get("/mystream2")
def stream_file():
    return StreamingResponse(stream_my_file(), media_type="video/mp4")
