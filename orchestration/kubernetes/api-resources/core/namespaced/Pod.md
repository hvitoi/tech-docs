# Pod (po)

- Kubernetes does not deploy containers directly on the worker nodes, instead it encapsulates it as an object named "Pod"
- A pod runs one of more containers (usually a main container and optionally side-car containers)

## Properties

### spec.containers[]

- If any of the container fails, the POD restarts
- Multi-container PODs **Design Patterns**
  - `Sidecar`
  - `Adapter`
  - `Ambassador`

```yaml
apiVersion: v1 # access to predefined set of object types
kind: Pod # kind of object to be created
metadata: # metadata to identify the object
  name: myapp
  labels:
    app: myapp
spec: # specification about the object
  containers:
    - name: nginx-container
      image: nginx:1.20
    - name: log-agent
      image: log-agent
```

### spec.containers[].env

- Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
spec:
  containers:
    - name: postgres
      image: postgres:12
      # set envs one by one
      env:
        # from literal
        - name: MY_FAVORITE_COLOR
          value: blue
        # from secret
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: pgsecret
              key: PG_PASSWORD
        # from configmap
        - name: MY_TOP_CONFIG
          valueFrom:
            configMapKeyRef:
              name: pgconfigmap
              key: PG_CONFIG
        # from field
        - name: MY_FAVORITE_ANIMAL
          fieldRef:
            fieldPath: metadata.labels # map labels into envs
```

### spec.containers[].envFrom

- Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
spec:
  containers:
    - name: postgres
      image: postgres:12
      # set all envs from a resource
      envFrom:
        - configMapRef:
            name: simpleconfigmap
        - secretRef:
            name: simplesecret
```

### spec.containers[].command & spec.containers[].args

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-curl
spec:
  containers:
    - name: curl
      image: curlimages/curl
      command: ["sleep"] # override the entrypoint from dockerfile
      args: ["infinity"] # override the cmd from dockerfile
```

### spec.containers[].ports[]

- This information is primarily informational, it does not expose the port outside the Pod (for that a service is needed)
- It tells Kubernetes and other tools (e.g., monitoring systems) that the application inside the container listens on the specified port.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
spec:
  containers:
    - name: postgres
      image: postgres:12
      ports:
        - containerPort: 5432
```

### spec.containers[].volumeMounts & spec.volumes

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  nodeName: node-name # manually schedule pod
  containers:
    - name: myapp
      image: nginx
      volumeMounts:
        - name: host-filesystem
          mountPath: /host-filesystem
        - name: postgres-data
          mountPath: /var/lib/postgresql/data # path to be mounted inside of the container
          subPath: postgres
        - name: pod-info
          mountPath: /etc/podinfo
          readOnly: false
        - name: configmap-data
          mountPath: /configmaps
        - name: secret-data
          mountPath: /secrets
  volumes:
    # from host filesystem
    - name: host-filesystem
      hostPath:
        path: /
        type: Directory # DirectoryOrCreate
    # from pvc
    - name: postgres-data
      persistentVolumeClaim:
        claimName: database-pvc
    # from aws storage
    - name: aws-volume
      awsElasticBlockStore:
        volumeID: <volume-id>
        fsType: ext4
    # from labels and annotations
    - name: pod-info
      downwardAPI:
        items:
          - path: labels
            fieldRef:
              fieldPath: metadata.labels
          - path: annotations
            fieldRef:
              fieldPath: metadata.annotations
    # from configmap
    - name: configmap-data
      configMap: # each key is created as a file
        name: simpleconfigmap
    # from secret
    - name: secret-data
      secret: # each key is created as a file
        secretName: simplesecret
        defaultMode: 420
```

### spec.containers[].livenessProbe & spec.containers[].readinessProbe

- Probes
  - **Liveness Probe**
    - Signals that a pod is in a failure state
    - If it fails, pod is restarted
  - **Readiness Probe**
    - Signals that the pod is ready to accept traffic
    - If it fails, traffic is not accepted
    - Traffic is blocked by removing the pod from the service LBs

- When to start probing? (Startup Probe)
  - It is defined by the `initialDelaySeconds` property
  - Signals that a pod has been started
  - Liveness or readiness probes start only after the startup probe is received
  - Specially useful for slow starting containers (to avoid them getting killed by the kubelet)

- `Kubelet` periodically fetches the probes of each pod in the node

- Springboot Actuator provides built-in readiness and liveness probes
- Old pods will be deleted only when the new pods are ready the receive traffic

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
    - name: nginx
      image: nginx:latest

      livenessProbe:
        initialDelaySeconds: 60 # start performing the probe (by kubelet) N seconds after the container has started
        periodSeconds: 1 # how often to perform the probe (by kubelet)
        httpGet: # Option 1
          port: 8000
          path: /actuator/health/liveness
        exec: # Option 2
          command:
            - /bin/shz
            - -c
            - nc -z localhost 8095

      readinessProbe:
        httpGet:
          port: 8000
          path: /actuator/health/readiness


```

### spec.containers[].resources

- Kube scheduler uses the resource information to decide which node to place the pod
- The default resource requests and resource limits are defined in the `LimitRange` object

- **Resource Requests**
  - Defaults:`0.5 vCPU` (500m), `256 Mi RAM`  (if no LimitRange is defined)
  - 1 CPU is equals to: 1 AWS vCPU, 1 GCP Core, 1 Azure Core, 1 Hyperthread
  - 1m (milicpu) is the minimum amount of CPU, it is 0.001 vCPU

