from fastapi import APIRouter, Response, status
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/response_path_operation_config",
    tags=["Response Path Operation Config"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    email: EmailStr | None = None
    tax: float = 10.5
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
def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# ---
# Output model as return type
@router.get("/items")
def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


# ---
# Output model as response_model param
@router.get(
    "/items2",
    response_model=list[Item],
    response_model_exclude_none=True,  # omit only the empty values
    response_model_exclude_unset=True,  # omit all the default values, not only those that are empty (nulls, empty lists, etc)
    response_model_include={
        "name",  # select the only fields to return in the response (won't work in this example because the return is a list)
    },
    response_model_exclude={
        "name",  # select the fields to exclude from the response (won't work in this example because the return is a list)
    },
)
async def read_items2():
    # The actual response is a list[dict], but the response_model is smart enough to know it's coersible to the list[Item] model
    # The same wouldn't be possible if you define the list[Item] model as the return type of the function
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


# ---

# Disable output model validation
# Disables it even though you have defined an output model


@router.get("/portal2", response_model=None)
async def get_portal2() -> Response:
    return {"message": "Here's your interdimensional portal."}
