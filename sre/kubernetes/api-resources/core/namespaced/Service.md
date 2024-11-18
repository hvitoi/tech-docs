# Service (svc)

- Kubernetes services work as `layer 4 load-balancers`
- They provide a stable `DNS address`
- They forward the connections to one of the pods which are backing the service
- Services use `selectors` (just like deployments and replicasets) to match the target pods by label

## ClusterIP

- Only accessible within the cluster
- Creates a `virtual IP` inside of the cluster to expose a pod or set of pods
- The reason for a virtual IP is that you cannot rely on the internal IP of the pod (it may change frequently)
- Also, provides a single interface for a group of pods

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-svc
spec:
  type: ClusterIP # Optional line. Services are ClusterIP by default
  selector:
    app: myapp
  ports:
    - name: my-cluster-ip
      protocol: TCP
      port: 3000
      targetPort: 3000
  clusterIP: None # None: Use the own Pod IP. Blank: automatically set a random IP
```

## NodePort

- Expose the service on `each node`. This port is forwarded to the port on the `pod`
- With NodePort, even if the pod is hosted on only one node, the port is open for all the nodes
- The app is then accessible from all nodes (even if the app is not deployed in that specific node)
- The port range on the node is from `30000-32767`

- A random algorithm is used to forward request to multiple pods
- NodePorts span **across nodes**
  - Therefore reaching the IP-Port of any node forwards the traffic to the correct pod (even if it is not in that node)
  - <http://192.169.1.2:30008>, <http://192.169.1.3:30008>, <http://192.169.1.2:40008>

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-svc
spec:
  type: NodePort
  selector: # selects every pod with matching key-value pairs
    app: myapp
  ports:
    - name: my-node-port
      protocol: TCP
      port: 3050 # port of the service (the one other pods will reach to)
      targetPort: 3000 # port of the application (port if not provided)
      nodePort: 31515 # port to the outside world (random 30000-32767 port if not provided)
```

## LoadBalancer

- Provides a single `URL` for the end user
- The end-user now reaches a LB (not the node directly as with NodePort)
- The LB then routes the traffic to the correct node
- Usually the LB from a cloud platform is used. Kubernetes integrates with the following LB:
  - Google Cloud Platform
  - AWS
  - Azure
- **LB Drawbacks**
  - One `Public IP` is created on the Cloud Provider `for each LoadBalancer` Service (which is not good! - use ingress whenever possible)
  - Also, there is no SSL termination (It's L4 LB, just redirect traffic)

![Load Balancer Problem](../../../concepts/.images/loadbalancer-problem.png)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-svc
spec:
  type: LoadBalancer
  selector: # selects every pod with matching key-value pairs
    app: myapp
  ports:
    - name: my-load-balancer
      protocol: TCP
      port: 3050 # port of the service
      targetPort: 3000 # port of the application (port if not provided)
```

## ExternalName

- Proxies the connection to an external URL
- Uses the default port for the service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  type: ExternalName
  externalName: mydb.mysql.database.azure.com
```
