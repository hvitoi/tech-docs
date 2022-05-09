# AzPrivateDnsZone

```powershell
# Create Private DNS Zone
$myzone = New-AzPrivateDnsZone `
            -Name "cloud-internal.com" `
            -ResourceGroupName "demo-rg"

# Get a handle to your virtual network
$vnet = Get-AzVirtualNetwork `
          -Name "privatenetwork" `
          -ResourceGroupName "demo-rg"

# Create a virtual network link
$mylink = New-AzPrivateDnsVirtualNetworkLink `
            -ZoneName "cloud-internal.com" `
            -ResourceGroupName "demo-rg" `
            -Name "networklink" `
            -VirtualNetworkId $vnet.id `
            -EnableRegistration
```
