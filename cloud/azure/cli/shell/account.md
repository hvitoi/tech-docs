# Account

```sh
az login
```

## show

```sh
# Show account
az account show \
  --output "table"

# Get subscription ID
az account show \
  --subscription "subscription-name" \
  | jq -r '.id'

# Tenant ID
az account show \
  --query "tenantId" \
  --output "tsv"
```

## set

```sh
# Set up a account
az account set --subscription "subscription-id"
```
