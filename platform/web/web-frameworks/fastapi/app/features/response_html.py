from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/response_html",
    tags=["HTMLResponse"],
)


# When a response_class is define, you don't need to build the Response object
# This also sets the Content-Type
@router.get("/", response_class=HTMLResponse)
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
    # return HTMLResponse(content=content) # without response_class
    return content  # simpler with response_class
