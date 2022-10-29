# acr

- Azure Container Registry
- Images published to ACR must be retagged E.g., `hvitoi.azurecr.io/nginx:latest`

## Setup

```sh
# Login to ACR
az acr login --name "hvitoi" # under the hood it adds a registry to docker
```

## Retag and push image

```sh
docker image tag "nginx" "hvitoi.azurecr.io/nginx" # retag
docker image push "hvitoi.azurecr.io/nginx" # push
```

## Manage

```sh
# Create repository
az acr create \
  --resource-group "demo-rg" \
  --name "hvitoi" \
  --sku Basic

# List images from ACR
az acr repository list \
  --name "hvitoi" \
  --output table

## Show tags of a specific repository
az acr repository show-tags \
  --name "hvitoi" \
  --repository "nginx" \
  --output table

# Query image from ACR image
az acr list \
  --resource-group "demo-rg" \
  --query "[].{acrLoginServer:loginServer}" \
  --output table
```

## Assign RBAC role to K8S cluster

```sh
# Get K8S clientID
CLIENT_ID=$(az aks show --resource-group "demo-rg" --name "demo-k8s" --query "servicePrincipalProfile.clientId" --output tsv)

# Get ACR clientID
ACR_ID=$(az acr show --name "hvitoi" --resource-group "demo-rg" --query "id" --output tsv)

# Assign permission
az role assignment create \
  --assignee $CLIENT_ID \
  --scope $ACR_ID \
  --role "acrpull"
```
