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

# %%
# convert to dict and include the default values
user.model_dump()

# %%
# Do not include "friends" and "signup_ts", since they were not set by the user
user.model_dump(exclude_unset=True)
