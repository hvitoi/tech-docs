from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/pathoperationconfig",
    tags=["Path Operation Configuration"],
)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@router.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
)
async def create_item(item: Item):
    return item
