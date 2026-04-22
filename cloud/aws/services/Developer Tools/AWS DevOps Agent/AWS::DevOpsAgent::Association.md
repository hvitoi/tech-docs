# AWS::DevOpsAgent::Association

- Associate the DevOps agent with an external tool

## Properties

```yaml
Type: AWS::DevOpsAgent::Association
Properties:
  AgentSpaceId: String
  Configuration:
    ServiceConfiguration
  LinkedAssociationIds:
    - String
  ServiceId: String
```

### ServiceId

- It's the UUID of the `AWS::DevOpsAgent::Service` resource
- The exception is only for the "Aws" and "SourceAwd" configurations, in which the id is `aws`

### Configuration

- `Aws`: the same aws account in which the agent is. Grant access for example to EKS
- `SourceAWS`: another aws account. Grant access for example to EKS
- `GitHub`: you need one association for each repo (referencing the same AWS::DevOpsAgent::Service)
- `Slack`
- `MCPServer`
- ...
