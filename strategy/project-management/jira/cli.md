# Jira CLI

## /v1/alerts

- <https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/api-group-alerts/#api-v1-alerts-get>

```shell
CLOUD_ID=abcdefd3-e5f8-43ca-9eec-c382a5220bd9
BASIC_AUTH="$(cat auth.txt)"

curl -X GET "https://api.atlassian.com/jsm/ops/api/$ORG_ID/v1/alerts" \
  -H "Accept: application/json" \
  -H "Authorization: $BASIC_AUTH"
  # -U 'email@example.com:<api_token>'
  -d "from=1742312040000" \  # filter by createdAt
  -d "to=1742312642000" \    # filter by createdAt
  -d "sort=updatedAt" \
  -d "order=desc" \
  -d "size=10" \
```
