# Install macOS

- This app is either available:
  - In user space (downloaded from the `App Store`)
  - In Recovery mode (the same installer version as your current macos installation)

- The installer will ask in which volume you want to install the system
  - Can be used to reinstall the current macOS installation
  - Can be used to install a new system as a secondary macOS installation (dual boot) in a new volume

## Bootable Installer

- You can create a bootable USB drive from the MacOS installer

```shell
/Aplications/Install\ macOS\ Ventura.app/Contents/Resources/createinstallmedia --volume /Volumes/MyUsbDrive
```

- The `Bootable Installer` can then be launched from iBoot

## MDM bypass

- As soon as the installation completes and the first setup appear, exit it (Command+Q) and boot into Recovery
- Once in Recovery, mount the Data partition

### Recovery

```shell
# Skip the user setup
touch '/Volumes/Vaporwave - Data/private/var/db/.AppleSetupDone'
```

```shell
# Change the root password so that you can log in with it
node_database='/Volumes/Vaporwave - Data/private/var/db/dslocal/nodes/Default'
dscl -f "$node_database" localhost -passwd "/Local/Default/Users/root"
```

### Root user

- Start the system and log in with the root account

```conf
# /etc/hosts
0.0.0.0 iprofiles.apple.com
```

```shell
# Create your user
sysadminctl -addUser myself -admin -password - -adminUser root -adminPassword -

# Enable secure token for the new user (necessary for filevault)
sysadminctl -secureTokenOn myself -password - -adminUser root -adminPassword -
```

### Conventional User

```shell
# Disable the root account
dsenableroot -d
```

```conf
# /etc/fstab
LABEL=Macintosh\040HD none auto noauto
LABEL=Macintosh\040HD\040-\040Data none auto noauto
```

- You may want to enable `FileVault` in system settings
