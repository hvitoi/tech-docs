# monitor

## metrics

```shell
# Alert when API goes beyond 80% for a period of 5 min
az monitor metrics alert create \
  -n "linuxvm" \
  -g "demo-rg" \
  --scopes "/subscriptions/{tenant-id}/resourceGroups/demo-rg/providers/Microsoft.Compute/virtualMachines/linuxvm" \
  --condition "avg Percentage CPU > 80" \ # 80%
  --condition "CPU Percentage > 800" \ # 80% = 800 milicores
  --window-size "5m" \
  --evaluation-frequency "1m" \
  --description "High CPU"
```

## log-analytics

```shell
az monitor log-analytics workspace create \
  --resource-group "aks-rg" \
  --workspace-name "aks-loganalyticsworkspace" \
  --query "id" \
  --output "tsv"
```
