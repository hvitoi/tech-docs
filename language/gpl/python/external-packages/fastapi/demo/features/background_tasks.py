from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Depends, Path


router = APIRouter(
    prefix="/background_tasks",
    tags=["Background Tasks"],
)


def write_log(message=""):
    # This function is executed after the response has been sent and the connection was closed
    with open("log.txt", mode="a") as email_file:
        # Creates the file at the cwd where python cmd was invoked
        email_file.write(message)


def authenticate_user(
    background_tasks: BackgroundTasks,
    email: Annotated[str, Path()],
):
    user_id = "123"
    message = f"User {user_id} ({email}) has been authenticated\n"
    background_tasks.add_task(write_log, message)  # Background task from a dependency
    return user_id


@router.post("/send-notification/{email}")
def send_notification(
    email: Annotated[str, Path()],
    background_tasks: BackgroundTasks,
    user_id: Annotated[str, Depends(authenticate_user)],
):
    background_tasks.add_task(
        write_log, message=f"A notification has been sent to {user_id} ({email})\n"
    )
    return {"message": "ok"}
