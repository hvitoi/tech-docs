# Hashing algorithms

## MD5

- Size: `128 bits` - `16 bytes` - `32 hex`

```shell
cat file.txt | md5sum
# 930db08d7fb48a7e8a524e736f7acae9
```

## SHA

- `SHA1`: 160bits
  - Applications: git
- `SHA256`: 256bit
  - Complex and time consuming
  - Used in applications where you want it to be a expensive operation
  - Applications: security and cryptography
- `SHA384`: 384bit
- `SHA512`: 512bit

```shell
# SHA1 hash
echo -n "Hello" | shasum

# SHA256 hash
echo -n "Hello" | shasum -a 256

# SHA512 hash
echo -n "Hello" | shasum -a 512
```

- Number of different hashes from `SHA1` hash function
  - 2^160 = 16^40 = 1.461501637×10^48
- Chance of producing same exact hash for different files in `SHA1` (`Dice theory`)
  - Probability of each SHA1 hash: 1/(2^160)
  - Probability of same exact hash: (1/(2^160))\*(1/\_(2^160)) = 1/(2^320)
- Chance of producing any exact hash for different files in `SHA1` (`Hash collision probability`)
  - Probability of same any hash: for 2 files: 2.84\*10^49
  - The probability increases with more files. E.g., 3 files -> 2.05\*10^48

## HMAC

- Hash with a key: Additional level of security
