from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/response_htmlresponse",
    tags=["Response HTMLResponse"],
)


@router.get("/")
def get_resource() -> Response:
    content = """
<body>
    <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)
