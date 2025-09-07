from fastapi import APIRouter, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/response_jsonresponse",
    tags=["JSONResponse"],
)


@router.get("/")
def get_resource() -> Response:
    # Building and returning a JSONResponse manually does not coerce the response against the model (it will be returned directly)
    # But you can apply jsonable_encoder to it before returning
    payload = jsonable_encoder({"message": "Here's your interdimensional portal."})

    # needs to be wrapped in JSONResponse (plain dicts would fail on the return type)
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=payload)
