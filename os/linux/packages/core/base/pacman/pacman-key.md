# pacman-key

Add the key that the CI uses to sign the packages

```shell
# Manually installing it
sudo pacman-key --recv-keys "DEB7F121BAAA6F3E" --keyserver "pgp.mit.edu"

# if you get an unknown trust issue, try signing the key manually
sudo pacman-key --lsign-key "DEB7F121BAAA6F3E"

# Refresh the public keys from packagers
pacman-key --refresh-keys
```
