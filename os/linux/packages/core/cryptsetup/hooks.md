# Initramfs Hooks

## Hook: encrypt

### cryptdevice

- Specifies the encrypted root device

```conf
cryptdevice=device:dmname:options
```

- `device`: e.g., /dev/sda1
- `dmname`: e.g., foo (will be available as /dev/mapper/foo)

### cryptkey

```conf
cryptkey=device:fstype:path
```

## Hook: sd-encrypt

- `systemd-cryptsetup-generator` is using during the initramfs stage when using the mkinitcpio hook `sd-encrypt`
- `/etc/crypttab.initramfs` is copied over as `/etc/crypttab` in the initramfs filesystem

### rd.luks.uuid

- The UUID of the crypted filesystem to be unlocked

```conf
rd.luks.uuid=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

- By default, the mapped device will be located at `/dev/mapper/luks-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`

### rd.luks.name

- With this option, rd.luks.uuid can be ommited

```conf
rd.luks.name=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=name
```

- Will be mapped as `/dev/mapper/name`

### rd.luks.key

```conf
rd.luks.key=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=/path/to/keyfile
```

### rd.luks.options

```conf
rd.luks.options=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=options
rd.luks.options=timeout=10s,discard,password-echo=no,tries=1
```
