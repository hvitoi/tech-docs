# AzImage

```powershell
# Create an image configuration from a VM
$image = New-AzImageConfig `
          -Location "East US" `
          -SourceVirtualMachineId "$vm.Id"

# Create the custom image
New-AzImage `
  -ResourceGroupName "demo-rg" `
  -ImageName "my-image" `
  -Image "$image"
```
