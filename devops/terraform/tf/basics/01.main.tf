terraform {
  # Terraform version
  required_version = ">= 0.13"

  # Terraform providers
  required_providers {
    # Azure Resource Manager 2.x (Base Azure RM Module)
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 2.0"
    }
    # Azure Active Directory 1.x (required for AKS and Azure AD Integration)
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 1.0"
    }
    # Random 3.x (Required to generate random names for Log Analytics Workspace)
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }

  # Terraform State Storage
  backend "azurerm" {
    resource_group_name  = "terraform-storage"
    storage_account_name = "hvitoi"
    container_name       = "tfstatefiles"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {

  }
}
