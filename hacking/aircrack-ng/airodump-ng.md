# airodump-ng

- Packet sniffer
- Uses an interface of type monitor

## List networks

```shell
# List network sources
airodump-ng "wlp3s0mon" # hop 2.4Ghz networks only
airodump-ng "wlp3s0mon" --band "a" # hop 5GHz networks only
airodump-ng "wlp3s0mon" --band "abg" # 2.4GHz and 5Ghz networks

```

- `BSSID`: MAC address of the target network
- `PWR`: Signal strength (higher the number the stronger)
- `Beacons`: frames sent by the network in order to broadcast its existence
- `#Data,`: number of data packets (frames)
- `#/s`: number of data packets in the last 10 seconds
- `CH`: channel
- `MB`: maximum speed supported
- `ENC`: encryption used by the network
- `CIPHER`: cypher used
- `AUTH`: authentication used
- `ESSID`: name of the network

| BSSID             | PWR | Beacons | #Data, | #/s | CH  | MB  | ENC  | CIPHER | AUTH | ESSID  |
| ----------------- | --- | ------- | ------ | --- | --- | --- | ---- | ------ | ---- | ------ |
| CB:32:E5:22:EE:85 | -1  | 0       | 0      | 0   | -1  | -1  |      |        |      |        |
| 27:EE:52:2A:D0:A1 | -51 | 37      | 17     | 0   | 4   | 130 | WPA2 | CCMP   | PSK  | WiFi-A |
| AB:84:C6:BF:C3:FA | -66 | 27      | 0      | 0   | 6   | 270 | WPA2 | CCMP   | PSK  | WiFi-B |
| D8:77:8B:57:1A:E5 | -73 | 29      | 2      | 0   | 2   | 270 | WPA2 | CCMP   | PSK  | WiFi-C |
| 70:4F:57:91:9A:DD | -74 | 10      | 0      | 0   | 11  | 130 | WPA2 | CCMP   | PSK  | WiFi-D |

## Sniff a network

```shell
# Sniff packets from a network and save to a file
airodump-ng "wlp3s0mon" \
  --bssid "29:EE:52:8F:D0:A3" \
  --channel "44" \
  --write "test"
```

- `test-01.csv`:
- `test-01.kismet.netxml`:
- `test-01.cap`: data captured (sent to and from the target network). Can be opened with wireshark
- `test-01.kismet.csv`:

- `BSSID`: MAC address of the router
- `STATION`: devices connected to the router
- `PWR`: Signal strength
- `Rate`: Speed
- `Lost`: Packets lost
- `Frames`: Packets captured
- `Probe`: if the device is probing for a network

| BSSID             | STATION           | PWR | Rate   | Lost | Frames | Notes | Probes |
| ----------------- | ----------------- | --- | ------ | ---- | ------ | ----- | ------ |
| 29:EE:52:8F:D0:A3 | 41:1C:83:76:2F:55 | -26 | 6e- 0e | 0    | 4      |       |        |
| 29:EE:52:8F:D0:A3 | D3:35:9D:71:D1:58 | -38 | 6e- 6e | 0    | 394    | 1     |        |
