# appservice

```sh
# Create App Service Plan
az appservice plan create \
  --resource-group "demo-rg" \
  --name "hvitoi-appserviceplan" \
  --sku "B1" \
  --is-linux # linux app service plans are required to run containers
```
