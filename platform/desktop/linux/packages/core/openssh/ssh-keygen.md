# ssh-keygen

- Generate ssh keys
- Private key `~/.ssh/id_rsa` must have permission 400 (or 600)
- Public key `~/.ssh/id_rsa.pub` must have permission 644

```shell
# List existing keys
ls "~/.ssh"

# SSH key-pair generation
ssh-keygen # No options
ssh-keygen -t "rsa" -b "4096" -C "hvitoi@gmail.com" # type RSA
ssh-keygen -t "ed25519" -C "Jenkins SSH keys" # type ED25519
ssh-keygen -f <key-name> # creates foo and foo.pub in the current directory
ssh-keygen -m "PEM" # PEM creates unencrypted private key
```

- `-t` (type): rsa, ed25519, etc
- `-b` (bits): bits for the key
- `-C`: label/comment
- `-f`: output key file name
- `-m`: key format
