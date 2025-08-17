from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


router = APIRouter(
    prefix="/sqlmodel",
    tags=["SQLModel"],
)


class HeroBase(SQLModel):
    name: str = Field(index=True)  # create an index table
    age: int | None = Field(default=None, index=True)  # INTEGER NULLABLE


class Hero(HeroBase, table=True):  # SQL table
    id: int | None = Field(default=None, primary_key=True)  # primary key
    secret_name: str


class HeroPublic(HeroBase):
    id: int


class HeroCreate(HeroBase):
    secret_name: str  # TEXT or VARCHAR


class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


## A SQLModel engine (underneath it's actually a SQLAlchemy engine) is what holds the connections to the database
sqlite_url = "sqlite:///sqlite_file_name"  # the relative root is where fastapi is the cwd where fastapi has started up
connect_args = {"check_same_thread": False}  # allow same DB in different threads
engine = create_engine(sqlite_url, connect_args=connect_args)


def register_startup_events(app):
    # On startup of the fastapi application run this function
    @app.on_event("startup")
    def on_startup():
        # create db and tables
        SQLModel.metadata.create_all(engine)


def get_session():
    # A "Session" is what stores the objects in memory and keeps track of any changes needed in the data
    # Then it uses the "Engine" to communicate with the database.
    with Session(engine) as session:
        yield session  # the rest of the function is executed (the close function called by "with" syntax) after the endpoint is done


SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    db_hero = Hero.model_validate(hero)

    # Puts hero in the Session's identity map as a pending row.
    # No SQL is sent yet.
    session.add(db_hero)

    # It does a "flush", that is: it takes all the pending inserts and send it to the db

    # BEGIN;
    #   INSERT INTO heroes (name, secret_name, age)
    #   VALUES (:name, :secret_name, :age);
    # COMMIT;
    session.commit()

    # Force re-reading the committed row to keep the row and the python object in sync
    # This is useful when the db automatically add default columns (timestamp, autoincrement, etc)

    # SELECT id, name, secret_name, age
    # FROM heroes
    # WHERE id = 1;
    session.refresh(db_hero)

    return hero


@router.get("/heroes/", response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: Annotated[int, Query()] = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    # SELECT * FROM heroes
    # LIMIT 100
    # OFFSET 0;
    query = select(Hero).offset(offset).limit(limit)
    # on the exec part, the query is executed! However it is only streamed from the database cursor when you tell it to!
    # exec returns an iterator, so that you can get the result from the database cursor little by little, however, no new query is executed, it is the streaming of the result of the initial query
    # .all(): load all the results into memory
    # .first(): load only the first result into memory
    # This way you can work with very large datasets without loading everything into RAM
    # Also, you can stream it, start processing rows as they arrive, instead of waiting for the entire query to finish
    heroes = session.exec(query).all()
    return heroes


@router.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(
    session: SessionDep,
    hero_id: Annotated[int, Path()],
):
    # SELECT *
    # FROM hero
    # WHERE id = <hero_id>
    hero = session.get(Hero, hero_id)  # Returns None if not found
    # hero = session.exec(select(Hero).where(Hero.id == hero_id)).first() # same
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.patch("/heroes/{hero_id}", response_model=HeroPublic)
def update_hero(
    session: SessionDep,
    hero_id: Annotated[int, Path()],
    hero: Annotated[HeroUpdate, Body()],
):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db


@router.delete("/heroes/{hero_id}")
def delete_hero(
    session: SessionDep,
    hero_id: Annotated[int, Path()],
):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    # session.delete() does not send request to the db yet, it just marks the object for deletion in the session
    # At this point, nothing has actually been removed from the database. The change is only staged in memory.
    session.delete(hero)

    # Commit actually send the deletion request to the database
    # DELETE FROM hero WHERE id = hero_id;
    # COMMIT;
    session.commit()
    return {"ok": True}
