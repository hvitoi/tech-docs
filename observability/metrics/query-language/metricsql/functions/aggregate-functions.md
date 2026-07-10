# Aggregate functions

- <https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions>
- Aggregation operators can be used to aggregate all dimensions or preserve some dimensions

- `without`: removes the listed labels from the result vector
- `by`: drops labels not listed in the by clause

## group

- All values in the resulting vector are 1

```conf
# all distinct metrics given a certain label value
group({service="insurance-payments"}) by (__name__)
```

## sum

- `sum(q) by (group_labels)`
- Calculate sum over dimensions

```conf
sum(http_requests_total)
sum(http_requests_total) by (application, group)
sum(http_requests_total) without (instance)
```

## max

```shell
# Is my service up and/or scrapeable?
absent(up{kubernetes_name+"doccserver"}) or
sum(up{kubernetes_name="doccserver"})
== 0

# Do I have the number of LB I expect?
sum(up{kubernetes_name="loadbalancer"}) < 3

# Is out LB at 50% capacity in terms of sessions?
max(haproxy_frontend_current_sessions / haproxy_frontend_limit_sessions)
BY (kubernetes_node_name, frontend) * 100
> 50

# Are 50% of tests taking longer than 10min?
max(test_duration_seconds{quantile="0.5", result="pass"})
BY (test_name)
> 600
```

## count_values

- Count number of elements with the same value

```conf
count_values("version", build_version)
```

## topk

```conf
topk(5, http_requests_total)
```
