# oidc-plugins

```shell
kubectl oidc-login setup \
  --oidc-issuer-url=https://myorg.okta.com/oauth2/abcde \
  --oidc-client-id=123

kubectl oidc-login get-token \
  --oidc-issuer-url=https://myorg.okta.com/oauth2/abcde \
  --oidc-client-id=123 \
  --oidc-extra-scope=email \
  --oidc-extra-scope=offline_access \
  --oidc-extra-scope=profile \
  --oidc-extra-scope=openid
```

```yaml
apiVersion: v1
kind: Config
current-context: staging-kubernetes

contexts:
  - name: staging-kubernetes
    context:
      cluster: my-aws-account/staging-kubernetes
      user: okta-oidc

clusters:
  - name: my-aws-account/staging-kubernetes
    cluster:
      server: https://foo.gr7.us-east-1.eks.amazonaws.com
      certificate-authority-data: ...

users:
  - name: okta-oidc
    user:
      exec:
        apiVersion: client.authentication.k8s.io/v1beta1
        command: kubectl
        args:
          - oidc-login
          - get-token
          - --oidc-issuer-url=https://yourorg.okta.com/oauth2/abcd
          - --oidc-client-id=123
          - --oidc-extra-scope=email
          - --oidc-extra-scope=offline_access
          - --oidc-extra-scope=profile
          - --oidc-extra-scope=openid
        env: null
        interactiveMode: IfAvailable
        provideClusterInfo: false
```
