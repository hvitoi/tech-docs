# AWS::DevOpsAgent::Service

- Represents a tool that the DevOps Agent will have access to
- It's also called "Capability Providers"
- It needs to be associated with the `AWS::DevOpsAgent::AgentSpace` using an `AWS::DevOpsAgent::Association`

## Private Links

- You might want to connect with MCPs available in a private VPC of your organization. For that a private link is needed. See `aws devops-agent create-private-connection`
- <https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-privately-hosted-tools.html#related-topics>

## Properties

```yaml
Type: AWS::DevOpsAgent::Service
Properties:
  KmsKeyArn: String
  ServiceDetails:
    ServiceDetails
  ServiceType: String
  Tags:
    - Tag
```

```json
// Example
{
  "services": [
    {
      "serviceId": "51aadfb1-f042-403e-9810-87378ff05e65",
      "serviceType": "github",
      "additionalServiceDetails": {
        "github": {
          "owner": "hvitoi", // has potential access to all repos of that user/org (if you allow it on the app installation)
          "ownerType": "user"
        }
      }
    },
    {
      "serviceId": "c3284ed3-7634-4fa1-afd6-80563bc10052",
      "serviceType": "mcpserver",
      "additionalServiceDetails": {
        "mcpserver": {
          "name": "prometheus-mcp",
          "endpoint": "https://myprometheus/mcp",
          "authorizationMethod": "api-key",
          "apiKeyHeader": "x-api-key"
        }
      },
      "privateConnectionName": "prometheus-mcp"
    }
  ]
}
```

### ServiceType

- `mcpserver`
- `github`
- `gitlab`
- ...
