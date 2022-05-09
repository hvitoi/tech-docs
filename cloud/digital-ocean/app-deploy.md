# Digital Ocean App Deployment

## Create Kubernetes Cluster

- Menu -> Create Kubernetes Cluster
  - Any Country
  - Default VPC
  - Cluster Capacity: 1GB node / 3 nodes
  - No tags
  - Choose name for the cluster

## Management Tools

- doctl: Digital Ocean Control
- [doctl](https://github.com/digitalocean/doctl) repository with instructions for installation

```bash
# Install via snap
sudo snap install doctl
```

- Create a API key in Menu/API with any name with read/write permission
- Login to Digital Ocean

```bash
# Authenticate
doctl auth init # and paste the token
```

## Create the DO context

```bash
# Create context
doctl kubernetes cluster kubeconfig save 'cluster-name'

# Select context
kubectl config use-context `context-name`

# Test context
kubectl get nodes
```

## Create deploy scripts in GitHub Actions

```yml
name: deploy-myservice

on:
  push:
    branches:
      - master
    paths:
      - 'myservice/**'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Setup repository
        uses: actions/checkout@v2

      - name: Build docker image
        run: docker build -t hvitoi/myservice myservice

      - name: Login to DockerHub
        run: docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}

      - name: Push image to DockerHub
        run: docker push hvitoi/myservice

      - name: Setup Digital Ocean doctl
        uses: digitalocean/action-doctl@v2
        with:
          token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}

      - name: Create kubectl context
        run: doctl kubernetes cluster kubeconfig save mycluster

      - name: Restart the deployment
        run: kubectl rollout restart deployment myservice-depl
```

```yml
name: deploy-manifests

on:
  push:
    branches:
      - master
    paths:
      - 'infra/**'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Setup repository
        uses: actions/checkout@v2

      - name: Setup Digital Ocean doctl
        uses: digitalocean/action-doctl@v2
        with:
          token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}

      - name: Create kubectl context
        run: doctl kubernetes cluster kubeconfig save mycluster

      - name: Apply all the config files to the Kubernetes cluster
        run: kubectl apply -f infra/k8s && kubectl apply -f infra/k8s-prod
```

## Deploy Ingress Nginx

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.34.1/deploy/static/provider/do/deploy.yaml
```

## Get Load Balancer ID

- At Networking / Load Balancers
- Ingress Nginx created a load balancers
- Get the load balancer ip

## Destroy Cluster

- Networking/Load balancer - Destroy
- Kubernetes/Cluster - Destroy
