# Logs Insights

> Logs Insights requires Fluentd installed (via CloudWatch Observability Addon)

## EKS Log Groups

- `/aws/containerinsights/my-eks-cluster/application`
  - Workloads (pods) logs

- `/aws/containerinsights/my-eks-cluster/dataplane`
  - EKS control plane logs

- `/aws/containerinsights/my-eks-cluster/performance`
  - Performance logs. E.g., filesystem capacity

## Query

The query is run in for a specific log group (e.g., `/aws/containerinsights/my-eks-cluster/application`)

### Logs Insights QL

```shell
fields @timestamp, log, @entity.Attributes.K8s.Workload
| filter @entity.Attributes.K8s.Workload = "my-deploy"
| sort @timestamp desc
| limit 100
```

### OpenSearch PPL

- OpenSearch PPL (Piped Processing Language) is a query language used in `OpenSearch` for analyzing and transforming large datasets, particularly logs or time-series data.

```shell
fields `@timestamp`, `@message`, `@entity.Attributes.K8s.Workload`
| where `@entity.Attributes.K8s.Workload` = "my-deploy"
| sort - `@timestamp`
| head 100
```

### OpenSearch SQL

```sql
SELECT `@timestamp`, `@message`, `@entity.Attributes.K8s.Workload`
FROM `/aws/containerinsights/my-eks-cluster/application`
WHERE `@entity.Attributes.K8s.Workload` = "my-deploy"
ORDER BY `@timestamp` DESC
LIMIT 100;
```
