# AzureStorageAccount

```powershell
# Create new SA
New-AzStorageAccount `
  -Name "storage-account-name" `
  -ResourceGroupName "rg-name" `
  -Location "region-name" `
  -Kind "BlockBlobStorage" `
  -SkuName "Premium_LRS"
```
