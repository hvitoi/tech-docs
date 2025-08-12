from typing import Annotated
from fastapi import APIRouter, Cookie

router = APIRouter(
    prefix="/cookies",
    tags=["Cookies"],
)

# Cookies are the parameter whose type is annotated with Cookie()


@router.get("/items")
def read_items(ads_id: Annotated[str | None, Cookie()]):
    return {"ads_id": ads_id}
