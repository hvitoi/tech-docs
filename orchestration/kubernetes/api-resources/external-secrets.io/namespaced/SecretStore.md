# SecretStore (ss)

- Sync secrets from AWS SecretsManager

```yaml
apiVersion: external-secrets.io/v1
kind: SecretStore
metadata:
  name: aws-secret-store-us-east-1
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
```
