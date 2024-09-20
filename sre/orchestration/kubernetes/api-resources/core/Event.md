# Event

- Events for of non-namespaced resources (node, etc) are non-namespaced
- Events for of namespaced resources (pod, deployments, etc) are namespaced

```yaml
apiVersion: v1
kind: Event
metadata:
  creationTimestamp: "2021-08-21T22:57:14Z"
  name: minikube.169d7469137ba7f3
  namespace: default
  resourceVersion: "407"
  uid: 5ff17bd5-a8e8-471f-a85a-cebc466533c8
type: Normal
reason: NodeReady
source:
  component: kubelet
  host: minikube
count: 1
involvedObject:
  kind: Node
  name: minikube
  uid: minikube
message: "Node minikube status is now: NodeReady"
```

```yaml
apiVersion: v1
kind: Event
metadata:
  name: nginx-6799fc88d8-44n5m.169d76352fe68269
  namespace: default
type: Normal
source:
  component: kubelet
  host: minikube
count: 1
reason: Created
involvedObject:
  apiVersion: v1
  fieldPath: spec.containers{nginx}
  kind: Pod
  name: nginx-6799fc88d8-44n5m
  namespace: default
message: Created container nginx
```
