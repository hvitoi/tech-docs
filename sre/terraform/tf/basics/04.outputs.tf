# print info after resources have been created/modified

output "location" {
  value = azurerm_resource_group.aks-rg.location
}

output "resource_group_id" {
  value = azurerm_resource_group.aks-rg.id
}

output "resource_group_name" {
  value = azurerm_resource_group.aks-rg.name
}
