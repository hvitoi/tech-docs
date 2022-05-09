# Deployment

- `Deployment` objects encapsulate `ReplicaSet` which encapsulates `Pod`
- Deployment objects create replicasets, which create pods automatically
- Enables rolling updates of pods

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

## Deployment Strategy

- **Recreate**

  - Destroy all replicas immediately and create new ones
  - The `old ReplicaSet` is scaled down to 0 and the `new ReplicaSet` is scaled up to n
  - It's good for databases that cannot have more than 1 replica at a time

- **Rolling Update**

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
      app: nginx-deploy
  template:
    metadata:
      labels:
        app: nginx-deploy
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

## Readiness

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-deploy
  template:
    metadata:
      labels:
        app: nginx-deploy
    spec:
      containers:
        - name: nginx
          image: nginx
  minReadySeconds: 15
```
