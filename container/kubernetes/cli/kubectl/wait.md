# wait

```shell
kubectl wait "kafka/my-cluster" \
  --for="condition=Ready" \
  --timeout="300s"
```
