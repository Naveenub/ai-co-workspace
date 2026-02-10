resource "aws_rds_instance" "workspace_db" {
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  name                 = "workspace"
  username             = "admin"
  password             = "ChangeMe123"
  skip_final_snapshot  = true
}
