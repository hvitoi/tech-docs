# AzApiManagement

```powershell
# Create API Management
New-AzApiManagement `
  -ResourceGroupName "demo-rg" `
  -Name "core-management" `
  -Location "East US" `
  -Organization "CompanyA" `
  -AdminEmail "admin@company.com"

# Set Context
$context = New-AzApiManagementContext `
            -ResourceGroupName "demo-rg" `
            -ServiceName "core-management"

# Import API
$api = Import-AzApiManagementApi `
        -Context $context `
        -SpecificationFormat "OpenApi" `
        -SpecificationUrl "https://corewebapi4000.azurewebsites.net/swagger/v1/swagger.json" `
        -ServiceUrl "https://corewebapi4000.azurewebsites.net"
```
