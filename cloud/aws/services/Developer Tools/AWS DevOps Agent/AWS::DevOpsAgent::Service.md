# AWS::DevOpsAgent::Service

- Represents a tool that the DevOps Agent will have access to
- It's also called "Capability Providers"
- It needs to be associated with the `AWS::DevOpsAgent::AgentSpace` using an `AWS::DevOpsAgent::Association`

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

### ServiceType

- `dynatrace`
- `gitlab`
- `mcpserver`
- `mcpservernewrelic`
- `mcpserversplunk`
- `servicenow`
