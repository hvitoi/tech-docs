# StatefulSet (sts)

- Kubernetes object to manage `stateful applications` (on the other hand Deployments manage stateless applications)
- A `StatefulSet` provides guarantees about the ordering, uniqueness, and persistence of pods, making it ideal for applications that maintain state (e.g., databases, key-value stores, etc.)

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
spec:
  serviceName: "redis"  # The name of the headless service that routes traffic to the StatefulSet pods
  replicas: 3  # Number of Redis instances in the cluster
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
        - name: redis
          image: redis:alpine
          ports:
            - containerPort: 6379
          volumeMounts:
            - name: redis-data
              mountPath: /data
  volumeClaimTemplates:  # Defines a PersistentVolumeClaim for each pod in the StatefulSet
    - metadata:
        name: redis-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```
