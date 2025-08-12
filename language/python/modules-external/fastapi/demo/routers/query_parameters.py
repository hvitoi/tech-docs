from fastapi import APIRouter

router = APIRouter(
    tags=["Query Parameters"],
)


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
