from typing import Annotated
from fastapi import APIRouter, Header

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
    return {"User-Agent": user_agent}
