# dscl

```shell
# Manage the users on a given system
dscl_path='/Volumes/Vaporwave - Data/private/var/db/dslocal/nodes/Default'

# Skip graphical user setup
touch '/Volumes/Macintosh - Data/private/var/db/.AppleSetupDone'
```

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

# Create a new user on a given system
dscl -f "$dscl_path" localhost \
    -create "/Local/Default/Users/myself"
```

## passwd

- Change password

```shell
# Change root password on a given system
dscl -f "$dscl_path" localhost \
    -passwd "/Local/Default/Users/root"
```

## delete

- Remove group

```shell
dscl . -delete /Groups/thegroup
dscl . -delete /Users/theuser
```
