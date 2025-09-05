terraform {
  required_providers {
    test = {
      source = "terraform.io/builtin/test"
    }

    http = {
      source = "hashicorp/http"
    }
  }
}

variable "api_url" {
  type    = string
  default = "https://msn.com:8080"
}

module "main" {
  source  = "../.."     # use the .tf files from the main directory
  api_url = var.api_url # override the default value in main.tf
}

locals {
  # break the URL into scheme and authority
  api_url_parts = regex(
    "^(?:(?P<scheme>[^:/?#]+):)?(?://(?P<authority>[^/?#]*))?",
    module.main.api_url,
  )
}

resource "test_assertions" "api_url" {

  # test the "api_url" component in main.tf
  component = "api_url"

  # verify local.api_url_parts.scheme
  equal "scheme" {
    description = "default scheme is https"
    got         = local.api_url_parts.scheme
    want        = "https"
  }

  # verify local.api_url_parts.authority
  check "port_number" {
    description = "default port number is 8080"
    condition   = can(regex(":8080$", local.api_url_parts.authority)) # true or false
  }
}

data "http" "api_response" {
  depends_on = [
    test_assertions.api_url, # previous block must pass
  ]

  url = module.main.api_url
}

resource "test_assertions" "api_response" {
  component = "api_response"

  check "valid_json" {
    description = "base URL responds with valid JSON"
    condition   = can(jsondecode(data.http.api_response.body))
  }
}
