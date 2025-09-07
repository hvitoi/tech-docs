from datetime import datetime

from pydantic import BaseModel


app = None

# Just like callbacks, webhooks are just a way to document on OpenAPI that your program supports webhooks (the events and models)
# The actual logic to handle webhooks is up to you


class User(BaseModel):
    username: str
    monthly_fee: float
    start_date: datetime


# "user-created" is an identified for the webhook. it's usually represented by an Event
# The client needs to define the URL in which he wants to receive this webhook request
@app.webhooks.post("user-created")
def user_created(body: User):
    """
    When a new user subscribes to your service we'll send you a POST request with this
    data to the URL that you register for the event `user-created` in the dashboard.
    """
    pass
