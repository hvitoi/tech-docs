# Config

- Kubeconfig can be configured by setting the environment variable `KUBECONFIG` with the path location of the file
- By default it looks for the path `~/.kube/config`

```yaml
apiVersion: v1
kind: Config
current-context: henry@playground
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
contexts:
  - name: henry@playground
    context:
      cluster: playground
      user: henry
      namespace: default # default namespace for that context
```
