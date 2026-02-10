resource "aws_s3_bucket" "artifacts" {
  bucket = "ai-workspace-artifacts"
  acl    = "private"
}
