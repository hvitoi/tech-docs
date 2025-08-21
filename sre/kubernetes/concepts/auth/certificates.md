# Certificates

- All the communication between the Kubernetes components are TLS `encrypted`

![Cluster Encryption](.images/cluster-encryption.png)

- For encryption, certificates are necessary

![Cluster Certificates](.images/cluster-certificates.png)
![Cluster Certificates](.images/cluster-certificates2.png)

## Certificate Properties

- `CN`: Common Name. Name of the component. E.g., system:node:node01
- `O`: Organization. Specify the group. E.g, SYSTEM:NODES

## Certificate Path

- Path for manual installation: `/var/lib/kubernetes/`
- Path for kubeadm installation: `/etc/kubernetes/pki/`

## Certificate API

- The `Certificate Authority (CA)` and the `CA Server` is in the `master nodes`
- The CA private keys are stored in the master nodes
- The CA in kubernetes has the `Common Name (CN)` `kubernetes`

- `The Certificate API` is useful to avoid manually ssh into the master node to sign a certificate
- With the certificate API, the CSR is created as a `CertificateSigningRequest` resource and can be reviewed and approved via kubectl
- All the certificate operations are carried out by the `Controller Manager`
  - It has the `CSR-APPROVING` and `CSR-SIGNING`controllers

```shell
# generate private key
openssl genrsa -out "henry.key" "2048"

# create csr
openssl req \
  -new \
  -key "henry.key" \
  -subj "/CN=henry" \
  -out "henry.csr"

# encode csr
cat "henry.csr" | base64
```

```yaml
apiVersion: certificates.k8s.io/v1beta1
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
