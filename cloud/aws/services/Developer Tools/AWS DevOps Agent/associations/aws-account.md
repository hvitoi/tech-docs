# AWS Account

## Monitor Account (same account)

```json
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
}
```

## External Account (cross account)

```json
{
    "agentSpaceId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    "createdAt": "2026-04-17T18:28:22.060000+00:00",
    "updatedAt": "2026-04-17T18:43:52.222000+00:00",
    "status": "invalid",
    "associationId": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
    "serviceId": "aws",
    "configuration": {
        "sourceAws": {
            "accountId": "123456789012",
            "accountType": "source",
            "assumableRoleArn": "arn:aws:iam::123456789012:role/devops-agent-source-account-role"
        }
    }
}
```
