# Container Network Interface (CNI)

- CNI allows multiple network solutions be compatible with Kubernetes
- CNI is configured in the `kubelet`
- CNI defines how the plugin should be developed and how container runtimes should invoke them
- Plugins available
  - `bridge`
  - `vlan`
  - `ipvlan`
  - `macvlan`
  - `windows`
  - `dhcp` (3rd party)
  - `host-local` (3rd party)
- Example: bridge plugin
  - Container runtime must
    - Create network namespace
    - Identify network the container must attach to
    - Invoke the Network Plugin (bridge) when container is added
    - Invoke the Network Plugin (bridge) when container is deleted
    - JSON format of the network configuration
  - Network Plugin must
    - Support command line arguments (add, del, check)
    - Support parameters container id, network ns, etc
    - Manage IP address assignment to pods
    - Return results in a specific format

## Networking

- Each `node` must have at least one `interface` connected to the network
- Each `interface` must have an `address` configured
- `Hosts` must have a unique `hostname` and `mac address`

![Kubernetes Networking](.images/kubernetes-networking.png)

## Ports

- `kube-apiserver`: 6443
- `etcd`: 2379 (2380 for etcd p2p connection)
- `kubelet`: 10250
- `kube-scheduler`: 10251
- `kube-controller-manager`: 10252

- Worker node expose services for external access on ports `30000-32767`

![Kubernetes ports](.images/kubernetes-ports.png)

## Networking Model (Between pods)

- Every pod should have an IP Address
- Every pod should be able to communicate with every pod in the same node
- Every pod should be able to communicate with every pod on other nodes without NAT

![Pod networking](.images/pod-networking.png)

## CNI

- Whenever a container is manipulated, `kubelet` executes a script defined by the CNI config
- `--cni-conf-dir=/etc/cni/net.d`: configuration so that kubelet knows which plugin to use
- `--cni-bin-dir=/etc/cni/bin`: binary for all supported plugins

```shell
./net-script.sh add "container" "namespace"
```

- `ADD`
  1. Create veth pair
  1. Attach veth pair
  1. Assign IP address
  1. Bring Up Interface

## WeaveWorks

- An weaver `agent` is deployed on the node and stores the topology of the entire setup
- Agents communicate with each other to update its topology info
- Weaver is deployed as `DaemonSet`
