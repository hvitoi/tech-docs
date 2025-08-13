from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/responses",
    tags=["Responses"],
)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    email: EmailStr | None = None
    tax: float = 10.5
    tags: list[str] = []


# ---
# Output model as return type
@router.get("/items")
async def read_items() -> list[Item]:
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

# Input/Output models


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@router.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# ---
# Generic Response

# RedirectResponse and JSONResponse are subclasses of Response


@router.get("/portal")
def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(
        content={"message": "Here's your interdimensional portal."}
    )  # needs to be wrapped in JSONResponse (plain dicts would fail on the return type)


# ---
# HTMLResponse
@router.get("/htmlresponse")
async def html_response():
    content = """
<body>
    <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)


# ---

# Disable output model validation
# Disables it even though you have defined an output model


@router.get("/portal2", response_model=None)
async def get_portal2() -> Response:
    return {"message": "Here's your interdimensional portal."}
