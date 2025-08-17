from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/response_jsonresponse",
    tags=["Response JSONResponse"],
)


@router.get("/")
def get_resource() -> Response:
    return JSONResponse(
        content={"message": "Here's your interdimensional portal."}
    )  # needs to be wrapped in JSONResponse (plain dicts would fail on the return type)
