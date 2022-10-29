# Azure Terraform

- Requires the plugin: <https://marketplace.visualstudio.com/items?itemName=charleszipp.azure-pipelines-tasks-terraform>
- The plugin is installed in the Azure DevOps Organization

## Steps

- The backend configuration for `state files` must be commented out. The state files will be configured in azure devops

- Variable related to `environment` are managed by azure

## Service Connection

1. Type: `Azure Resource Manager`
   - Authentication Method: `Service Principal` (automatic)
   - Grant acesso to all resource groups

- Under `API permission` ("Manage" tab) in the Service Principal created in Azure Portal...
  - Add API permission: `Azure Active Directory Graph`
  - Permission: `Directory.ReadWrite.All`
  - Click `Grant admin consent for Default Directory`

## SSH Keys

- Generate a SSH key manually

```sh
# Create SSH Key
ssh-keygen \
  -m "PEM" \
  -t "rsa" \
  -b "4096" \
  -C "azureuser@myserver" \
  -f "./akssshkey" \
  -N "mypassphrase"
```

- SSH keys will be stored in azure devops under `Pipelines/Library/Secure Files`
- Upload your SSH pub key to secure files
- Authorize for use in all pipelines
