# Asymmetric encryption

- Asymmetric cryptography is also called "public-key cryptography"

- `Public Key`: shared with everyone
- `Private Key`: kept secret

![Asymmetric encryption](./images/asymmetric-encryption.png)

- Both keys have the same length
- Asymmetric keys allow signing and verifying signatures

## Encryption & Signing Algorithms

### RSA (Rivest-Shamir-Adleman)

- It's based on the difficulty of factoring large prime numbers
- Can be used for encryption and digital signature
- Widely used, but slower and uses large key sizes compared to modern algorithms

- Sizes
  - 1024 bits
  - 2048 bits (default)
  - 3072 bits
  - 4096 bits

```shell
ssh-keygen -t "rsa" # output both keys (private and public)
openssl genrsa # output private key only (public can be extracted from the private)
```

- Variations
  - **RS256** (RSA Signature with SHA-256): for signing only

## Signing-only Algorithms

### ECDSA (Elliptic Curve Digital Signature Algorithm)

- A variant of DSA, but based on the math of elliptic curves
- Mainly used for digital signatures
- Provides strong security with much smaller keys than RSA
- Very common in modern systems (e.g., TLS certificates, Bitcoin, SSH)

- Variations
  - **ES256** (ECDSA with SHA-256)

### EdDSA (Edwards-curve Digital Signature Algorithm)

- Elliptic curve, but with modern optimizations (Ed25519, Ed448).
- Used in SSH (newer keys), modern cryptocurrencies, OpenPGP.
