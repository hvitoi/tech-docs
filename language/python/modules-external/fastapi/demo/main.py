from fastapi import FastAPI
from routers import path_parameters, query_parameters, request_body

app = FastAPI()


@app.get("/")
async def read_root():
    return {"foo": "bar"}


# Include routers
app.include_router(path_parameters.router)
app.include_router(query_parameters.router)
app.include_router(request_body.router)
