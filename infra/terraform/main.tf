terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  # O backend deve ser configurado no CI via -backend-config
  backend "azurerm" {}
}

provider "azurerm" {
  features {}
  use_oidc = true
}

variable "project_name" {
  default = "fiap-churn"
}

variable "location" {
  default = "brazilsouth"
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-${var.project_name}"
  location = var.location
}

# --- Azure Container Registry ---
resource "azurerm_container_registry" "acr" {
  name                = "acr${replace(var.project_name, "-", "")}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

# --- Container Apps Environment ---
resource "azurerm_container_app_environment" "aca_env" {
  name                = "env-${var.project_name}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# --- Container App (API) ---
resource "azurerm_container_app" "api" {
  name                         = "api-${var.project_name}"
  container_app_environment_id = azurerm_container_app_environment.aca_env.id
  resource_group_name          = azurerm_resource_group.rg.name
  revision_mode                = "Single"

  template {
    container {
      name   = "churn-api"
      image  = "${azurerm_container_registry.acr.login_server}/churn-api:latest"
      cpu    = 0.25
      memory = "0.5Gi"
      
      env {
        name  = "ENVIRONMENT"
        value = "production"
      }
    }
    min_replicas = 0 # Scale to zero para economia
    max_replicas = 2
  }

  ingress {
    allow_insecure_connections = false
    external_enabled           = true
    target_port                = 8000
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }

  lifecycle {
    ignore_changes = [
      template[0].container[0].image # Evitar que o Terraform resete a imagem no deploy
    ]
  }
}

output "api_url" {
  value = azurerm_container_app.api.latest_revision_fqdn
}
