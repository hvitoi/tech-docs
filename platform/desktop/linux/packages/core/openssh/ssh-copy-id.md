# ssh-copy-id

- Install public keys of the clients

- Keys in the server are stored at `~/.ssh/authorized_keys` in the server
- Public keys are important so that server can `authorize` and `decrypt` information from the client

```shell
# Run these commands in the client side!
ssh-copy-id -i "/path/to/key.pub" "user@ssh-server"
ssh-copy-id -i "~/.ssh/id_ed25519.pub" "root@ip"
```
