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

## count_values

- Count number of elements with the same value

```conf
count_values("version", build_version)
```

## topk

```conf
topk(5, http_requests_total)
```
