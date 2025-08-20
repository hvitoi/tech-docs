# TCP/IP frames

- The HTTP message carried inside TCP/IP packets/frames

## Packets

- `HTTP Package` consists of several headers
  1. TCP
  1. IP
  1. Ethernet II
  1. Frame

- Each header is built on top of the previous header

```shell
sudo tcpdump -A -i any tcp port 80
```
