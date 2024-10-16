# Config

- Kubeconfig can be configured by setting the environment variable `KUBECONFIG` with the path location of the file
- By default it looks for the path `~/.kube/config`

```yaml
apiVersion: v1
kind: Config
current-context: henry@playground

contexts:
  - name: henry@playground
    context:
      cluster: playground
      user: henry
      namespace: default # default namespace for that context

clusters:
  - name: playground
    cluster:
      server: https://10.10.10.10:6443
      certificate-authority-data: ca.crt-base64

users:
  - name: henry
    user:
      client-certificate-data: henry.crt-base64
      client-key-data: henry.key-base64

  # oidc login (requires https://github.com/int128/kubelogin)
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
