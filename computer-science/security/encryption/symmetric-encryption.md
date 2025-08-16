# Symmetric encryption

- The same key encrypts and decrypts the data
- It's also known as `secret-key encryption`
- The encryption key is generated directly from the password
- It is not possible to change the password/key of already encrypted content. In this case the data has to be decrypted and encrypted with a different password

## Algorithms

### AES (Advanced Encryption Standard)

- Uses `block cipher`
  - encrypt fixed-size blocks (AES, DES, Twofish)

- Most widely used today (TLS, VPNs, disk encryption, WiFi WPA2/WPA3)
- Block cipher (operates on fixed-size blocks, usually 128 bits)

- Key sizes:
  - 128 bits
  - 192 bits
  - 256 bits: `AES256`

### CHACHA

- Uses `stream cipher`
  - encrypt data bit by bit or byte by byte (ChaCha20, RC4)
