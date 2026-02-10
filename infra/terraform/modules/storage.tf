variable "project_name" {}

resource "aws_s3_bucket" "artifacts" {
  bucket = "${var.project_name}-artifacts"

  tags = {
    Name = "${var.project_name}-artifacts"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.artifacts.bucket
}
