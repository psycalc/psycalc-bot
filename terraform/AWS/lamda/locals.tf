
locals {
  s3_bucket      = "my-s3-bucket"
  s3_key         = "v1.0.0/telegram_bot.zip"
  lambda_zip_out = data.archive_file.lambda_zip.output_path
}