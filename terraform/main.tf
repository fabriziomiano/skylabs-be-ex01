terraform {
  required_providers {
    heroku = {
      source = "heroku/heroku"
      version = "~> 2.0"
    }
  }
}

output "app_url" {
  value = "https://${heroku_app.app.name}.herokuapp.com"
}