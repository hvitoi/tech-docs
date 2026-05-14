# aws secretsmanager

```shell
# Get metadata (description, ARN, tags, rotation config)
aws secretsmanager describe-secret \
  --secret-id mysecret/staging/connector-mtls

# Get the secret value
aws secretsmanager get-secret-value \
  --secret-id mysecret/staging/connector-mtls
```
