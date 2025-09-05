# Certificates

```shell
# generate kube-apiserver private key
openssl genrsa -out "apiserver.key" "2048"

# certificate signing request
openssl req \
  -new \
  -key "apiserver.key" \
  --config "openssl.cnf" \
  -subj "/CN=kube-apiserver" \
  -out "apiserver.csr"

# sign with ca
openssl x509 \
  -req \
  -in "apiserver.csr" \
  -signkey "ca.key" \ # ca private key
  -out "apiserver.crt"
```

```conf
[req]
req_extensions = v3_req

[v3_req]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation,
SubjectAltName = @alt_names

[alt_names]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster.local
IP.1 = 10.96.0.1
IP.2 = 172.17.0.87
```

```conf
ExecStart=/usr/local/bin/kube-apiserver \\
  ... \\

  # server certificate
  --client-ca-file=/var/lib/kubernetes/ca.pem \\
  --tls-cert-file=/var/lib/kubernetes/apiserver.crt \\
  --tls-private-key-file=/var/lib/kubernetes/apiserver.key \\

  # client certificate (to connect with etcd)
  --etcd-cafile=/var/lib/kubernetes/ca.pem \\
  --etcd-certfile=/var/lib/kubernetes/apiserver-etcd-client.crt \\
  --etcd-keyfile=/var/lib/kubernetes/apiserver-etcd-client.key \\

  # client certificate (to connect with kubelet)
  --kubelet-client-certificate=/var/lib/kubernetes/apiserver-kubelet-client.crt \\
  --kubelet-client-key=/var/lib/kubernetes/apiserver-kubelet-client.key \\
```
