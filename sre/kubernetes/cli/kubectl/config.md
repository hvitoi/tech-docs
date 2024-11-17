# kubectl config

## view

- Default context is stored at `~/.kube/config` and it must have `600` permission

```shell
# Show kubeconfig
kubectl config view
kubectl config view -o jsonpath='{.users[?(@.name == "admin")].user.password}' # get user + password of the admin user
```

## get-contexts

```shell
# List all contexts (clusters)
kubectl config get-contexts
```

## current-context

```shell
# View current context
kubectl config current-context
```

## use-context

```shell
# Select a context
kubectl config use-context "context-name"
```

## set-cluster

- Set cluster

```shell
kubectl config set-cluster <cluster-name> \
  --server <url> \
  --insecure-skip-tls-verify true
```

## set-credentials

- Set user

```shell
kubectl config set-credentials "user-name" --token="token"
```

## set-context

- Set context, set a default namespace, make it currently in use

```shell
kubectl config set-context "context-name" --cluster="cluster" --user="user" --namespace="namespace" --current
```

## ~/.kube/config

- Kubeconfig is not an API resource, but rather a local configuration file
- Kubeconfig can be configured by setting the environment variable `KUBECONFIG` with the path location of the file
- By default it looks for the path `~/.kube/config`

```shell
# Linux/Mac (bash)
export KUBECONFIG="/home/hvitoi/Documents/kubeconfig.yaml"
```

```cmd
rem Windows (cmd)
export KUBECONFIG="C:\Users\A0000000\Documents\kubeconfig.yaml"
```

```powershell
# Windows (powershell)
$env:KUBECONFIG="C:\Users\A0000000\Documents\kubeconfig.yaml"
```

```yaml
# ~/.kube/config
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

  # login using aws eks cli
  - name: my-user
    user:
      exec:
        apiVersion: client.authentication.k8s.io/v1beta1
        command: aws
        args:
          - eks
          - get-token
          - --region
          - us-east-1
          - --cluster-name
          - my-cluster
          - --output
          - json
        env:
          - name: AWS_PROFILE
            value: br-staging-staging
```
