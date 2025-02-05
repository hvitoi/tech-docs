# Prometheus API

```shell
set query "ALERTS%7Bservice%3D%7E%22bndes-client%22%7D"
set time "1738765048.314"

curl "http://localhost:9090/api/v1/query?query=$query&time=$time"
```

```json
{
  "status": "success",
  "data": {
    "resultType": "vector",
    "result": [
      {
        "metric": {
          "__name__": "ALERTS",
          "alertgroup": "service_lending_pj",
          "alertname": "service_is_down_ca87622864e4e45e0590ea146b9788781a6f325d",
          "alertstate": "firing",
          "aws_region": "us-east-1",
          "country": "br",
          "environment": "staging",
          "job": "kubernetes-pods",
          "monitor": "staging-global-green-vicmetrics-alert",
          "prototype": "global",
          "prototype_promxy": "global",
          "raw_name": "service_is_down",
          "service": "bndes-client",
          "severity": "warning",
          "squad": "lending-pj",
          "stack_id": "green"
        },
        "value": [
          1738765048.314,
          "1"
        ]
      }
    ]
  }
}
```
