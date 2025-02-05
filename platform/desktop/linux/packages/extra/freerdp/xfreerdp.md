# xfreerdp

- A Remote Desktop **client** that supports several protocols
- Protocols
  - `RDP` (Remote Desktop Protocol): proprietary (microsoft)
  - `VNC` (Virtual Network Computing): open source

```shell
xfreerdp /v:"hostname/ip" /u:"username"
xfreerdp /v:"hostname/ip" /d:"domain" /u:"username"
```

## Relay Server

- Acts as a middle man between the server and the client
- It's required for RDP connections over the Internet
- Needs to be hosted in a publicly accessible server (e.g., Linode)
- <https://www.youtube.com/watch?v=EXL8mMUXs88>

## Cloud-Based RDP Server

- **TeamViewer**
- **Anydesk**
- **Rustdesk**
  - <https://github.com/rustdesk/rustdesk>
  - Allows self-hosting

- **Chrome Remote Desktop** (browser-based)
- **Guacamole** (browser-based)
- **KASM VNC** (browser-based)

## Local RDP Server

- Requires both computers to be on the same network
- Alternatively you can connect over the internet using a VPN or port forwarding

- **Microsoft Remote Desktop Connection** (mstsc)
  - Requires Windows Pro edition
