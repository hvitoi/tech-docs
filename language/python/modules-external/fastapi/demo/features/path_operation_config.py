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
    # tags=["foo"],
    summary="Create an item",
    description="This description overrides the function docstring",
    response_description="The created item",
    deprecated=True,
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
