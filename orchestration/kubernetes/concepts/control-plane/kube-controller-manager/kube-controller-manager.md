# kube-controller-manager

- Manages various controllers in Kubernetes
- Controllers are responsible for verifying and responding when nodes, containers or endpoints go down. They make decisions to bring up new resources in such cases.

- The `controllers` are continuously watching the `status` of the pod (**watch status**)
- The `controllers` act to solve a failure situation (**remediate situation**)

## Controllers

### Node Controller

- Monitors the state of `nodes`
- _Node Monitor Period = 5s_: Check status of nodes every 5s
- _Node Monitor Grace Period = 40s_: Wait 40s before marking it unreachable
- _Pod Eviction Timeout = 5m_: Wait 5m before before considering a node dead and moving the pods to a healthy node

![Node Controller](.images/node-controller.png)

### Replication Controller

- It's an older technology and has been replaced by `replicaset`
- Assure the desired number of containers are running
- The replication controller spans across multiple nodes in the cluster

![Replication Controller](.images/replication-controller.png)

### Endpoints Controller

- Populates the endpoints objects (joins services & pods)

### Service Account & Token Controller

- Creates default accounts and API Access for new namespaces

### Cloud Controller

- Cloud-specific control logic
- On-Premise Kubernetes clusters won't have this component

### Other controllers

- Controllers are enabled on the `--controllers` parameter
- By default enables all-by-default controllers

- List of all controllers
  - attachdetach
  - bootstrapsigner
  - clusterrole-aggregation
  - cronjob
  - csrapproving
  - csrcleaner
  - csrsigning
  - daemonset
  - deployment
  - disruption
  - endpoint
  - garbagecollector
  - horizontalpodautoscaling
  - job
  - namespace
  - nodeipam
  - nodelifecycle
  - persistentvolume-binder
  - persistentvolume-expander
  - podgc
  - pv-protection
  - pvc-protection
  - replicateset
  - replicationcontroller
  - resourcequota
  - root-ca-cert-publisher
  - route
  - service
  - serviceaccount
  - serviceaccount-token
  - statefulset
  - tokencleaner
  - ttl
  - ttl-after-finished
