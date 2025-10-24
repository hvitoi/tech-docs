# istio_request_duration_milliseconds_sum

- It's a `DISTRIBUTION`, maps ranges of values to frequency

## Incoming requests

```conf
# average latency
sum (
  rate(
    istio_request_duration_milliseconds_sum{
      reporter="destination",
      destination_service="myapp-mesh.default.svc.cluster.local"
    }[$__rate_interval]
  )
)
/
sum (
  rate(
    istio_request_duration_milliseconds_count{
      reporter="destination",
      destination_service="myapp-mesh.default.svc.cluster.local"
    }[$__rate_interval]
  )
)
```

## Outgoing requests

```conf
sum (
  rate(
    istio_request_duration_milliseconds_sum{
      reporter="source",
      destination_service="myapp-mesh.default.svc.cluster.local"
    }[$__rate_interval]
  )
)
/
sum(
  rate(
    istio_request_duration_milliseconds_count{
      reporter="source",
      destination_service="myapp-mesh.default.svc.cluster.local"
    }[$__rate_interval]
  )
)
```
