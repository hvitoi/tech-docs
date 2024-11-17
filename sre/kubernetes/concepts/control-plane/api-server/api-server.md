# API Server

- It's the primary management component of the kubernetes cluster
- Orchestrate all operations within the cluster
- Can be accessed via `kubectl` or via `rest`

![Kube API Server](.images/kube-apiserver.png)

- **Responsabilities**
  - `Authenticate`
  - `Validate Request`
  - `Retrieve Data`
  - `Update ETCD`

- `kube-apiserver` is the only one component that interacts directly with ETCD. kube-scheduler and kubelet can update etcd but by means of the kube-apiserver

- Example: creating a pod
  1. user requests a new pod (kubectl or rest)
  1. kube-apiserver receives the request and consults etcd cluster to check if it already exists or has changed
  1. kube-apiserver then pass info to the kube-scheduler for a new pod creation
  1. kube-apiserver contacts the correct node kubelet to deploy the container
  1. kubelet responds to kube-apiserver with the current node status
  1. kube-apiserver updates etcd

## The API

- **Groups**
  - `Core group`
    - /api/v1/ns
    - /api/v1/po
    - /api/v1/svc
  - `Named group`
    - /apis/apps
    - /apis/extensions
    - /apis/networking.k8s.io
    - /apis/storage.k8s.io
    - /apis/authentication.k8s.io
    - /apis/certificates.k8s.io
  - `Other groups`
    - /version
    - /metrics
    - /healthz
    - /logs
- **Resources**
  - /apis/apps/`deployments`
  - /apis/apps/`statefulsets`
  - ...
- **Verbs**
  - List
  - Get
  - Create
  - Delete
  - Update
  - Watch

### kubectl

- Kubectl is the k8s command-line tool
- Kubectl manages the master in the k8s cluster
- Instructions <https://kubernetes.io/docs/tasks/tools/install-kubectl/>

```shell
# Download binary
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"

# Make it executable
chmod +x "./kubectl"

# Move it to PATH
sudo mv "./kubectl" "/usr/local/bin/kubectl"

# Check installation version
kubectl version

# Information about the cluster
kubectl cluster-info
```

### rest

```shell
# Get all API groups
curl -X GET "https://10.10.10.10:6443/" --header "Authorization: Bearer my-jwt" --insecure
```

```shell
# Authentication
curl -X GET "/api/v1/pods" -u "user:pass" # basic auth
curl -X GET "/api/v1/pods" --header "Authorization: Bearer my-token" # token auth
curl -X GET "/api/v1/pods" --key "admin.key" --cert "admin.crt" --cacert "ca.crt" # certificate auth
```

```shell
# get pods
curl -X GET "/api/v1/pods" -u "user:pass"

# create pod
curl -X POST "/api/v1/namespaces/default/pods"
```
