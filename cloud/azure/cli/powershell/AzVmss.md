# AzVmss

```powershell
$config = @{
  "fileUris" = (,"https://hvitoi.blob.core.windows.net/script/script.ps1");
  "commandToExecute" = "powershell -ExecutionPolicy Unrestricted -File install.ps1"
}

# Get VMSS instance
$set = Get-AzVmss -ResourceGroupName "demo-rg" -VMScaleSetName "demo-vmss"

## Add extension
$set = Add-AzVmssExtension -VirtualMachineScaleSet $set -Name "customScript" -Publisher "Microsoft.Compute" -Type "CustomScriptExtension" -TypeHandlerVersion 1.9 -Setting $config

# Update Vmss
Update-AzVmss -ResourceGroupName "demo-rg" -Name "demo-vmss" -VirtualMachineScaleSet $set
```
