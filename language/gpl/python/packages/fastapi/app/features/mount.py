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

# -------- Sub App

## Mount a completely independent sub app under a path

subapi = None  # FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
