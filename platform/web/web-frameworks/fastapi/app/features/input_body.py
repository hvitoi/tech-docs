from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Body
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter(
    prefix="/requestbody",
    tags=["Input Body"],
)

# Request body is the parameter whose type is annotated with Body()
# Or it can be inferred: the parameter is associated with a Pydantic model


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    item_id: UUID
    started_at: datetime
    ended_at: datetime
    process_after: timedelta
    repeat_at: time | None
    name: str
    description: str | None = Field(  # Field accepts the same args as Body()
        default=None,  # default values are passed like this when Field validations are necessary
        title="The description of the item",
        max_length=300,
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero",
        examples=[1.99],  # you can define inline examples
    )
    tax: float | None = None
    image: list[Image] | None = None
    weights: dict[int, float]  # arbitrary dict (flexible model)

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            # Explicitly define an example, instead of OpenAPI's auto-generated ones
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        },
    }


class User(BaseModel):
    username: str
    full_name: str | None = None


# --- Annotated Body
@router.post("/items/")
def create_item(
    item: Annotated[  # item=Body() <-- deprecated syntax
        Item,
        Body(
            embed=True,  # this body is expected to be passed in a nested key. {"item": <item>}
        ),
    ],
):
    return item


# --- Inferred Body
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


# --- Multiple RequestBody models


@router.post("/items2")
def update_items2(
    item: Item,
    user: User,
    importance: Annotated[int, Body()],
):
    # when there are multiple models, they are expected together in a single map. E.g., {"user": ..., "item": ..., "importance": ...}
    return {
        "item": item,
        "user": user,
        "importance": importance,
    }
