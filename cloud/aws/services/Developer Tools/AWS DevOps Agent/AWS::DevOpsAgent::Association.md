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

- `Aws`
- `Dynatrace`
- `EventChannel`
- `GitHub`
- `GitLab`
- `MCPServer`
- `MCPServerDatadog`
- `MCPServerNewRelic`
- `MCPServerSplunk`
- `ServiceNow`
- `Slack`
- `SourceAws`
