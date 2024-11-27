# openssl

## genrsa

- Generate key

```shell
# Generate RSA private key
openssl genrsa # 2048 by default.
openssl genrsa -out "private.key" # output to a file
openssl genrsa "4096" # specify key size

# Generate and encrypt it with a passphrase
openssl genrsa -aes256
openssl genrsa -des3

# Output to a file
openssl genrsa -aes256 -out "private.key" # PEM is the extension for keys
```

## rsa

- Extract public from a private key

```shell
# Retrieve public key from a private key
openssl rsa \
  -in "private.key" \
  -pubout \
  -outform "PEM" \
  -out "public.key"
```

## req

- Certificate Signing Request (CSR)

- `CN`: Common name. Can be anything
- `C`: Contry
- `ST`: State
- `O`: Organization

```shell
# Simple CSR
openssl req \
  -new \
  -key "private.key" \
  -subj "/C=US/ST=CA/O=MyOrg, Inc./CN=mydomain.com" \
  -out "cert.csr"
```

```shell
# Certificate Signing Request (CSR) with openssl config file
openssl req \
  -new \
  -key "private.key" \
  --config "openssl.cnf" \
  -subj "/C=US/ST=CA/O=MyOrg, Inc./CN=mydomain.com" \
  -out "cert.csr"
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

## x509

- Sign Certificates

```shell
# Sign CSR
openssl x509 \
  -req \
  -in "cert.csr" \
  -signkey "ca.key" \ # private key to sign with
  -out "cert.crt"
```

```shell
# Inspect Certificate
openssl x509 \
  -text \
  -noout \
  -in "cert.crt"
```

```shell
# Get the system CA certificates
awk -v cmd='openssl x509 -noout -subject' '
    /BEGIN/{close(cmd)};{print | cmd}' < /etc/ssl/certs/ca-certificates.crt
```

## s_client

- Test Connectivity

```shell
# Test connectivity
openssl s_client -connect "20.244.9.3:9093"
```
