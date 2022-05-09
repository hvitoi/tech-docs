# Other

## Application Management

- **Self Managed**

  - `Ketch`: wrapper around other tool (bad)
  - `Shipa`: wrapper around other tool (bad )
  - `Knative`: self managed serverless solution
  - `Kubevela`: create new simpler CRDs

- **Managed**

- `Fly.io`: think about the code only. Very simple
- `Google Cloud Run`: based on knative
- `Azure Container Instances`: simple
- `Azure Container Apps`: newer container instances
- `AWS Lightsail`: aws alternative. Very simple
- `AWS ECS`: AWS ECS (with or without Fargate). Competitor of Kubernetes
- `AWS Lambda`: function runner (also runs container images)

## Infrastructure & Services

- `Chef`: old
- `Puppet`: old
- `Ansible`: most used tool to manage infrastructure on premise
- `Terraform`: manage infrastructure on cloud
- `Pulumi`: imperative way to define infrastructure. Has its own language
- `Eksctl`: for kubernetes clusters in AWS EKS only
- `Crossplane`: manages the infrastructure using kubernetes. Integrates well with cloud native tools. Provide CRDs for any infrastructure

## GitOps

- `Argo CD`: great ecosystem
- `Flux`: invented the term gitops. Has great corporative support from weaveworks
- `Racher Fleet`: designed for huge scale

## Progressive Delivery

- `Argo Rollouts`: ...
- `Flagger`: from Weaveworks

## Security

- `Snyk`: security scanning
- `Kubespace`: scan the k8s cluster and container images

- `Gatekeeper`: leverages K8S Admission Controller. Create your own policies for the cluster
- `Kyverno`: create policies similar to gatekeeper, but designed to be kubernetes native

## Development

- **Dev Environment**
  - `Gitpod`: spin a code from a git repo as a container in a remote infrastructure
  - `Okteto`
  - `Devspace`
  - `Codezero`
  - `Skaffold`
- **Local Environment**
  - `Kind`: kubernetes cluster running in docker
  - `K3D`: kubernetes cluster running in docker (K3S lightweight K8S distribution)
  - `Microk8s`: linux only
  - `Rancherdesktop`: full replacement for docker. Build container images and run kubernetes clusters (k3s)
  - `Capsule`: create namespace with steroids
  - `Vcluster`: create virtual k8s cluster inside of a real k8s cluster

## CI/CD Pipelines

- `Jenkins`: time-proof pipeline solution. Bottle tested
- `Circle CI`: pipeline as a service. Independent of big vendors
- `Code Fresh`: runs Argo Workflows
- `Argo Workflows + Argo Events`: pipelines cloud-native way
- `Tekton`: similar to argo. Cloud native
- `Github Actions`: easy and great
- `Devtron`: collection of tools

## Logging, Monitoring & Troubleshooting

- `Loki`: best self hosted logging solution. By grafana
- `Prometheus`: the standard for monitoring and metrics in kubernetes
- `Grafana`: best for visualization
- `Troubleshoot.sh`: troubleshooting as a service
- `Komodor`: troubleshooting by yourself

## Kubernetes Dashboards

- `K9S`: Terminal graphical interface
- `Kubeapps`: collection of other tools
- `Kubesphere`: integrate different tools
- `K8slens`: most polished dashboard
- `Octant`: bad
- `Rancher`: complete dashboard for multiple clusters

## Containers

- `Docker`: pioneer, but bloated
- `Buildx`: build images only. Runs as a daemon
- `Kaniko`: build container images remotely in a cluster as a container
- `Shipwright`: wrapper around other tools to build container images
- `Nerdctl`: born out of containerd project. Build container images

## Kubernetes

- `EKS`: great, but always behind
- `ECS Fargate`: strange
- `AKS`: great
- `GKE`: the best
- `GKE Autopilot`: fully managed GKE solution
- `Linode LKE`: cheap
- `Digital Ocean DOKS`: cheap
- `Civo CK`: new comer, cheap. Based on K3S
