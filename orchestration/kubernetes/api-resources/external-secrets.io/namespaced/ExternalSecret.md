# ExternalSecret (es)

```yaml
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: my-secret
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secret-store-us-east-1 # the SecretStore resource created
    kind: SecretStore
  target:
    name: my-secret
    creationPolicy: Owner
  dataFrom:
    - extract:
        key: mysecret/staging/connector-mtls
```
