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

- `SourceAws`
- `Aws`: associate an AWS Account to discover the topology

For the following ones, you need to use the UUID of the `AWS::DevOpsAgent::Service` resource

- `GitHub`
- `GitLab`
- `Slack`
- `Dynatrace`
- `ServiceNow`
- `MCPServer`
- `MCPServerNewRelic`
- `MCPServerDatadog`
- `MCPServerSplunk`
- `EventChannel`
