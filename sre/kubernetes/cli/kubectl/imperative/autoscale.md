# kubectl autoscale

- Scales automatically based on load
- Creates a `HorizontalPodAutoscaler` (HPA) resource

```shell
# Scales 1 when cpu reaches 70% until 10 max
kubectl autoscale "deployment/mysql" \
  --min "5" \
  --max "10" \
  --cpu-percent "70"
```
