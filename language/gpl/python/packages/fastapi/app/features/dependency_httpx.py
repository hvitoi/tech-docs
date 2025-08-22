from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from httpx import AsyncClient

router = APIRouter(
    prefix="/dependency_httpx",
    tags=["Dependency HTTPX"],
)


async def get_http_client(request: Request) -> AsyncClient:
    async with request.app.state.http_client as client:
        return client


@router.get("/repo_stat")
async def get_repo_stats(
    repo: Annotated[str, Query()],
    client: Annotated[AsyncClient, Depends(get_http_client)],
):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Repo not found or GitHub API error",
        )

    data = response.json()
    return {
        "full_name": data.get("full_name"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "open_issues": data.get("open_issues_count"),
    }
