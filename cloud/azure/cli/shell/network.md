# network

## vnet

```shell
# Create Virtual Network and a Default Subnet
az network vnet create \
  --resource-group "aks-rg" \
  --name "aks-vnet" \
  --address-prefix "10.0.0.0/8" \
  --subnet-name "aks-subnet-default" \
  --subnet-prefix "10.240.0.0/16"

# Create Subnet for Virtual Nodes
az network vnet subnet create \
  --resource-group "aks-rg" \
  --vnet-name "aks-vnet" \
  --name "aks-subnet-vnodes" \
  --address-prefixes "10.241.0.0/16"

# Show VNet Default subnet
az network vnet subnet show \
  --resource-group "aks-rg" \
  --vnet-name "aks-vnet" \
  --name "aks-subnet-default" \
  --query "id" \
  --output "tsv"
```

## private-dns

```shell
# Create your Private DNS Zone
az network private-dns zone create \
  -g "demo-rg" \
  -n "cloud-internal.com"

# Create a virtual network link
az network private-dns link vnet create \
  -g "demo-rg" \
  -n "networklink" \
  -z "cloud-internal.com" \
  -v "privatenetwork" \
  -e "true"
```

## public-ip

```shell
# Create a Public IP
az network public-ip create \
  --resource-group "demo-rg" \
  --name "myAKSPublicIPForIngress" \
  --sku "Standard" \
  --allocation-method "static" \
  --query "publicIp.ipAddress" \
  -o "tsv"
```

## dns

```shell
# Show A records
az network dns record-set a list \
  --resource-group "demo-rg" \
  -z "hvitoi.com"

```
