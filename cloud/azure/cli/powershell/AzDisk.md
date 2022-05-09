# AzDisk

```powershell
# Disk config
$dataDiskConfig = New-AzDiskConfig -SkuName $storageType -Location $location -CreateOption "Empty" -DiskSizeGB $dataDiskSize

# Create disk
$dataDisk = New-AzDisk -ResourceGroupName $resourcegroup -DiskName $dataDiskName -Disk $dataDiskConfig
```
