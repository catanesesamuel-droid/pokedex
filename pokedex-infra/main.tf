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

# Cosmos DB
resource "azurerm_cosmosdb_account" "main" {
  name                = "cosmos-pokedex"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  consistency_policy { consistency_level = "Session" }
  geo_location { location = azurerm_resource_group.main.location; failover_priority = 0 }
}

resource "azurerm_cosmosdb_sql_database" "main" {
  name                = "pokedex"
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}

# Storage Account (para Functions)
resource "azurerm_storage_account" "main" {
  name                     = "stpokedex"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Function App
resource "azurerm_service_plan" "main" {
  name                = "asp-pokedex"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = "Y1"  # Consumption plan (gratis)
}

resource "azurerm_linux_function_app" "main" {
  name                = "func-pokedex"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  storage_account_name       = azurerm_storage_account.main.name
  storage_account_access_key = azurerm_storage_account.main.primary_access_key
  service_plan_id            = azurerm_service_plan.main.id
  site_config {
    application_stack { python_version = "3.11" }
    cors { allowed_origins = ["*"] }
  }
  app_settings = {
    COSMOS_ENDPOINT  = azurerm_cosmosdb_account.main.endpoint
    COSMOS_KEY       = azurerm_cosmosdb_account.main.primary_key
    COSMOS_DATABASE  = "pokedex"
    JWT_SECRET       = "cambia-esto-por-una-clave-segura"
  }
}

# Static Web App (frontend)
resource "azurerm_static_web_app" "main" {
  name                = "swa-pokedex"
  resource_group_name = azurerm_resource_group.main.name
  location            = "spaincentral"
  sku_tier            = "Free"
}