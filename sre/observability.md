# Observability

- Trace the request through multiple services
- The more `observable` a system is, the more `controllable` it is
- 3 pillars of observability
  - **Metrics**
  - **Logging**
  - **Tracing**

## Metrics

- Metrics are `numeric representation of data` measured over intervals of time
- Analytics Data and Metrics about the running services within an application
- 4 golden signals

  - `latency`: time to serve a request
  - `traffic`: requests/s
  - `error`: error rate of requests
  - `saturation`: fullness of a service

- A `threshold` is an objetive that should not be trespassed
- Ideally the current `state` must not reach the threshold

```sh
# Is my service up and/or scrapeable?
absent(up{kubernetes_name+"doccserver"}) or
sum(up{kubernetes_name="doccserver"})
== 0
```

```sh
# Do I have the number of LB I expect?
sum(up{kubernetes_name="loadbalancer"}) < 3
```

```sh
# Is out LB at 50% capacity in terms of sessions?
max(haproxy_frontend_current_sessions / haproxy_frontend_limit_sessions)
BY (kubernetes_node_name, frontend) * 100
> 50
```

```sh
# Are 50% of tests taking longer than 10min?
max(test_duration_seconds{quantile="0.5", result="pass"})
BY (test_name)
> 600
```

## Logging

- Log is a `immutable`, `timestamped` record of `discrete events` that happened over time

## Tracing

- Trace is a representation of a series of causally related distributed events
- Shows the `end-to-end request flow` through a distributed system
