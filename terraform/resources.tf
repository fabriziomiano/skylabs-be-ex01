resource "heroku_app" "app" {
  name = var.app_name
  region = "eu"
}

# Build code & release to the app
resource "heroku_build" "app" {
  app = heroku_app.app.name
  source = {
    url =  "https://github.com/fabriziomiano/skylabs-be-ex01/archive/master.tar.gz"
    version = "1.0"
  }
}

# Launch the app's web process by scaling-up
resource "heroku_formation" "app" {
  app        = heroku_app.app.name
  type       = "web"
  quantity   = 1
  size       = "free"
  depends_on = [heroku_build.app]
}
