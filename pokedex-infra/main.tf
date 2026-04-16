terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "~> 3.90"
    }
  }
  
  
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstatepokedex1234"  
    container_name       = "tfstate"
    key                  = "pokedex.terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

# Tus recursos (el grupo que quieras crear)
resource "azurerm_resource_group" "main" {
  name     = "rg-pokedex"
  location = "spaincentral"
}