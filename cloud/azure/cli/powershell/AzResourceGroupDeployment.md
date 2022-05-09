# AzResourceGroupDeployment

- Deploy ARM templates

```powershell
New-AzResourceGroupDeployment `
  -Name "demo-deployment" `
  -ResourceGroupName "demo-rg" `
  -TemplateFile "template.json" `
  -TemplateParameterFile "parameters.json"
```
