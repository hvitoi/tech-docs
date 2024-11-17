# DaemonSet (ds)

- `DaemonSet` assures that one replica of the pod runs on each node
- DeamonSets are not scheduled by kube-scheduler, because it must be in all of the nodes
- **Use cases**
  - Monitoring Solution: monitoring agent for each node
  - Logs Viewer
  - kube-proxy: networking solution for each node

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: myapp-ds
spec:
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      name: myapp-po
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx-container
          image: nginx
```
