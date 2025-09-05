# Operators

- <https://prometheus.io/docs/prometheus/latest/querying/operators/>

## Binary Operator

### Arithmetic

```promql
+ #(addition)
- #(subtraction)
* #(multiplication)
/ #(division)
% #(modulo)
^ #(power/exponentiation)
```

### Trigonometric

```promql
atan2
```

### Comparison

```promql
== (equal)
!= (not-equal)
> (greater-than)
< (less-than)
>= (greater-or-equal)
<= (less-or-equal)
```

### Logical

```promql
and #(intersection)
or #(union)
unless #(complement)
```

## Vector matching

- **ignoring**
- **group_left**
- **group_right**

## Aggregation

- Aggregation operators can be used to aggregate all dimensions or preserve some dimensions using
  - `without`: removes the listed labels from the result vector
  - `by`: drops labels not listed in the by clause

- **sum**: calculate sum over dimensions
- **min**: select minimum over dimensions
- **max**: select maximum over dimensions
- **avg**: calculate the average over dimensions
- **group**: all values in the resulting vector are 1
- **stddev**: calculate population standard deviation over dimensions
- **stdvar**: calculate population standard variance over dimensions
- **count**: count number of elements in the vector
- **count_values**: count number of elements with the same value
- **bottomk**: smallest k elements by sample value
- **topk**: largest k elements by sample value
- **quantile**: calculate φ-quantile (0 ≤ φ ≤ 1) over dimensions

```conf
sum without (instance) (http_requests_total)
sum by (application, group) (http_requests_total)

sum(http_requests_total)

count_values("version", build_version)

topk(5, http_requests_total)

# all distinct metrics given a certain label value
group({service="insurance-payments"}) by (__name__)
```
