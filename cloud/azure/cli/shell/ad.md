# ad

## sp

```sh
# Create service principal
az ad sp create-for-rbac \
  --name "http://my-service-principal-name" \
  --scopes "acr-registry-id" \
  --role "acrpull" \
  --query "password" \
  --output "tsv"

# Show service principal
az ad sp show \
  --id "http://my-service-principal-name" \
  --query "appId" \
  --output "tsv"
```

## user

```sh
az ad user create \
  --display-name "john" \
  --user-principal-name "john@awesome.onmicrosoft.com" \
  --password "pass" \
  --query "objectId" \
  --output "tsv"
```

## group

```sh
# create
az ad group create \
  --display-name "devteam" \
  --mail-nickname "devteam" \
  --query "objectId" \
  --output "tsv"

# add users
az ad group member add \
  --group "devteam" \
  --member-id "user-id"

# show
 az ad group show \
  --group "aks-admins"
```
