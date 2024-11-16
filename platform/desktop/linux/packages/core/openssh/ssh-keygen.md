# ssh-keygen

- Generate ssh keys
- Private key `~/.ssh/id_rsa` must have permission 400 (or 600)
- Public key `~/.ssh/id_rsa.pub` must have permission 644

```shell
# List existing keys
ls "~/.ssh"

# Create a SSH key-pair at ~/.ssh (id_rsa & id_rsa.pub)
ssh-keygen
```

## -t (Key Type)

- rsa
- ed25519
- ed25519-sk
- ecdsa
- ecdsa-sk
-

```shell
ssh-keygen -t "rsa"
```

## -b (Bits)

- Specifies the number of bits in the key to create
- For RSA keys, the minimum size is 1024 bits and the default is 3072 bits.  Generally, 3072 bits is considered sufficient.

```shell
ssh-keygen -b "4096"
```

## -C (Comments)

```shell
ssh-keygen -C "user@example.com"
ssh-keygen -C "My Awesome Key"
```

## -m (Key Format)

```shell
ssh-keygen -m "PEM"
```

- **RFC4716**
  - RFC 4716/SSH2 public or private key
- **PKCS8**
  - PKCS8 public or private key
- **PEM**
  - PEM public key

- **-----BEGIN OPENSSH PRIVATE KEY-----**
  - OpenSSH proprietary format introduced in OpenSSH 6.5 (2014)
  - Uses the OpenSSH-specific encoding for private keys
  - This format can encapsulate various `key types` like:
    - RSA
    - Ed25519
    - ECDSA
    - DSA

- **-----BEGIN RSA PRIVATE KEY-----**
  - This is a `PEM-encoded` `PKCS#1` or `PKCS#8` private key
  - The key is stored in PEM (Privacy-Enhanced Mail) format, which is Base64-encoded ASN.1 DER data
  - It predates the OpenSSH-specific format
  - Contains only RSA private keys
  - It is compatible with a wide range of applications beyond OpenSSH, such as SSL/TLS libraries (e.g., OpenSSL)

## -f (Filename)

- Output key file name

```shell
ssh-keygen -f "foo" # creates foo and foo.pub in the current directory
```
