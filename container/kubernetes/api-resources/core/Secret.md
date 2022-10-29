# Secret

- A secret is only sent to a node if a pod on that node requires it.
- Kubelet stores the secret into a `tmpfs` so that the secret is `not written to disk storage`.
- Once the Pod that depends on the secret is deleted, kubelet will delete its local copy of the secret data as well.
- If trying to reference a secret that doesn't exist, the pod won't start

- **Good practices**
  - Not checking-in secret object definition files to source code repositories.
  - Enabling Encryption at Rest for Secrets so they are stored encrypted in ETCD.

## Encoding/Decoding data

```sh
# encode
echo -n "my-top-secret" | base64

# decode
echo -n "bXktdG9wLXNlY3JldA==" | base64 -d
```

## Opaque secret

- Default kind of secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data: # data here must be base64 encoded!
  DB_HOST: bXlzcWw= # mysql
  DB_USER: cm9vdA== # root
  DB_PASSWORD: cGFzcw== # pass
```

## Dockerconfigjson secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: regcred
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: eyJhdXRocyI6eyJwcml2YXRlLXJlZ2lzdHJ5LmlvIjp7InVzZXJuYW1lIjoicmVnaXN0cnktdXNlciIsInBhc3N3b3JkIjoicmVnaXN0cnktcGFzc3dvcmQiLCJlbWFpbCI6Im1haWxAbWFpbC5jb20iLCJhdXRoIjoiY21WbmFYTjBjbmt0ZFhObGNqcHlaV2RwYzNSeWVTMXdZWE56ZDI5eVpBPT0ifX19
```
