from fastapi import APIRouter, HTTPException, Response, status
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/statuscodes",
    tags=["Response Status Codes"],
)

# fastapi.status are just convenience variables to the integer of a status code


@router.post(
    "/items/{name}",
    status_code=status.HTTP_200_OK,  # defines the default status code (but can be overridden)
)
def create_item(
    response: Response,  # The temporal response
    name: str,
    foo: bool = False,
):
    if foo:
        # it's not common to change the http status code like that, you will usually raise an HTTPException
        response.status_code = status.HTTP_201_CREATED
        return {"name": name}

    # you can also change the response status code by building a JSONResponse object
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"name": name})


## -- Raise HTTPException


@router.get("/items/{item_id}")
async def raise_http_exception(item_id: str):
    items = {"a": 1, "b": 2, "c": 3}
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},  # extra headers
        )
    return {"item": items[item_id]}
