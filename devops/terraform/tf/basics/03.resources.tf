# random_pet is resource from "random" provider
resource "random_pet" "aksrandom" {

}

# Azure Resource group
resource "azurerm_resource_group" "demo-rg" { # demo-rg is for terraform reference only
  name     = "demo-rg"                        # actual resource name in azure
  location = "South Central US"

  tags = {
    "environment" = "k8sdev"
    "demotag"     = "refreshtest"
  }
}

resource "azurerm_resource_group" "aks-rg" {
  # values from variables
  name     = "${var.resource_group_name}-${var.environment}"
  location = var.location
}
