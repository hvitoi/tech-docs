# gh api

```shell
gh api --silent \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "orgs/nubank/teams/my-team"

curl -Lsf \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $token" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/nubank/teams/my-team
```
