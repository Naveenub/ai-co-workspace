variable "project_name" {}
variable "db_username" {}
variable "db_password" {}

resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15"
  instance_class       = "db.t3.micro"
  name                 = "workspace"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
  publicly_accessible  = false

  tags = {
    Name = "${var.project_name}-db"
  }
}

output "db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
