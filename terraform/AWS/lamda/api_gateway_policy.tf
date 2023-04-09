data "aws_iam_policy_document" "api_gateway_policy" {
  statement {
    effect = "Allow"
    principals {
      type        = "*"
      identifiers = ["*"]
    }
    actions   = ["execute-api:Invoke"]
    resources = ["execute-api:${var.aws_region}:${var.aws_account}:*/*"]
  }
}

resource "aws_iam_policy" "api_gateway_policy" {
  name        = "api_gateway_policy"
  description = "Policy for API Gateway to allow invocation"
  policy      = data.aws_iam_policy_document.api_gateway_policy.json
}
