# destroy

- destroy resources contained in `.tf` files

```shell
# destroy resources from all tf files
terraform destroy

# destroy specific resource
terraform destroy -target "azurerm_resource_group.my-rg"
```
