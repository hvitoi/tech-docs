# Jira CLI

## /v1/alerts

```shell
CLOUD_ID=abcdefd3-e5f8-43ca-9eec-c382a5220bd9
BASIC_AUTH="$(cat auth.txt)"

curl -X GET "https://api.atlassian.com/jsm/ops/api/$ORG_ID/v1/alerts\
?from=1742312040000\
&to=1742312642000\
&sort=updatedAt\
&order=desc\
&size=10" \
  -H 'Accept: application/json' \
  -H "Authorization: $BASIC_AUTH" \
  -U 'email@example.com:<api_token>'
```
