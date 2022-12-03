# vm

```shell
# Show a VM
az vm image show --location `location`

# List all publishers
az vm image list-publishers --location `location`
```

## Create VM

- If no location is provided, the location used is the one from the resource group

```shell
az vm create \
  --resource-group "demo-rg" \
  --name "demovm" \
  --image "win2019datacenter" \
  --admin-username "hvitoi" \
  --admin-password "pass1234"
```

## Apply extension

```shell
az vm extension set \
  --resource-group "demo-rg" \
  --vm-name "demovm" \
  --name "customScript" \
  --publisher "Microsoft.Azure.Extensions" \
  --settings "customscript.json"
```

## Encryption

- Encrypt a disk with keys to be stored in key vault

```shell
az vm encryption enable \
  --name "demo-vm" \
  --resource-group "demo-rg" \
  --disk-encryption-keyvault "hvitoi" \
  --volume-type "ALL" # ALL, DATA, OS
```
