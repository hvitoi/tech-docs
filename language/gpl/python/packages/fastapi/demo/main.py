from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from demo.features import (  # or ".features"
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
    middleware,
    models,
    response_htmlresponse,
    response_jsonresponse,
    response_path_operation_config,
    response_redirectresponse,
    response_status_codes,
    response_streamingresponse,
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
app.include_router(response_path_operation_config.router)
app.include_router(response_htmlresponse.router)
app.include_router(response_jsonresponse.router)
app.include_router(response_redirectresponse.router)
app.include_router(response_streamingresponse.router)
app.include_router(response_status_codes.router)
app.include_router(sqlmodel.router)
app.include_router(background_tasks.router)

# Register custom exception handler for a given Exception

# app.add_exception_handler(
#     exception_handlers.MyException,
#     exception_handlers.my_exception_handler,
# )
# app.add_exception_handler(
#     HTTPException,
#     exception_handlers.http_exception_handler,
# )
# app.add_exception_handler(
#     RequestValidationError,
#     exception_handlers.request_validation_handler,
# )


# Register middlewares (apply to all routes)
# app.add_middleware(MyInnermostMiddleware)
# app.add_middleware(MyOutermostMiddleware)
app.add_middleware(middleware.ProcessTimeMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=middleware.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static Files: Navigate to <origin>/myfiles/image.png
# app.mount(
#     "/myfiles",
#     # The relative directory refers to the same where the python command was run
#     StaticFiles(directory="static"),
#     name="myawesomefiles",  # name used internally by FastAPI
# )

# Run unicorn directly from the Python file.
# This is used to connect to the debugger in your IDE easily
# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
