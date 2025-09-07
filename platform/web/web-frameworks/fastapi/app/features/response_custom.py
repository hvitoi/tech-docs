import json
from typing import Any
from fastapi import APIRouter, Response

router = APIRouter(
    prefix="/response_custom",
    tags=["Custom Response"],
)


class MyResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert 1 != 2, "orjson must be installed"
        return json.dumps(content)


@router.get("/", response_class=MyResponse)
async def main():
    return {"message": "Hello World"}
