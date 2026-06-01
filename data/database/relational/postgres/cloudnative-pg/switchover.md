# Switchover

- Switchover is the planned version — graceful role swap with no data loss, used for maintenance.

```shell
# Trigger switchover it by hand
kubectl cnpg promote mycluster <target-instance-name>
```
