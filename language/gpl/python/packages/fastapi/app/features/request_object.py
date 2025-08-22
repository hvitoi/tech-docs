from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/requestobject",
    tags=["Request Object"],
)


@router.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    root_path = request.scope.get("root_path")
    return {
        "client_host": client_host,
        "item_id": item_id,
        "root_path": root_path,  # you can change the prefix with --root-path cli arg
    }
