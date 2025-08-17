from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time
import json

router = APIRouter(
    prefix="/response_streamingresponse",
    tags=["Response StreamingResponse"],
)


def ndjson_stream():
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
    return StreamingResponse(ndjson_stream(), media_type="application/x-ndjson")
