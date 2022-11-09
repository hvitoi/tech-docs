# wg-quick

- This requires your conf file to be placed at `/etc/wireguard` (e.g., /etc/wireguard/wg0.conf)
- Alternatevely, use `nmcli connection`

```sh
wg-quick up "wg0"
wg-quick down "wg0"
```
