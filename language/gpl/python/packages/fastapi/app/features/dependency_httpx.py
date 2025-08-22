from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from httpx import AsyncClient

router = APIRouter(
    prefix="/dependency_httpx",
    tags=["Dependency HTTPX"],
)


async def get_http_client(request: Request) -> AsyncClient:
    return request.app.state.http_client


@router.get("/repo_stat")
async def get_repo_stats(
    repo: Annotated[str, Query()],
    http_client: Annotated[AsyncClient, Depends(get_http_client)],
):
    url = f"https://api.github.com/repos/{repo}"
    response = await http_client.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Repo not found or GitHub API error",
        )

    data = response.json()
    return data
