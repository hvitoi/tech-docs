from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@router.get("/items/{item_id}")
def read_item(
    item_id: int,  # path parameter
    # query parameters are everything that do not match with a path parameter
    q1: int | None = None,  # query parameter
    q2: bool | None = None,  # query parameter (accepts True, true, 1, on, yes)
):
    return {
        "item_id": item_id,
        "q1": q1,
        "q2": q2,
    }


@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_id": item_id,
    }
