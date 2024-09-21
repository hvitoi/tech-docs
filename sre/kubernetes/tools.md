# Container Tools

## Kubernetes Cluster

- `EKS`: great, but always behind
- `ECS Fargate`: strange
- `AKS`: great
- `GKE`: the best
- `GKE Autopilot`: fully managed GKE solution
- `Linode LKE`: cheap
- `Digital Ocean DOKS`: cheap
- `Civo CK`: new comer, cheap. Based on K3S

## Kubernetes Dashboards

- `K9S`: Terminal graphical interface
- `Kubeapps`: collection of other tools
- `Kubesphere`: integrate different tools
- `K8slens`: most polished dashboard
- `Octant`: bad
- `Rancher`: complete dashboard for multiple clusters

## Development Environment

- **Dev Environment**
  - `Gitpod`: spin a code from a git repo as a container in a remote infrastructure
  - `Github Codespaces`: like gitpod, but done by microsoft
  - `Okteto`
  - `Devspace`
  - `Tilt`
  - `Codezero`
  - `Skaffold`

- **Local Environment**
  - `Kind`: kubernetes cluster running in a container
  - `K3D`: kubernetes cluster running in a container (K3S lightweight K8S distribution)
  - `Minikube`: kubernetes cluster running in a container or via a standalone application
  - `Docker Desktop`: Build container images and run kubernetes clusters
  - `Rancher Desktop`: Build container images and run kubernetes clusters (k3s) - Full replacement for docker
  - `Microk8s`: runs in a Linux VM and uses snap to install its components
  - `Capsule`: create namespace with steroids
  - `Vcluster`: create virtual k8s cluster inside of a real k8s cluster

## Application Management

- **Manifests**
  - `Helm`
  - `Kustomize`
  - `Carvel ytt`: yamls with functions. Complex
  - `Jsonnet Tanka`: complex
  - `cdk8s`: allows manifests in any language

- **Self Managed**
  - `Knative`: self managed serverless solution
  - `Kubevela`: create new simpler CRDs
  - `Shipa`: wrapper around other tool (bad)
  - `Ketch`: wrapper around other tool (bad)

- **Cloud Managed**
  - `Fly`: think about the code only. Very simple
  - `Google Cloud Run`: based on knative
  - `Azure Container Instances`: simple
  - `Azure Container Apps`: newer container instances
  - `AWS Lightsail`: aws alternative. Very simple
  - `AWS ECS`: AWS ECS (with or without Fargate). Competitor of Kubernetes
  - `AWS Lambda`: function runner (also runs container images)

## Infrastructure & Service Management

- `Cluster API`: control plane to manage kubernetes resources
- `Eksctl`: for kubernetes clusters in AWS EKS only

## Image Build

- `Kaniko`: build container images remotely in a cluster as a container
- `Shipwright`: wrapper around other tools to build container images
