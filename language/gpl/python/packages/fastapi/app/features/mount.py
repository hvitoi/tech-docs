from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

app = None  # Mocked FastAPI app

# Mounting" means adding a completely "independent" application in a specific path, that then takes care of
# handling everything under that path, with the path operations declared in that sub-application.

# -------- Static Files

# Static Files: Navigate to <origin>/myfiles/image.png

app.mount(
    # sub path
    "/myfiles",
    # The relative directory refers to the same where the python command was run
    StaticFiles(directory="static"),
    name="myawesomefiles",  # name used internally by FastAPI
)

# -------- SubApp (FastAPI)

## Mount a completely independent sub app under a path

subapp = None  # FastAPI()


@subapp.get("/subapp_fastapi")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapp)

# -------- SubApp (Flask, Django)

subapp_flask = None  # Flask(__name__)

app.mount("/subapp_flask", WSGIMiddleware(subapp_flask))
