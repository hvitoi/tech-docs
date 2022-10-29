# role

- Used to setup permissions

```sh
# Get clientId of the "Service Principal"
CLIENT_ID=$(az aks show --resource-group "demo-rg" --name "demo-k8s" --query "servicePrincipalProfile.clientId" --output tsv)

# Get ACR resource Id
ACR_ID=$(az acr show --resource-group "demo-rg" --name "hvitoi" --query "id" --output tsv) # /subscriptions/c903ad61-2a3e-49b1-ad34-8affe3fdb1df/resourceGroups/awesome-rg/providers/Microsoft.ContainerRegistry/registries/hvitoi

# Assign to the "Service Principal" (which is used by aks) permissions to pull images from ACR
az role assignment create \
  --assignee $CLIENT_ID \
  --scope $ACR_ID \
  --role "acrpull"
```
