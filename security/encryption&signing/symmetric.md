# Symmetric encryption

- The same key encrypts and decrypts the data
- It's also known as `secret-key encryption`
- The encryption key is generated directly from the password
- It is not possible to change the password/key of already encrypted content. In this case the data has to be decrypted and encrypted with a different password

## Encryption-only algorithms

### AES (Advanced Encryption Standard)

- Uses `block cipher`
  - encrypt fixed-size blocks (AES, DES, Twofish)

- Most widely used today (TLS, VPNs, disk encryption, WiFi WPA2/WPA3)
- Block cipher (operates on fixed-size blocks, usually 128 bits)

- Key sizes:
  - 128 bits
  - 192 bits
  - 256 bits: `AES256`

### ChaCha20

- Uses `stream cipher`
  - encrypt data bit by bit or byte by byte (ChaCha20, RC4)

## Signing-only algorithms

### HMAC (Hash-based Message Authentication Code)

- Used for signing / authentication (integrity + authenticity, but not encryption)
- Keyed hashing scheme
- Example algorithms:
  - HMAC-SHA256 (used in JWT HS256)
  - HMAC-SHA1
  - HMAC-SHA512

- Variations
  - **HS256** (HMAC with SHA-256)
