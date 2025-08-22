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
    return Response(
        content=data,
        media_type="application/xml",
        status_code=status.HTTP_201_CREATED,
        headers={},
    )
