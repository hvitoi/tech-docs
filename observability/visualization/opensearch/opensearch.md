# OpenSearch

## OpenSearch PPL

- OpenSearch PPL (Piped Processing Language) is a query language used in `OpenSearch` for analyzing and transforming large datasets, particularly logs or time-series data.

```shell
fields `@timestamp`, `@message`, `@entity.Attributes.K8s.Workload`
| where `@entity.Attributes.K8s.Workload` = "my-deploy"
| sort - `@timestamp`
| head 100
```

## OpenSearch SQL

```sql
SELECT `@timestamp`, `@message`, `@entity.Attributes.K8s.Workload`
FROM `/aws/containerinsights/my-eks-cluster/application`
WHERE `@entity.Attributes.K8s.Workload` = "my-deploy"
ORDER BY `@timestamp` DESC
LIMIT 100;
```
