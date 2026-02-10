provider "aws" {
  region = "us-east-1"
}

module "network" {
  source = "../modules/network.tf"
}

module "db" {
  source = "../modules/db.tf"
}

module "storage" {
  source = "../modules/storage.tf"
}
