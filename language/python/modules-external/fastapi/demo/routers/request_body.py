from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    tags=["Request Body"],
)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/")
def create_item(item: Item):
    return item


@router.put("/items/{item_id}")
def update_item(
    # FastAPI automatically recognizes what is a path parameter, what is a request body and what is a query string
    item_id: int,  # path parameter: the parameter name that matches with a string in the path
    item: Item,  # request body: the parameter name that is associated with a Pydantic model
    myqs1: str,  # query string: everything else
    myqs2: str,  # query string: everything else
):
    return {
        "item_id": item_id,
        **item.model_dump(),
    }