- **Resource Limits**
  - Defaults: `1 vCPU` (1000m), `512 Mi RAM` (if no LimitRange is defined)
  - If CPU usage exceeds the limit, the container is **throttled**
  - If memory usage exceeds the limit constantly, the container is **terminated** (OOMKilled)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
      resources:
        requests: # This is the minimum resources that k8s will allocated to the container
          memory: 1Gi
          cpu: 1
        limits: # max resource usage
          memory: 2Gi
          cpu: 1200m # same as 1.2 cpu

          # gpu units
          nvidia.com/gpu: 1
          amd.com/gpu: 1
          aws.amazon.com/neuron: 1
          habana.ai/gaudi: 1
```

### spec.restartPolicy

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
spec:
  containers:
    - name: postgres
      image: postgres:12
  restartPolicy: Never
```

### spec.imagePullSecrets

- In order to authenticate against a private container registry, a secret must be created

```shell
kubectl create secret docker-registry "regcred" \
  --docker-server "private-registry.io" \
  --docker-username "registry-user" \
  --docker-password "registry-password" \
  --docker-email "mail@mail.com"
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx-container
      image: private-registry.io/apps/internal-app:1.0.0
  imagePullSecrets:
    - name: regcred
```

### spec.nodeName

- Every pod has a field called `spec.nodeName`
- It is a responsibility of the `scheduler` to fill this field and schedule the pod. But you can do that manually too
- The nodeName property cannot be modified after the pod has been created
- If a pod could not be scheduled to any node because a `scheduler` is not present, the pod remains in `pending` state
- Another way to schedule a pod to a node is creating a `Binding` object

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-po
  labels:
    app: myapp
spec:
  containers:
    - name: nginx-container
      image: docker.io/nginx
      ports:
        - containerPort: 3000
  nodeName: node01
```

### spec.NodeSelector

- With the node selectors you can `run certain workloads in certain nodes`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
  # select schedulable nodes by labels
  nodeSelector:
    a-size: a-large-node
```

### spec.affinity.nodeAffinity

- `Scheduling`: the state in which the pod does not exist yet
- `Execution`: the state in which a pod is running and has already been scheduled

- Node affinity types
  - **requiredDuringSchedulingIgnoredDuringExecution**: if affinity rules cannot be matched, pod will not be scheduled
  - **preferredDuringSchedulingIgnoredDuringExecution**: if affinity rules cannot be matched, pod will be scheduled to another node that "violates less" the rules

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions: # select node by labels
              - key: karpenter.sh/capacity-type
                operator: In
                value:
                  - spot
              - key: foo
                operator: NotIn
                value:
                  - small
              - key: bar
                operator: Exists
```

### spec.affinity.podAntiAffinity

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: karpenter.sh/capacity-type
                operator: In
                value:
                  - spot
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - topologyKey: kubernetes.io/hostname
```

### spec.schedulerName

- A pod can be instructed to use a specific scheduler other than the default

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
  schedulerName: my-custom-scheduler
```

### spec.tolerations

- `Toleration`: tolerance that a `pod` has to a specific node taint. If not specified, pods have no tolerations. Toleration does not guarantee that a pod will be scheduled to the tolerated pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
  tolerations:
    - key: "nvidia.com/gpu" # tolerates the node taint "nvidia.com/gpu"
      operator: "Exists"
      effect: "NoSchedule"
    - key: "foo"
      operator: "Equal"
      value: "blue"
      effect: "NoSchedule"
```

### spec.initContainers

- **initContainer**: a container that will runs a `initial setup` task until completion and then terminates

- That is a task that will be run only one time when the pod is first created. E.g., pulls a code or binary from a repository that will be used by the main application
- Or a process that waits for an external service or database to be up before the actual application starts

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
    - name: myapp-container
      image: busybox:1.28
      command: ["sh", "-c", "echo 'The app is running!' && sleep 3600"]
  initContainers:
    # each initContainer is executed in sequence
    # if any container execution fails, the whole pod is restarted (and start the init containers all over)
    # While init containers are running, the pod shows the status "Init:0/1"
    - name: init-myservice-pullcode
      image: busybox
      command:
        [
          "sh",
          "-c",
          "git clone https://github.com/foo/bar.git",
        ]
    - name: init-db
      image: busybox:1.28
      command:
        [
          "sh",
          "-c",
          "until nslookup mydb; do echo 'Waiting for mydb'; sleep 2; done;",
        ]
    - name: init-db2
      image: busybox:1.31
      command:
        [
          "sh",
          "-c",
          'echo -e "Checking for the availability of MySQL Server deployment"; while ! nc -z mysql 3306; do sleep 1; printf "-"; done; echo -e "  >> MySQL DB Server has started";',
        ]
```

- Each init container is run one at a time in sequential order (`Init:0/3`)
- If any of the initContainers fail to complete, Kubernetes restarts the Pod repeatedly until the Init Container succeeds

### spec.securityContext

- Can be configured for at `Container level` or `Pod level`
- Container settings will override the Pod settings

- **runAsUser**: ID of the user to use
- **capabilities**: linux capabilities that can be added or removed

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myos
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      securityContext:
        runAsUser: 0 # override user 1000, and run as user 0 (root)
        capabilities: # capabilities apply only for the securityContext inside the container
          add: ["MAC_ADMIN"]
  securityContext:
    runAsUser: 1000 # will be overridden
```

### spec.topologySpreadConstraints

- Describes how a group of pods ought to spread across topology domains (e.g., Availability Zones)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  topologySpreadConstraints:
    - topologyKey: "topology.kubernetes.io/zone" # try to use one than one zone (as defined by this label)
      maxSkew: 1
      whenUnsatisfiable: ScheduleAnyway

      # only nodes that have this label
      labelSelector:
        matchLabels:
          mylabel: foo
```
