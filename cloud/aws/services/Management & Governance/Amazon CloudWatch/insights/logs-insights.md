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

#### At application log group

```shell
fields @timestamp, log, @entity.Attributes.K8s.Workload
| filter @entity.Attributes.K8s.Workload = "my-deploy"
| sort @timestamp desc
| limit 100
```

```shell
# Application log errors by container name
stats count() as countoferrors by kubernetes.container_name
| filter stream="stderr"
| sort countoferrors desc
```

#### At performance log group

```shell
# Average node CPU utilization
stats avg(node_cpu_utilization) as avg_node_cpu_utilization by NodeName
| sort avg_node_cpu_utilization DESC
```

```shell
# Average container restarts
stats avg(number_of_container_restarts) as avg_number_of_container_restarts by PodName
| sort avg_number_of_container_restarts DESC
```

```shell
# Average node failures
stats avg(cluster_failed_node_count) as avg_node_failures
| filter Type="Cluster"
| sort @timestamp desc
```

```shell
# Percentage of container CPU usage
stats pct(container_cpu_usage_total, 50) as cpu_percentage_median by kubernetes.container_name
| filter Type="Container"
```

```shell
# Pods Requested vs Pods Running
fields @timestamp, @message
| sort @timestamp desc
| filter Type="Pod"
| stats min(pod_number_of_containers) as requested, min(pod_number_of_running_containers) as running, ceil(avg(pod_number_of_containers-pod_number_of_running_containers)) as pods_missing by kubernetes.pod_name
| sort pods_missing desc
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
