# ReplicaSet (rs)

- `ReplicaSet` is a newer version of ReplicationController
- It uses `selectors` (just like services) to match the target pods by label
- ReplicaSet is a process that monitors the pods by their labels

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

## Self healing

- `ReplicaSet` maintains a stable set of instances of a pod. It guarantees the availability of pods
- Therefore it is one of the pieces in Kubernetes that allows applications to self heal
- This helps in ensuring that a pod is re-created automatically when the application within the pod crashes
- Kubernetes provides additional support to check the health of applications running within PODs and take necessary actions through **Liveness** and **Readiness** Probes
