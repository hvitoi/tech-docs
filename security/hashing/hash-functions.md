# Hash functions

- A a hash function takes an input and produces hash value known as a `message digest`

## General-purpose

### MD5 (Message-digest algorithm)

- Size: `128 bits` - `16 bytes` - `32 hex`

```shell
cat file.txt | md5sum
# 930db08d7fb48a7e8a524e736f7acae9
```

### SHA-1 (Secure Hash Algorithm 1)

- `SHA-1`: 160-bit (20-byte)
- Tipically rendered as a 40 hexadecimal digits
- Applications: git

```shell
# SHA1 hash
echo -n "Hello" | shasum
```

- Number of different hashes from `SHA1` hash function
  - 2^160 = 16^40 = 1.461501637×10^48
- Chance of producing same exact hash for different files in `SHA1` (`Dice theory`)
  - Probability of each SHA1 hash: 1/(2^160)
  - Probability of same exact hash: (1/(2^160))\*(1/\_(2^160)) = 1/(2^320)
- Chance of producing any exact hash for different files in `SHA1` (`Hash collision probability`)
  - Probability of same any hash: for 2 files: 2.84\*10^49
  - The probability increases with more files. E.g., 3 files -> 2.05\*10^48

### SHA-2 (Secure Hash Algorithm 2)

- `SHA-224`: 224-bit (28-byte)
- `SHA-256`: 256-bit (32-byte)
- `SHA-384`: 384-bit (48-byte)
- `SHA-512`: 512-bit (64-byte)

```shell

# SHA256 hash
echo -n "Hello" | shasum -a 256

# SHA512 hash
echo -n "Hello" | shasum -a 512
```

## Password hashing

- Also known as "key derivation functions"
- Designed to be slow to resist brute-force attacks

- `bcrypt`: Strong, widely supported, adds salt automatically.
- `scrypt`: Memory-hard, useful against GPU attacks.
- `PBKDF2`: Iterative key derivation, configurable iterations.
- `Argon2`: Winner of the Password Hashing Competition (PHC); very secure and memory-hard.

## Non-cryptographic

- Also known as "fast hash functions"
- Used for hash tables, checksums, or detecting accidental changes—not for security.

- `MurmurHash`: Very fast, good distribution
- `CityHash` / `FarmHash` / `MetroHash`: High-performance hashing for large data
- `FNV-1a`: Simple, fast, good for small data sets

## Checksums / error detection

- `CRC32`: common for files and network packets
- `Adler-32`: faster than CRC32 for small data
