output "vpc_id" {
  value = module.network.vpc_id
}

output "db_endpoint" {
  value = module.database.db_endpoint
}

output "artifact_bucket" {
  value = module.storage.bucket_name
}
