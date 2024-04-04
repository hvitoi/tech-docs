# csrutil

- `System Integrity Protection` ("rootless") is a security feature that protects some files and directories from being modified — even from the root user.

```shell
# Disable SIP completely
csrutil disable

# Enable SIP
csrutil enable

# Enable SIP with exceptions
csrutil enable --without fs --without debug --without nvram

# Get SIP status (if the system is sealed)
csrutil status
csrutil authenticated-root status
csrutil authenticated-root disable # allow changing the SSV
```
