# Minikube

## Install

- Minikube creates the nodes (virtual machines)
- Instructions <https://kubernetes.io/docs/tasks/tools/install-minikube/>
- [Get started](https://minikube.sigs.k8s.io/docs/start/)

```sh
# Download binary
curl -Lo "minikube" "https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"

# Make it executable
chmod +x "minikube"

# Install
sudo mkdir -p "/usr/local/bin/"
sudo install "minikube" "/usr/local/bin/"
```

## Basics

```sh
# Start a new cluster (exposes apiserver on port 8443)
minikube start
minikube start --memory "4096" # megabytes by default
minikube start --memory "4096m"
minikube start --memory "4g"

# Get status
minikube status

# Stop
minikube stop

# Delete
minikube delete
```

## Managing

```sh
## Switch into the node
minikube ssh

# Insert minikube context into kubeconfig
minikube update-context

## Configure local docker to point into docker inside the kubernetes cluster
eval $(minikube docker-env) # eval setup new environment variables

## Get node ip
minikube ip # The node is accessible on the browser with this IP!

# Open minikube dashboard
minikube dashboard

# Tunnel services
minikube tunnel

```

## Addons

```sh
# List of available addons
minikube addons list

# Enable addon
minikube addons enable "ingress"
minikube addons enable "metrics-server"
```
