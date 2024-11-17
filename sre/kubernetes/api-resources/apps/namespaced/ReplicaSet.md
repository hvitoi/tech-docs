# ReplicaSet (rs)

- It's a newer version of ReplicationController
- `ReplicaSet` will maintain a stable set of instances of a pod. It guarantees the availability of pods
- ReplicaSet is a process that monitors the pods by their labels
- There is a 1 to 1 relation to the pod replicas (3 pod replicas -> 3 replica sets)

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-rs
spec:
  replicas: 3
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

- Kubernetes supports **self-healing** applications through `ReplicaSets` and `Replication Controllers`
- This helps in ensuring that a POD is re-created automatically when the application within the POD crashes.
- Kubernetes provides additional support to check the health of applications running within PODs and take necessary actions through **Liveness** and **Readiness** Probes
