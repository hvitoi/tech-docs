# nixos-rebuild

- Update the configuration file

```shell
# rebuild and change to the new generation
nixos-rebuild switch

# use new config file and update dependencies
nixos-rebuild switch --upgrade

# rollout to a previous generation
nixos-rebuild switch --rollback

# specify the config file
nixos-rebuild with -I nixos-config "path/to/your/configuration.nix"
```
