# SQLite ORM integrations

## Connection URLs (DSN)

- The "host" segment is empty, so the path starts after `///` — hence the **four** slashes for absolute paths

```txt
sqlite:///relative/path.db      # SQLAlchemy, relative
sqlite:////abs/path/to.db       # SQLAlchemy, absolute (4 slashes)
sqlite://                       # SQLAlchemy, in-memory
sqlite+aiosqlite:///app.db      # SQLAlchemy async
file:app.db?mode=ro             # SQLite URI filename, read-only
file::memory:?cache=shared      # shared in-memory across connections
```

## SQLAlchemy

```python
from sqlalchemy import create_engine, ForeignKey, event
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase): ...

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))

engine = create_engine("sqlite:///app.db", echo=True)

@event.listens_for(engine, "connect")
def _pragmas(dbapi_con, _):
    dbapi_con.execute("PRAGMA foreign_keys=ON")
    dbapi_con.execute("PRAGMA journal_mode=WAL")

Base.metadata.create_all(engine)

with Session(engine) as s, s.begin():
    s.add(Book(title="Ficciones", author_id=1))
```

- `StaticPool` + `check_same_thread=False` is the usual recipe for `:memory:` in tests, otherwise each connection gets its own empty db
- Alembic migrations work, but SQLite has **no real `ALTER TABLE`** — use `render_as_batch=True` so Alembic does copy-and-swap

## SQLModel

- SQLAlchemy + Pydantic (same URLs/engine), the default pairing with FastAPI

```python
from sqlmodel import Field, SQLModel, create_engine, Session

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str

engine = create_engine("sqlite:///app.db", connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)
```

## Django

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {"init_command": "PRAGMA journal_mode=WAL; PRAGMA synchronous=NORMAL;",
                    "transaction_mode": "IMMEDIATE"},   # Django 5.1+
    }
}
```

- Django's default project DB; enables FK enforcement itself
- Since 5.1 the SQLite options above make it viable in production for modest write loads

## Peewee

```python
from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase("app.db", pragmas={"journal_mode": "wal", "foreign_keys": 1})

class Book(Model):
    title = CharField()
    class Meta: database = db
```

- Lightest option; `playhouse.sqlite_ext` exposes FTS5, JSON1, closure tables

## Node / TypeScript

```txt
better-sqlite3   # synchronous, fastest, the default choice
node:sqlite      # built into Node 22+ (experimental)
Prisma           # datasource db { provider = "sqlite"  url = "file:./dev.db" }
Drizzle          # drizzle-orm/better-sqlite3, also targets Turso/D1
```

## Hosted / distributed SQLite

- `Turso` / `libSQL` — SQLite fork with a server mode + replicas (`libsql://...`)
- `Cloudflare D1` — SQLite at the edge
- `Litestream` — streams WAL to S3 for continuous backup
- `LiteFS` — FUSE-based replication (Fly.io)
