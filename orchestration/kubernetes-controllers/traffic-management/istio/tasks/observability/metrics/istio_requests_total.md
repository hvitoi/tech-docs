# istio_requests_total

- It's a `COUNTER`, which is a  strictly increasing integer

## Incoming requests

```conf
# req/s
sum by (response_code) (
  rate(
    istio_requests_total{
      reporter="destination",
      destination_service="myapp-mesh.default.svc.cluster.local"
    }[$__rate_interval]
  )
)
```

## Outgoing requests

```conf
sum by (response_code) (
  rate(
    istio_requests_total{
      reporter="source",
      destination_service="anotherapp"
    }[$__rate_interval]
  )
)
```
