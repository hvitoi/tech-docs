# Jira CLI

## /v1/alerts

- <https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/api-group-alerts/#api-v1-alerts-get>
- Query Params
  - `to/from`: Unix epoch (milliseconds) used to filter by "createdAt"
  - `query`

```shell
CLOUD_ID=abc390d3-e5f8-43ca-9eec-c382a5220b00
BASIC_AUTH="$(cat ~/auth_jira.txt)"

Q_FROM=1773847141696
Q_TO=1773847141696
Q_SORT=updatedAt
Q_ORDER=desc
Q_SIZE=10
Q_QUERY='updatedAt>=1773854061285%20AND%20updatedAt<=1773854061285'

curl -s -X GET "https://api.atlassian.com/jsm/ops/api/$CLOUD_ID/v1/alerts?from=$Q_FROM&to=$Q_TO&sort=$Q_SORT&order=$Q_ORDER&size=$Q_SIZE&query=$Q_QUERY" \
  -H "Authorization: $BASIC_AUTH" | jq
```

## /v1/alerts/:id

```shell
CLOUD_ID=abc390d3-e5f8-43ca-9eec-c382a5220b00
BASIC_AUTH="$(cat ~/auth_jira.txt)"
ALERT_ID=b4c8d5b7-059e-4e9a-a724-3698ba1f6b0d-1773847141696

curl -s -X GET "https://api.atlassian.com/jsm/ops/api/$CLOUD_ID/v1/alerts/$ALERT_ID" \
  -H "Authorization: $BASIC_AUTH" | jq
```
