# cryptcheck

- Crypt remote
- `crypt` remote takes another remote as part of its configuration
- It encrypts data and hands it over to the underlying remote
- Everything crypt does is to encrypt and decrypt data

1. Create new remote
1. Choose type "crypt" (Encrypt/Decrypt a remote)
1. Select the origin remote
1. Create passwords
1. Done

```shell
# checks a remote against a crypted remote. It works by reading the nonce from each file on the crypted remote
rclone cryptcheck "/path/to/files" "remote-crypt:path"
```
