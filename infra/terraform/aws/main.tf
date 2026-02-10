module "network" {
  source = "../modules"

  project_name = var.project_name
}

module "storage" {
  source = "../modules"

  project_name = var.project_name
}

module "database" {
  source = "../modules"

  project_name = var.project_name
  db_username  = var.db_username
  db_password  = var.db_password
}
