from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from demo.features import (  # or ".features"
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
    background_tasks,
    response_path_operation_config,
    response_htmlresponse,
    response_jsonresponse,
    response_redirectresponse,
    response_status_codes,
    response_streamingresponse,
    sqlmodel,
)

app = FastAPI()
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)]) # Add global dependencies


@app.get("/")
async def read_root():  # path operation function
    return {"foo": "bar"}


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

# Register Events
sqlmodel.register_startup_events(app)
