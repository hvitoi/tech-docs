from fastapi import FastAPI
from routers import (
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
)

app = FastAPI()


@app.get("/")
async def read_root():
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
