# Prometheus API

- It's an API standard
- It's adopted by `Prometheus Server` and `VictoriaMetrics` (vmselect)

## Query API

- The resultType is a `vector`

- **query**
  - The promql query

- **time**
  - The moment at which it will be returned the time series that were scraped at that moment
  - Defaults to now (server's clock). That is: returns the time series present at the latest scrape (within the staleness window, usually 5m)

- **max_lookback** (VM only)
  - The query respects the `staleness window`. It's how further the query will walk backward to find the latest sample of a given time series
  - There is a server default of 5 min, that can be overridden with this parameter
  - Example: if the pod died 2 minutes ago, its last sample is still within the 5m window, the latest sample will show up in the query, still reporting whatever value it had at death
  - Prometheus also writes a special `stale marker` (NaN value) into that series immediately when the scrape target disappears from service discovery. This force the this series to stop showing up in instant queries faster than the full 5m staleness window

```shell
HOST='host'
QUERY='services_http_requests_total{service="ronaldo",path="/api/version"}'

curl -sX POST "$HOST/api/v1/query" \
  --data-urlencode "query=$QUERY"
  # --data-urlencode "time=1738765048.314"
  # --data-urlencode "max_lookback=1h"
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

- The resultType is a `matrix`

```shell
HOST='host'
QUERY='services_http_requests_total{service="ronaldo",path="/api/version"}'

curl -sX POST "$HOST/api/v1/query_range" \
  --data-urlencode "query=$QUERY" \
  --data-urlencode "start=$(date -u -d '5 min ago' +%s)" \
  --data-urlencode "end=$(date -u +%s)" \
  --data-urlencode "step=15s" | jq
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
            1783978236,
            "1762"
          ],
          [
            1783978251,
            "1768"
          ],
          [
            1783978266,
            "1768"
          ],
          [
            1783978281,
            "1774"
          ],
          [
            1783978296,
            "1774"
          ],
          [
            1783978311,
            "1780"
          ],
          [
            1783978326,
            "1780"
          ],
          [
            1783978341,
            "1786"
          ],
          [
            1783978356,
            "1786"
          ],
          [
            1783978371,
            "1792"
          ],
          [
            1783978386,
            "1792"
          ],
          [
            1783978401,
            "1798"
          ],
          [
            1783978416,
            "1798"
          ],
          [
            1783978431,
            "1804"
          ],
          [
            1783978446,
            "1804"
          ],
          [
            1783978461,
            "1810"
          ],
          [
            1783978476,
            "1810"
          ],
          [
            1783978491,
            "1816"
          ],
          [
            1783978506,
            "1816"
          ],
          [
            1783978521,
            "1816"
          ],
          [
            1783978536,
            "1816"
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
            1783978236,
            "2147"
          ],
          [
            1783978251,
            "2147"
          ],
          [
            1783978266,
            "2153"
          ],
          [
            1783978281,
            "2153"
          ],
          [
            1783978296,
            "2159"
          ],
          [
            1783978311,
            "2159"
          ],
          [
            1783978326,
            "2165"
          ],
          [
            1783978341,
            "2165"
          ],
          [
            1783978356,
            "2171"
          ],
          [
            1783978371,
            "2171"
          ],
          [
            1783978386,
            "2177"
          ],
          [
            1783978401,
            "2177"
          ],
          [
            1783978416,
            "2183"
          ],
          [
            1783978431,
            "2183"
          ],
          [
            1783978446,
            "2189"
          ],
          [
            1783978461,
            "2189"
          ],
          [
            1783978476,
            "2195"
          ],
          [
            1783978491,
            "2195"
          ],
          [
            1783978506,
            "2201"
          ],
          [
            1783978521,
            "2201"
          ],
          [
            1783978536,
            "2201"
          ]
        ]
      }
    ]
  },
  "stats": {
    "seriesFetched": "2",
    "executionTimeMsec": 5
  }
}
```
