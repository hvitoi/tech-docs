# ssh-add

- Add keys to client

```shell
# Start the SSH authentication agent (and print the process id)
eval "$(ssh-agent -s)"

# Add old private key to a new computer
ssh-add # Without arguments (adds ~/.ssh/id_rsa, ~/.ssh/id_dsa, ~/.ssh/id_ecdsa. ~/ssh/id_ed25519, and ~/.ssh/identity, if they exist.)
ssh-add "/path/to/private_key" # Specific private key
ssh-add ~/.ssh/id_rsa
ssh-add -L # Print ssh public keys
```

- Private key `~/.ssh/id_rsa` must have permission 400 (or 600)
- Public key `~/.ssh/id_rsa.pub` must have permission 644
