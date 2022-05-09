# AzVm

```powershell
# Create
New-AzVm `
  -ResourceGroupName "demo-rg" `
  -Name "demo-vm" `
  -Location "CentralUS" `
  -Image "win2019datacenter"

# Stop
Stop-AzVm `
  -ResourceGroupName "demo-rg" `
  -Name "demo-vm" `
  -Force

# Get
Get-AzVm `
  -ResourceGroupName "demo-rg" `
  -Name "demo-vm"
```

## Add a new disk

```powershell
$resourcegroup = 'test-grp'
$machinename = 'demovm'
$location = 'North Europe'
$storageType = 'Standard_LRS'
$dataDiskName = 'newdisk01'
$dataDiskSize = 20

# Disk config
$datadiskConfig = New-AzDiskConfig -SkuName $storageType -Location $location -CreateOption Empty -DiskSizeGB $dataDiskSize

# Create new disk
$dataDisk01 = New-AzDisk -DiskName $dataDiskName -Disk $datadiskConfig -ResourceGroupName $resourcegroup

# Get VM
$vm = Get-AzVM -Name $machinename -ResourceGroupName $resourcegroup

# Attach disk to VM
$vm = Add-AzVMDataDisk -VM $vm -Name $dataDiskName -CreateOption Attach -ManagedDiskId $dataDisk01.Id -Lun 1

# Update VM
Update-AzVM -VM $vm -ResourceGroupName $resourcegroup
```

## Resize

```powershell
# Get VM instance
$vm = Get-AzVM -ResourceGroupName "demo-rg" -VMName "demo-vm"

# Set new size
$vm.HardwareProfile.VmSize ="Standard_DS1_v2"

# Update VM
Update-AzVM -VM $vm -ResourceGroupName "demo-rg"
```

## Managed Identity

```powershell
$vm = Get-AzVm `
  -Name "appvm" `
  -ResourceGroupName "demo-rg"

Update-AzVm `
  -VM $vm `
  -ResourceGroupName "demo-rg" `
  -IdentityType "SystemAssigned" # managed identity

Update-AzVm `
  -VM $vm `
  -ResourceGroupName "demo-rg" `
  -IdentityType "UserAssigned" # conventional application object
```
