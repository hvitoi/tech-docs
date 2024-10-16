# kms

## encrypt

```shell
# Encryption
aws kms encrypt \
  --key-id "alias/tutorial" \
  --plaintext "fileb://example.txt" \
  --query "CiphertextBlob" \
  > "encrypted-text.base64" # outputs the encrypted file in base64
```

## decrypt

```shell
# Decryption (KMS knows already which key to use)
aws kms decrypt \
  --ciphertext-blob "fileb://encrypted-text" \
  --query "Plaintext" \
  > "decrypted-text.base64"
```
