# kms

```shell
# Encryption
aws kms encrypt \
  --region "eu-west-2" \
  --key-id "alias/tutorial" \
  --plaintext "fileb://example.txt" \
  --query "CiphertextBlob" \
  --output "text" \
  > "encrypted-text.base64" # outputs the encrypted file in base64


# Decryption (KMS knows already which key to use)
aws kms decrypt \
  --region "eu-west-2" \
  --ciphertext-blob "fileb://encrypted-text" \
  --query "Plaintext" \
  --output "text" \
  > "decrypted-text.base64"
```
