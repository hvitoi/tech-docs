# locale-gen

- Edit `/etc/locale.gen` and uncomment en_US.UTF-8 UTF-8 and other needed locales
- The locale.gen command uses that configuration

```shell
# Edit /etc/locale.gen
vi "/etc/locale.gen"

# Generate location configuration
locale-gen

# or simply
locale-gen "en_US.UTF8"
```
