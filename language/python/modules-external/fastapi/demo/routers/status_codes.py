from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix="/statuscodes",
    tags=["Status Codes"],
)

# fastapi.status are just convenience variables to the integer of a status code


@router.post(
    "/items/{name}",
    status_code=status.HTTP_201_CREATED,  # defines the default status code (but can be overridden)
)
def create_item(
    response: Response,  # The temporal response
    name: str,
    force_failure: bool = False,
):
    if force_failure:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
    return {"name": name}
