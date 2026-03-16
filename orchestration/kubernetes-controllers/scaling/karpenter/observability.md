# Karpenter Observability

## Logs

- Always export your logs (e.g., to Cloudwatch)

```shell
kubectl logs -n kube-system -l app.kubernetes.io/name=karpenter -f
```

## Metrics

- <https://karpenter.sh/docs/reference/metrics/>
- Karpenter exposes Prometheus metrics at `karpenter.kube-system.svc.cluster.local:8080/metrics`
- Metrics
  - Pod startup latency
  - Node utilization
  - ...
