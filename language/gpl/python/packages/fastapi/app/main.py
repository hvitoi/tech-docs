from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute

from app.features import (  # or ".features"
    background_tasks,
    dependencies,
    dependency_oauth,
    encoders,
    exception_handlers,
    input_body,
    input_cookies,
    input_form_data,
    input_form_data_file,
    input_headers,
    input_path_parameters,
    input_query_parameters,
    models,
    path_operation_config,
    request_object,
    response_custom,
    response_file,
    response_generic,
    response_html,
    response_json,
    response_templates,
    response_object,
    response_plaintext,
    response_redirect,
    response_streaming,
    sqlmodel,
)

description = """
My API helps you do awesome stuff.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="Henry's App",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",  # with the identifier, url can be omitted
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    default_response_class=JSONResponse,  # Can be changed for example to XML
    # root_path="/api/v1", # same as the cli arg --root-path
    # openapi_url="/api/v1/openapi.json", # by default it is served under /openapi.json (or disable it completely with None)
    # docs_url="/documentation", # /docs by default
    # redoc_url=None, # /redoc by default
    # dependencies=[Depends(verify_token), Depends(verify_key)] # Add global dependencies
    lifespan=sqlmodel.lifespan,
)


@app.get("/")
async def read_root():  # path operation function
    return {"msg": "Hello World"}


# Include routers
app.include_router(input_query_parameters.router)
app.include_router(input_path_parameters.router)
app.include_router(input_body.router)
app.include_router(input_headers.router)
app.include_router(input_cookies.router)
app.include_router(input_form_data.router)
app.include_router(input_form_data_file.router)
app.include_router(models.router)
app.include_router(encoders.router)
app.include_router(dependencies.router)
app.include_router(dependency_oauth.router)
app.include_router(exception_handlers.router)
app.include_router(path_operation_config.router)
app.include_router(response_generic.router)
app.include_router(response_file.router)
app.include_router(response_html.router)
app.include_router(response_plaintext.router)
app.include_router(response_json.router)
app.include_router(response_redirect.router)
app.include_router(response_streaming.router)
app.include_router(response_templates.router)
app.include_router(response_custom.router)
app.include_router(response_object.router)
app.include_router(request_object.router)
app.include_router(sqlmodel.router)
app.include_router(background_tasks.router)

for route in app.routes:
    if isinstance(route, APIRoute):
        pass
        # route.operation_id = "lala" # modify route


# Run unicorn directly from the Python file. This is used to connect to the debugger in your IDE easily
# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
