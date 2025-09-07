from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix="/response_generic",
    tags=["Response"],
)


@router.get("/")
def get_resource() -> Response:
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    response = Response(
        content=data,
        media_type="application/xml",
        status_code=status.HTTP_201_CREATED,
        headers={},
    )
    # You can access the built response just like a temporal response object
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response
