# Victoriametrics API

## Query API

```shell
HOST='host'
QUERY='services_http_requests_total{service="ronaldo",path="/api/version"}'

curl -X POST "$HOST/query_range" --data-urlencode "query=$QUERY"
```

```json
// Response
{
  "status": "success",
  "isPartial": false,
  "data": {
    "resultType": "vector",
    "result": [
      // Returns 2 time series, because there were 2 time series (one for each pod) at the latest scrape
      {
        "metric": {
          "__name__": "services_http_requests_total",
          "aws_region": "us-east-2",
          "environment": "prod",
          "kubernetes_pod_name": "ronaldo-5975f7c77d-7kktn",
          "method": "get",
          "path": "/api/version",
          "service": "ronaldo",
          "status": "200",
        },
        "value": [
          1783977321, // the timestamp of the scrape
          "1576" // value (the counter) on that scrape
        ]
      },
      {
        "metric": {
          "__name__": "services_http_requests_total",
          "aws_region": "us-east-2",
          "environment": "prod",
          "kubernetes_pod_name": "ronaldo-5975f7c77d-ftrnw",
          "method": "get",
          "path": "/api/version",
          "service": "ronaldo",
          "status": "200",
        },
        "value": [
          1783977321, // the timestamp of the scrape
          "1959" // value (the counter) on that scrape
        ]
      }
    ]
  },
  "stats": {
    "seriesFetched": "2",
    "executionTimeMsec": 8
  }
}
```

## Query Range API

```shell
HOST='host'
QUERY='services_http_requests_total{service="ronaldo",path="/api/version"}'

curl -X POST "$HOST/query_range" --data-urlencode "query=$QUERY"
```

```json
// Response
{
  "status": "success",
  "isPartial": false,
  "data": {
    "resultType": "matrix",
    "result": [
      {
        "metric": {
          "__name__": "services_http_requests_total",
          "aws_region": "us-east-2",
          "environment": "prod",
          "kubernetes_pod_name": "prod-global-blue-ronaldo-deployment-5975f7c77d-7kktn",
          "method": "get",
          "path": "/api/version",
          "service": "ronaldo",
          "status": "200",
        },
        "values": [
          [
            1783977106,
            "1540"
          ],
          [
            1783977406,
            "1600"
          ]
        ]
      },
      {
        "metric": {
          "__name__": "services_http_requests_total",
          "aws_region": "us-east-2",
          "environment": "prod",
          "kubernetes_pod_name": "prod-global-blue-ronaldo-deployment-5975f7c77d-ftrnw",
          "method": "get",
          "path": "/api/version",
          "service": "ronaldo",
          "status": "200",
        },
        "values": [
          [
            1783977106,
            "1919"
          ],
          [
            1783977406,
            "1983"
          ]
        ]
      }
    ]
  },
  "stats": {
    "seriesFetched": "2",
    "executionTimeMsec": 2
  }
}
```
