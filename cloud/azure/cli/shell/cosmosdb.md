# cosmosdb

```shell
# Single region (no redundancy)
az cosmosdb create \
  --name "hvitoi" \
  --resource-group "demo-rg" \
  --default-consistency-level "BoundedStaleness" \ # Reads can lag behind the writes by at most `K` versions of an item or by `T` time interval
  --max-interval "5" \ # allow simultaneous and out-of-order orders with a max 5s tolerance window (used only with bounded staleness)
  --locations \
    regionName="South Central US" \
    failoverPriority="0" \
    isZoneRedundant="false"

# Multiple regions
az cosmosdb create
  --name "hvitoi" \
  --resource-group "demo-rg" \
  --locations \
    regionName="South Central US" \
    failoverPriority="0" \
    isZoneRedundant="false"
  --locations \
    regionName='East US 2' \
    failoverPriority="1" \
    isZoneRedundant="false"
  --enable-automatic-failover="true" # automatically use another region for write if one fails

# Create CosmosDB account based on the Azure Table API (not SQL)
az cosmosdb create
  --name "hvitoi" \
  --resource-group "demo-rg" \
  --locations \
    regionName="South Central US" \
    failoverPriority="0" \
    isZoneRedundant="false"
  --capabilities "EnableTable"
```
