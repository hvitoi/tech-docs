# Google Kubernetes Engine (GKE)

- Skaffold must be configured to send a build requests to 'Google Cloud Build'

1. Create a new project on Google Cloud [Console](https://console.cloud.google.com/home/dashboard)
1. Go to Kubernetes Engine -> [Clusters](https://console.cloud.google.com/kubernetes/list)
1. Create Cluster
1. Cluster basics

- name: Name of the cluster
- zone: southamerica-east1-a
- version: at least 1.15

1. Node pools:

- number of nodes: 3
- Nodes/Machine type: g1-small (Series N1)

1. Install [GCloud SDK](https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu)

```sh
# Add the Cloud SDK distribution URI as a package source
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

1. Add the new context

```sh
# Login to GCloud SDK
gcloud auth login

# Initialize GCLoud
gcloud init
  # Re-initialize the previous configuration
  # Choose e-mail account
  # Select the project
  # Set default region (y)
  # southamerica-east1-a

# Add a context of C
gcloud container clusters get-credentials "cluster-name"

# List all contexts (clusters)
kubectl config get-contexts

# Select a context
kubectl config use-context "context-name"

```

1. Enable GCloud Build

- Enable GCloud Build on the console: Tools/Cloud Build
- Change skaffold: `googleCloudBuild: projectId: ticketing-283819`
- Change the image name to gcloud standards: `gcr.io/ticketing-283819/auth`

1. Create a Load Balancer

- Go to official documentation of [Nginx Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#gce-gke)

```sh
# Initialize as cluster-admin
kubectl create clusterrolebinding cluster-admin-binding \
  --clusterrole cluster-admin \
  --user $(gcloud config get-value account)
# Install Nginx Ingress Controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.34.1/deploy/static/provider/cloud/deploy.yaml
```

- Go to Networking / Network Services/ Load Balancing (a LB was automatically created)
- Get the IP address of the load balancer (35.198.25.168)
- Add the IP to the /etc/hosts: 35.198.25.168 ticketing.dev

1. Run the skaffold

```sh
# Authenticate
gcloud auth application-default login

# Run
skaffold dev
```
