from typing import Annotated
from fastapi import APIRouter, Cookie
from pydantic import BaseModel

router = APIRouter(
    prefix="/cookies",
    tags=["Input Cookies"],
)

# Cookies are the parameter whose type is annotated with Cookie()


@router.get("/items")
def read_items(ads_id: Annotated[str | None, Cookie()]):
    return {"ads_id": ads_id}


class MyCookies(BaseModel):
    model_config = {"extra": "forbid"}  # control exactly what cookies you can receive

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@router.get("items2")
def read_items2(cookies: Annotated[MyCookies, Cookie()]):
    return cookies
