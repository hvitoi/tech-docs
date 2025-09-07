from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix="/responseobject",
    tags=["Temporal Response Object"],
)


## ----- Cookies


@router.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}


## ----- Headers


@router.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}


## ---- Status Codes


# fastapi.status are just convenience variables to the integer of a status code
@router.post("/items/{name}", status_code=status.HTTP_200_OK)
def create_item(response: Response):
    # override the default status code defined by the "status_code" path operation config
    # it's not common to change the http status code like that, you will usually raise an HTTPException
    response.status_code = status.HTTP_201_CREATED
    return {"message": "Hello World"}

    # you can also change the response status code by building a JSONResponse object
    # return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"message": "Hello World"})
