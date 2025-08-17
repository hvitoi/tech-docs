# %%
from datetime import timedelta, datetime

started_at: datetime = datetime.fromisoformat("2025-07-01 12:00")
duration: timedelta = timedelta(hours=6)

ended_at = started_at + duration
ended_at
