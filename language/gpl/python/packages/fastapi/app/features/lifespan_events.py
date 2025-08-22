from contextlib import asynccontextmanager

# Define tasks to be executed at the application startup or shutdown


class MockFastAPI:
    lifespan = None


# On startup of the fastapi application run this function
@asynccontextmanager
async def lifespan(app: MockFastAPI):
    # --- Startup logic ---
    print("🚀 App is starting up...")
    # e.g., connect to DB, initialize caches, etc.
    # SQLModel.metadata.create_all(engine)  # startup
    yield
    # --- Shutdown logic ---
    print("🛑 App is shutting down...")
    # e.g., close DB, flush logs, cleanup


app = MockFastAPI(
    lifespan=lifespan,
)
