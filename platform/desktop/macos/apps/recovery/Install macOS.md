# Install macOS

- This app is either available:
  - In user space (downloaded from the `App Store`)
  - In Recovery mode (the same installer version as your current macos installation)
  - As a bootable installer. You can create a bootable USB drive from the MacOS installer `/Aplications/Install\ macOS\ Ventura.app/Contents/Resources/createinstallmedia --volume /Volumes/MyUsbDrive`, it can then be launched from iBoot

## Installation

- The installer will ask in which volume you want to install the system

1. Can be used to reinstall the current macOS installation
2. Can be used to install a new system as a secondary macOS installation (dual boot) in a new volume
    - If you're making a second installation, create first the plain APFS volume (no encryption needed) via Disk Utility
    - You will need to set a owner for this new volume (with one of the users of the existing installation). If you want to keep then segregate, do not mark "copy account settings"

## MDM bypass

- As soon as the installation completes and the first setup appear, exit it (Command+Q) and boot into Recovery
- Once in Recovery, mount the Data partition

### At Recovery

```shell
# Mount the new Data volume
diskutil list # get the volume id
diskutil mount diskXsY
```

- See [MDM Hosts](../../cli/profiles.md#mdm-hosts)

```shell
# Block MDM server connection
echo "0.0.0.0 iprofiles.apple.com" >> '/Volumes/Vaporwave - Data/private/etc/hosts'
echo "0.0.0.0 mdmenrollment.apple.com" >> '/Volumes/Vaporwave - Data/private/etc/hosts'
echo "0.0.0.0 deviceenrollment.apple.com" >> '/Volumes/Vaporwave - Data/private/etc/hosts'
echo "0.0.0.0 acmdm.apple.com" >> '/Volumes/Vaporwave - Data/private/etc/hosts'
echo "0.0.0.0 albert.apple.com" >> '/Volumes/Vaporwave - Data/private/etc/hosts'
echo "0.0.0.0 gdmf.apple.com" >> '/Volumes/Vaporwave - Data/private/etc/hosts'
```

```shell
# Skip the user setup
touch '/Volumes/Vaporwave - Data/private/var/db/.AppleSetupDone'
```

```shell
# Enable the root user and define a password for it
node_database='/Volumes/Vaporwave - Data/private/var/db/dslocal/nodes/Default'
dscl -f "$node_database" localhost -passwd "/Local/Default/Users/root"
```

### Logged as root user

- Start the system and log in with the root account

```shell
# Create your user
sysadminctl -addUser myself -admin -password - -adminUser root -adminPassword -

# Enable secure token for the new user (necessary for FileVault)
sysadminctl -secureTokenOn myself -password - -adminUser root -adminPassword -
```

### Logged as admin user

```shell
# disable root account
dsenableroot -d
```

```conf
# /etc/fstab
LABEL=Macintosh\040HD none auto noauto
LABEL=Macintosh\040HD\040-\040Data none auto noauto
```

```shell
# enable FileVault
sudo fdesetup enable
```

```shell
# verify absence of profiles
profiles status --type enrollment
```
