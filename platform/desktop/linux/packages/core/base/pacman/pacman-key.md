# pacman-key

Add the key that the CI uses to sign the packages

```shell
# Refresh the public keys from packagers
pacman-key --refresh-keys

# Delete key
pacman-key --delete "F1E594"

# Fetch keyid
pacman-key --recv-keys "DEB7F121BAAA6F3E" --keyserver "pgp.mit.edu"

# Sign keyid
pacman-key --lsign-key "DEB7F121BAAA6F3E"

# Refresh database
pacman -Syy
```

```shell
pacman-key --init
pacman-key --populate
pacman-key --refresh-keys
pacman -Syy
```
