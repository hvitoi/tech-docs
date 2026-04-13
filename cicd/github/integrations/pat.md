# Auth

## Personal Access Token (PAT)

- <https://github.com/settings/personal-access-tokens>
- Used for human users, from a script
- It's a static token tied to your personal account
- There's also the classic non-fine-grained tokens: <https://github.com/settings/tokens>
- With that, the API sees the request as you, same permissions, same rate limits (5,000 req/hr), same audit trail.

```shell
curl -Lsf \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GH_PAT" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user
```

## GITHUB_TOKEN

- Auto-provisioned inside a GitHub Actions job
- Scoped to the repository that triggered the workflow
- Expires when the job finishes

```yaml
# .github/workflows/example.yaml
jobs:
  api-call:
    runs-on: ubuntu-latest
    steps:
      - name: Call GitHub API
        run: |
          curl -Lsf \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${{ secrets.GITHUB_TOKEN }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/${{ github.repository }}/issues
```
