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

### ServiceType

- `dynatrace`
- `gitlab`
- `mcpserver`
- `mcpservernewrelic`
- `mcpserversplunk`
- `servicenow`
