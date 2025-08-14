# %%
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime = datetime.now()
    friends: list[int] = []


external_data = {"id": "123", "name": "Henry"}

user = User(**external_data)

user_updated = user.model_copy(update={"name": "John"})
user_updated
