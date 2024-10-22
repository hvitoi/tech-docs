# ssh-add

- Add keys to client
- Example: add old private key to a new computer

```shell
# If no args are provided, adds ~/.ssh/id_rsa, ~/.ssh/id_dsa, ~/.ssh/id_ecdsa. ~/ssh/id_ed25519, and ~/.ssh/identity, if they exist.
ssh-add

# Add a specific private key
ssh-add ~/.ssh/id_rsa

# MacOS (if you are getting the error: failed to retrieve git folder: failed to clone ref 'refs/heads/main': ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain)
ssh-add --apple-use-keychain ~/.ssh/id_rsa

 # Print ssh public keys
ssh-add -L
```
