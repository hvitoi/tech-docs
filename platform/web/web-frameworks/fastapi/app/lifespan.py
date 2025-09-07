from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine

from app.config import settings

# Define tasks to be executed at the application startup or shutdown


## --- DB Lifespan


def db_setup(app: FastAPI):
    ## A SQLModel engine (underneath it's actually a SQLAlchemy engine) is what holds the connections to the database
    engine = create_engine(
        settings.database_url,
        connect_args={"check_same_thread": False},  # allow same DB in different threads
    )
    SQLModel.metadata.create_all(engine)
    app.state.db_engine = engine


def db_teardown(app: FastAPI):
    app.state.db_engine.dispose()


## --- HTTP client Lifespan


def http_client_setup(app: FastAPI):
    app.state.http_client = httpx.AsyncClient()


async def http_client_teardown(app: FastAPI):
    await app.state.http_client.aclose()


## --- Lifespan


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup logic --- (e.g., connect to DB, initialize caches, etc.)
    db_setup(app)
    http_client_setup(app)

    yield

    # --- Shutdown logic --- (e.g., close DB, flush logs, cleanup)
    db_teardown(app)
    await http_client_teardown(app)
