# Instructions

## SSH Keys

- SSH keys must be created before

```sh
# Create SSH Key
ssh-keygen \
  -m "PEM" \
  -t "rsa" \
  -b "4096" \
  -C "azureuser@myserver" \
  -f "./aksprodsshkey" \
  -N "mypassphrase"
```

## Users

- Create an AD user in the admin group to test the connectivity
