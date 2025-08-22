from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/response_templates",
    tags=["Response Templates"],
)


templates = Jinja2Templates(directory="templates")


@router.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"id": id},
    )


### templates/item.html

# <html>
# <head>
#   <title>Item Details</title>
#   <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">
# </head>
# <body>
#   <h1><a href="{{ url_for('read_item', id=id) }}">Item ID: {{ id }}</a></h1>
# </body>
# </html>
