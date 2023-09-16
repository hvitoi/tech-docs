# dscl

## list

```shell
dscl localhost \
    -list /Local/Default/Users

sudo dscl . -list /Users
```

## read

```shell
# Read all information
dscl localhost \
    -read /Local/Default/Users/root
```

## create

```shell
# Create a new user
dscl localhost \
    -create "/Local/Default/Users/myself"
```

## passwd

- Change password

```shell
# Change root password of a given system
dscl -f "/Volumes/Vaporwave - Data/private/var/db/dslocal/nodes/Default" localhost \
    -passwd "/Local/Default/Users/root"
```

```shell
# Skip graphical user setup
touch "/Volumes/Macintosh - Data/private/var/db/.AppleSetupDone"
```

## delete

- Remove group

```shell
dscl . -delete /Groups/thegroup
dscl . -delete /Users/theuser
```
