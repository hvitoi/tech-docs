from fastapi import FastAPI
from features import (
    cookies,
    form_data,
    form_data_file,
    headers,
    multiple_models,
    path_parameters,
    query_parameters,
    request_body,
    response,
    status_codes,
    exception_handlers,
    path_operation_config,
    encoders,
)

app = FastAPI()


@app.get("/")
async def read_root():  # path operation function
    return {"foo": "bar"}


# Include routers
app.include_router(path_parameters.router)
app.include_router(query_parameters.router)
app.include_router(request_body.router)
app.include_router(headers.router)
app.include_router(cookies.router)
app.include_router(response.router)
app.include_router(multiple_models.router)
app.include_router(status_codes.router)
app.include_router(form_data.router)
app.include_router(form_data_file.router)
app.include_router(exception_handlers.router)
app.include_router(path_operation_config.router)
app.include_router(encoders.router)

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
