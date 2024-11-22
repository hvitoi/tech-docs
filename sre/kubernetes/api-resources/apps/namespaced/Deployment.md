# Deployment (deploy)

- `Deployment` objects encapsulate `ReplicaSet` which encapsulates `Pod`
- Deployment objects create replicasets, which create pods automatically
- Enables `rollout`, `rollbacks`, `rolling updates` of pods
- Each new revision of the deployment creates a new replicaset, this way it is possible to rollback to previous versions

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deploy
spec:
  replicas: 3 # target number of identical pod instances
  selector: # what pods to control
    matchLabels:
      app: myapp
  template: # single pod specification
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx-container
          image: nginx
```

## Properties

### spec.strategy

- Deployment Strategy

- **Recreate**
  - Destroy all replicas immediately and create new ones
  - The `old ReplicaSet` is scaled down to 0 and the `new ReplicaSet` is scaled up to n
  - It's good for databases that cannot have more than 1 replica at a time

- **Rolling Update** (default)
  - Take down old version and bring up newer version one by one
  - The `old ReplicaSet` is scaled down one at a time, simultaneously scaling up the `new ReplicaSet` one by one

- The final state of any deployment strategies maintains the `newer ReplicaSet` (scaled to N), and the `older ReplicaSet` (scaled to 0)
- The reason to maintain the older ReplicaSet is for rolling back purposes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25% # max 25% will go down at once to upgrade
```

### spec.minReadySeconds

- Readiness

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
  minReadySeconds: 15
```

### spec.revisionHistoryLimit

- My default, a deployment maintains the history of the last 10 revisions

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
  revisionHistoryLimit: 15
```

### spec.replicas (bypass)

- Bypass to `rs.spec.replicas`

### spec.selector (bypass)

- Bypass to `rs.spec.selector`

### spec.template (bypass)

- Bypass to `rs.spec.template`
