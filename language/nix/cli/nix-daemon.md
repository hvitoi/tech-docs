# nix-daemon

```shell
# Run nix daemon manually
nix-daemon
```

```shell
# access the daemon socket
sudo usermod -aG "nix-users" $USER

# nix daemon
systemctl enable "nix-daemon.service"

# add bin folder into your path
echo -n 'export PATH=$PATH:$HOME/.nix-profile/bin' >> "~/.zshrc"
```
