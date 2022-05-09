# AzKeyVault

```powershell
# Create key vault
$keyVault = New-AzKeyVault `
              -Name "hvitoi" `
              -ResourceGroupName "demo-rg" `
              -Location "Central US" `
              -EnableSoftDelete `
              -EnablePurgeProtection

# Get Storage Account
$storageAccount = Set-AzStorageAccount `
                    -Name "hvitoi" `
                    -ResourceGroupName "demo-rg" `
                    -AssignIdentity

# Allow SA to manager the key vault keys
Set-AzKeyVaultAccessPolicy `
  -VaultName "$keyVault.VaultName" `
  -ObjectId "$storageAccount.Identity.PrincipalId" `
  -PermissionToKeys "wrapkey, unwrapkey, get, recover"

# Get Key Vault key
$key = Add-AzKeyVaultKey `
  -VaultName "$keyVault.VaultName" `
  -Name "appkey" `
  -Destination "Software"

#
Set-AzStorageAccount
  -ResourceGroupName "$storageAccount.ResourceGroupName" `
  -AccountName "$storageAccount.StorageAccountName" `
  -KeyvaultEncryption `
  -KeyVaultUri "$keyVault.VaultUri"
  -KeyName "$key.Name" `
  -KeyVersion "$key.Version" `
```
