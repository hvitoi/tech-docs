from enum import Enum
from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(
    prefix="/pathparameters",
    tags=["Path Parameters"],
)

# Path parameters are the parameter whose type is annotated with Path()
# Or it can be inferred: its variable name is contained in the path


class Color(int, Enum):
    red = 1
    blue = 2
    green = 3


@router.get("/colors/{color}")
def read_model(color: Color):
    return {"color": color}


@router.get("/items/{item_id}")
def read_items(
    item_id: Annotated[
        int,
        Path(
            title="The ID of the item to get",
            ge=1,  # validation
            le=1000,  # validation
        ),
    ],
):
    return {"item_id": item_id}
