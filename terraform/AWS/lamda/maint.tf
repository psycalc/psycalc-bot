provider "aws" {
  region = "us-east-1"
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/../../psycalc-bot"
  output_path = "${path.module}/lambda_function_payload.zip"
}

locals {
  s3_bucket      = "my-s3-bucket"
  s3_key         = "v1.0.0/telegram_bot.zip"
  lambda_zip_out = data.archive_file.lambda_zip.output_path
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

resource "aws_apigatewayv2_api" "api" {
  name          = "telegram-bot-api"
  protocol_type = "HTTP"
}

resource "aws_lambda_permission" "allow_api_gateway_invoke" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.example.arn
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.api.execution_arn}/*/*"
}

resource "aws_apigatewayv2_integration" "integration" {
  api_id           = aws_apigatewayv2_api.api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.example.invoke_arn
}

resource "aws_apigatewayv2_route" "route" {
  api_id    = aws_apigatewayv2_api.api.id
  route_key = "ANY /{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.integration.id}"
}

resource "aws_apigatewayv2_deployment" "deployment" {
  api_id = aws_apigatewayv2_api.api.id

  trigger {
    name = "deploy"
    tags = {
      Environment = "production"
    }
  }
}

resource "aws_api_gateway_rest_api" "example" {
  name        = "psycalc-bot"
  description = "REST API for the PsyCalc Telegram bot"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "execute-api:Invoke"
      ],
      "Resource": [
        "execute-api:${var.aws_region}:${var.aws_account}://${aws_api_gateway_rest_api.example.id}/*"
      ]
    }
  ]
}
EOF
}

resource "aws_api_gateway_resource" "example" {
  rest_api_id = aws_api_gateway_rest_api.example.id
  parent_id   = aws_api_gateway_rest_api.example.root_resource_id
  path_part   = "bot"
}

resource "aws_api_gateway_method" "example" {
  rest_api_id   = aws_api_gateway_rest_api.example.id
  resource_id   = aws_api_gateway_resource.example.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "example" {
  rest_api_id             = aws_api_gateway_rest_api.example.id
  resource_id             = aws_api_gateway_resource.example.id
  http_method             = aws_api_gateway_method.example.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.example.invoke_arn
}

resource "aws_api_gateway_deployment" "example" {
  rest_api_id = aws_api_gateway_rest_api.example.id
  stage_name  = "prod"

  lifecycle {
    create_before_destroy = true
  }
}

