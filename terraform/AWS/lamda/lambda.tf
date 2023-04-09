data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "C:/Users/OlegP/Desktop/psycalc-bot"
  output_path = "${path.root}/lambda.zip"

  excludes = [
    "terraform.tfstate",
    ".env",
    ".gitignore",
    "docker-compose.yml",
    "Dockerfile",
    "logictorefactor.py",
    "questions.js",
    "requirements.txt",
    "uniqueness_of_questions.py",
    "validate_tests.py",
    "venv/",
    "terraform/"
  ]
}





resource "aws_s3_bucket" "bucket" {
  bucket = local.s3_bucket
}

resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.bucket.id
  key    = local.s3_key
  source = local.lambda_zip_out
}

resource "aws_lambda_function" "example" {
  function_name = "telegram_bot"

  s3_bucket = aws_s3_bucket.bucket.id
  s3_key    = local.s3_key

  handler = "main.handler"
  runtime = "python3.8"

  role = aws_iam_role.lambda_exec.arn
}

resource "aws_iam_role" "lambda_exec" {
  name = "example_lambda"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })

  inline_policy {
    name = "allow_s3_access"

    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect   = "Allow"
          Action   = [
            "s3:GetObject",
            "s3:ListBucket",
            "s3:PutObject",
          ]
          Resource = [
            aws_s3_bucket.bucket.arn,
            "${aws_s3_bucket.bucket.arn}/*",
          ]
        }
      ]
    })
  }
}