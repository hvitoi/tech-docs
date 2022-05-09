# AzNetworkSecurityGroup

```powershell
# VNet config
$demosubnetConfig = New-AzVirtualNetworkSubnetConfig `
                      -Name default `
                      -AddressPrefix "10.3.0.0/24"

# Create VNet
$vnet = New-AzVirtualNetwork `
          -ResourceGroupName "demo-rg" `
          -Location "southcentralus" `
          -Name "demo-vnet" `
          -AddressPrefix "10.3.0.0/16" `
          -Subnet $demosubnetConfig

# Create Public IP
$demoip = New-AzPublicIpAddress `
            -ResourceGroupName "demo-rg" `
            -Location "southcentralus" `
            -Name "demo-ip" `
            -AllocationMethod "Dynamic"

# NSG config
$RuleConfig = New-AzNetworkSecurityRuleConfig `
                -Name "RuleRDP" `
                -Protocol "TCP" `
                -Direction "Inbound" `
                -Priority "300" `
                -SourceAddressPrefix "2.49.112.48" `
                -SourcePortRange "*" `
                -DestinationAddressPrefix "*" `
                -DestinationPortRange "3389" `
                -Access "Allow"

# Create NSG
$securitygroup = New-AzNetworkSecurityGroup `
                  -ResourceGroupName "demo-rg" `
                  -Location "southcentralus" `
                  -Name "demo-nsg" `
                  -SecurityRules $RuleConfig

# Create NIC (attach subnet, publicIP and NSG)
$nic = New-AzNetworkInterface `
        -Name "demo-nic" `
        -ResourceGroupName "demo-rg" `
        -Location "southcentralus" `
        -SubnetId $vnet.Subnets[0].Id `
        -PublicIpAddressId $demoip.Id `
        -NetworkSecurityGroupId $securitygroup.Id

# Get VM credentials (write)
$cred = Get-Credential

# VM config
$vmConfig = New-AzVMConfig `
  -VMName "demo-vm" `
  -VMSize "Standard_D2s_v3" | `
  Set-AzVMOperatingSystem `
    -Windows `
    -ComputerName "demo-vm" `
    -Credential $cred | `
    Set-AzVMSourceImage `
      -PublisherName "MicrosoftWindowsServer" `
      -Offer "WindowsServer" `
      -Skus "2016-Datacenter" `
      -Version "latest" | `
      Add-AzVMNetworkInterface `
        -Id $nic.Id

# Create VM
New-AzVM `
  -ResourceGroupName "demo-rg" `
  -Location "southcentralus" `
  -VM $vmConfig
```
