# DaemonSet (ds)

- `DaemonSet` assures that one (and only one) replica of the pod runs on each node
- DaemonSets are not scheduled by kube-scheduler, because it must be in all of the nodes

- **Use cases**
  - `Logs collection`: e.g., fluentd
  - `Node monitoring`: e.g., cloudwatchagent
  - `Application Trace Collection`: e.g., aws x-ray
  - `Network solutions`: e.g., kube-proxy

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
