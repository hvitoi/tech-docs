# vmss

```sh
az vmss create \
  -n "demo-vmss" \
  -g "demo-rg" \
  --instance-count 1 \
  --image "Win2016Datacenter" \
  --data-disk-sizes-gb 10 \
  --vnet-name "demo-vnet" \
  --subnet "default" \
  --public-ip-per-vm \
  --admin-username "hvitoi"
```

## Extensions

```sh
az vmss extension set \
  --publisher "Microsoft.Compute" \
  --version "1.10" \
  --resource-group "demo-rg" \
  --vmss-name "demo-vmss" \
  --name "CustomScriptExtension" \
  --settings "script.json"
```
