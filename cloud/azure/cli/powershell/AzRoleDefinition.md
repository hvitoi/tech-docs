# AzRoleDefinition

```powershell
# Create a role based on json
New-AzRoleDefinition `
  -InputFile "customrole.json"

# Assign role to user
New-AzRoleAssignment `
  -ResourceGroupName "demo-rg" `
  -SignInName "demousrA@techsup1000gmail.onmicrosoft.com" `
  -RoleDefinitionName "stagingrole"
```

```json
{
  "Name": "stagingrole",
  "Id": null,
  "IsCustom": true,
  "Description": "Allows for read access to Azure Virtual Machines and storage accounts",
  "Actions": ["Microsoft.Compute/*/read", "Microsoft.Storage/*/read"],
  "NotActions": [],
  "AssignableScopes": ["/subscriptions/20c6eec9-2d80-4700-b0f6-4fde579a8783"]
}
```
