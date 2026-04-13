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

```json
// example
{
  "associations": [
    // AWS Account
    {
      "agentSpaceId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "createdAt": "2026-04-10T11:55:38.558000+00:00",
      "updatedAt": "2026-04-10T11:55:38.558000+00:00",
      "status": "valid",
      "associationId": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
      "serviceId": "aws",
      "configuration": {
        "aws": {
          "assumableRoleArn": "arn:aws:iam::123456789012:role/devops-agent-agent-space-role",
          "accountId": "123456789012",
          "accountType": "monitor"
        }
      }
    },
    // MCP Server
    {
      "agentSpaceId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "createdAt": "2026-04-10T12:02:03.366000+00:00",
      "updatedAt": "2026-04-10T12:02:03.366000+00:00",
      "associationId": "cccccccc-cccc-cccc-cccc-cccccccccccc",
      "serviceId": "dddddddd-dddd-dddd-dddd-dddddddddddd",
      "configuration": {
        "SDK_UNKNOWN_MEMBER": {
          "name": "mcpserver"
        }
      }
    },
    // GitHub Repo
    {
      "agentSpaceId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "createdAt": "2026-04-13T11:29:22.677000+00:00",
      "updatedAt": "2026-04-13T11:29:22.677000+00:00",
      "associationId": "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee",
      "serviceId": "ffffffff-ffff-ffff-ffff-ffffffffffff",
      "configuration": {
        "github": {
          "repoName": "my-repo-1",
          "repoId": "111111111",
          "owner": "my-user",
          "ownerType": "user"
        }
      }
    },
    // GitHub Repo
    {
      "agentSpaceId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "createdAt": "2026-04-13T11:31:58.335000+00:00",
      "updatedAt": "2026-04-13T11:31:58.335000+00:00",
      "associationId": "99999999-9999-9999-9999-999999999999",
      "serviceId": "ffffffff-ffff-ffff-ffff-ffffffffffff",
      "configuration": {
        "github": {
          "repoName": "my-repo-2",
          "repoId": "222222222",
          "owner": "my-user",
          "ownerType": "user"
        }
      }
    }
  ]
}
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
