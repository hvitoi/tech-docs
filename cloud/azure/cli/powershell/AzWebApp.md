# AzWebApp

```powershell
# Create web app
New-AzWebApp `
  -Name "hvitoi" `
  -ResourceGroupName "demo-rg" ` # Existing resource group
  -AppServicePlan "hvitoi-appserviceplan" ` # Existing app service plan
  -Location "SouthCentralUs"
```

```powershell
# Add new slot
New-AzWebAppSlot `
  -Name "hvitoi" `
  -ResourceGroupName "demo-rg" `
  -Slot "staging"
```
