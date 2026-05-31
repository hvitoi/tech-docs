# StatefulSet (sts)

- Kubernetes object to manage `stateful applications` (on the other hand Deployments manage stateless applications)
- A `StatefulSet` provides guarantees about the ordering, uniqueness, and persistence of pods, making it ideal for applications that maintain state (e.g., databases, key-value stores, etc.)

| Property         | Deployment                 | StatefulSet                                     |
| ---------------- | -------------------------- | ----------------------------------------------- |
| Pod names        | Random hash                | Ordinal: name-0, name-1, …                      |
| Creation order   | All at once, any order     | Sequential: 0 ready → then 1 → then 2           |
| Deletion order   | Any order                  | Reverse: 2 → 1 → 0                              |
| Network identity | Shared Service, random IPs | Stable DNS per pod                              |
| Storage          | Usually shared/ephemeral   | One dedicated volume per pod, survives restarts |

## Properties

### spec.volumeClaimTemplates

- It's a template for PVCs
- The StatefulSet creates `one PVC per pod`, not one shared PVC. So you end up with:
  - redis-data-redis-0   →  PV  (1Gi)   mounted on redis-0
  - redis-data-redis-1   →  PV  (1Gi)   mounted on redis-1
  - redis-data-redis-2   →  PV  (1Gi)   mounted on redis-2
- If let's say redis-2 crashes and gets rescheduled to a new node, the new redis-2 re-attaches to the exact same redis-data-redis-2
- Deleting the StatefulSet does not delete the PVCs by default. But it means you clean them up manually.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
spec:
  serviceName: "redis"
  replicas: 3
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
  volumeClaimTemplates:
    - metadata:
        name: redis-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

### spec.serviceName

- This points at a `headless Service` (a Service with clusterIP: None). Instead of load-balancing across random pods, it gives each pod its own stable DNS name
- The StatefulSet does NOT create the Service object automatically, you need to do it

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
spec:
  serviceName: redis
  replicas: 3
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
  volumeClaimTemplates:
    - metadata:
        name: redis-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

- Setting `clusterIP: None` makes it headless — no virtual IP, no load balancing. Instead, DNS behaves differently:
  - A query for `redis.default.svc.cluster.local` returns the A records of all pods (not one VIP). And because a StatefulSet is backing it, each pod also gets its own DNS record:
    - `redis-0.redis.default.svc.cluster.local` → pod redis-0's IP
    - `redis-1.redis.default.svc.cluster.local` → pod redis-1's IP
    - `redis-2.redis.default.svc.cluster.local` → pod redis-2's IP
- With a Deployment you only get a single virtual IP that hides which pod you hit.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis        # must match spec.serviceName in the StatefulSet
spec:
  clusterIP: None    # ← this is what makes it "headless"
  selector:
    app: redis       # matches the pod labels
  ports:
    - port: 6379
      targetPort: 6379
```
