# AWS Account

```json
// example
{
  "associations": [
    // AWS Account (same account)
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
