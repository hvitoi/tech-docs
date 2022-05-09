# locale-gen

- Edit `/etc/locale.gen` and uncomment en_US.UTF-8 UTF-8 and other needed locales
- The locale.gen command uses that configuration

```shell
# Edit /etc/locale.gen
vi "/etc/locale.gen"

# Generate location configuration
locale-gen

# Create locale.conf
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
```
