from typing import Annotated
from fastapi import APIRouter, Form
from pydantic import BaseModel

# 'Content-Type: application/x-www-form-urlencoded'
# The way HTML forms (<form></form>) sends the data to the server normally uses a "special" encoding for that data, it's different from JSON.

router = APIRouter(
    prefix="/formdata",
    tags=["Form Data"],
)


@router.post("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    return {"username": username}


# ---


class MyForm(BaseModel):
    model_config = {"extra": "forbid"}
    username: str
    password: str


@router.post("/login2/")
async def login2(data: Annotated[MyForm, Form()]):
    return data
