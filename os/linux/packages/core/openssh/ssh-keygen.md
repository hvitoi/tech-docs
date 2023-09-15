# ssh-keygen

- Generate ssh keys

```shell
# List existing keys
ls "~/.ssh"

# SSH key-pair generation
ssh-keygen # No options
ssh-keygen -t "rsa" -b "4096" -C "hvitoi@gmail.com" # type RSA
ssh-keygen -t "ed25519" -C "Jenkins SSH keys" # type ED25519
ssh-keygen -f "key-name" -m "PEM" # Set name and create in the current directory. PEM creates unencrypted private key
```

- `-t` (type): rsa, ed25519, etc
- `-b` (bits): bits for the key
- `-C`: label/comment
- `-f`: output key file name
- `-m`: key format
