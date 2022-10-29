# storage

```sh
# List storage accounts
az storage account list
```

```sh
# Create a container
az storage container create \
  --name "demo-container" \
  --account-name "demo-storageaccount" \
  --account-key "Dbrn8TduNojZrzlKZSLHS8lHC1Yv6BDpG6XfeVBaJ9oKOzZmIBdczNo6vvThVHI4VikW1SqXkhaDr52tNDLxew=="

# Upload blob
az storage blob upload \
  --account-name "demo-storageaccount" \
  --container-name "demo-container" \
  --name "customrole.json" \
  --file "customrole.json" \
  --account-key "Dbrn8TduNojZrzlKZSLHS8lHC1Yv6BDpG6XfeVBaJ9oKOzZmIBdczNo6vvThVHI4VikW1SqXkhaDr52tNDLxew=="
```
