# aws secretsmanager

```shell
# Create a new secret with a value
aws secretsmanager create-secret \
  --name mysecret/connector-mtls \
  --secret-string file:///absolute/path/to/secret.txt

# Get secret metadata
aws secretsmanager describe-secret \
  --secret-id mysecret/connector-mtls

# Get secret
aws secretsmanager get-secret-value \
  --secret-id mysecret/connector-mtls

# Update secret
aws secretsmanager put-secret-value \
  --secret-id mysecret/connector-mtls \
  --secret-string file:///absolute/path/to/secret.txt
```
