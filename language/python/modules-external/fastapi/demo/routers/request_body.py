from typing import Annotated
from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter(
    tags=["Request Body"],
)

# Request body is the parameter whose type is annotated with Body()
# Or it can be inferred: the parameter is associated with a Pydantic model


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/")
def create_item(item: Annotated[Item, Body()]):  # item=Body() <-- deprecated syntax
    return item


@router.put("/items/{item_id}")
def update_item(
    # FastAPI automatically recognizes what is a path parameter, what is a request body and what is a query string
    item_id: int,  # path parameter: the parameter name that matches with a string in the path
    item: Item,  # request body: the parameter name that is associated with a Pydantic model
    q: str,  # query string: everything else
):
    return {
        "item_id": item_id,
        "q": q,
        **item.model_dump(),
    }
