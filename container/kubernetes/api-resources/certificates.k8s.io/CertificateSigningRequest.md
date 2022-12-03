# CertificateSigningRequest

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: henry
spec:
  groups:
    - system:authenticated
  usages:
    - digital signature
    - key encipherment
    - server auth
  request: LS0tLkasRIJDHKAHK81LS0tLkasRIJDHKAHK81...
```

```shell
kubectl get csr
kubectl certificate approve "henry"
```

- After approval, the CSR resource will have a new "certificate" field which can then be shared with the user
