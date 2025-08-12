from typing import Annotated
from fastapi import APIRouter, Header
from pydantic import BaseModel

router = APIRouter(
    prefix="/headers",
    tags=["Headers"],
)

# Headers are the parameter whose type is annotated with Header()


@router.get("/items")
def read_items(
    user_agent: Annotated[
        str | None,
        Header(
            convert_underscores=True  # Change to False to prevent conversion from _ is converted to -
        ),
    ],
    x_token: Annotated[
        list[str], Header()  # The header X-Token can then be sent more than once
    ],
):
    return {
        "User-Agent": user_agent,
        "X-Token": x_token,
    }


class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@router.get("/items2")
async def read_items2(
    headers: Annotated[
        CommonHeaders,
        Header(
            convert_underscores=True,
        ),
    ],
):
    return headers
