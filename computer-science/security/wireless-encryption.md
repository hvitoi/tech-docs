# Wireless encryption

- The security setting defines the type of authentication and encryption used by the router, and the level of privacy protection for data transmitted over its network.

## WEP

- WEP: `Wired Equivalent Privacy`
- Uses an algorithm called RC4
- Each packet is encrypted using a unique `key stream`
  - A random `initialization vector` (IV) with 24 bits is used to generate the key streams
  - IV + Key = key stream

## WPA3 Personal

- `Wi-Fi Protected Access - Personal`
- It's the newest, most secure protocol currently available for Wi-Fi devices
- It works with all devices that support Wi-Fi 6 (802.11ax), and some older devices

## WPA2/WPA3 Transitional

- It's a mixed mode that uses WPA3 Personal with devices that support that protocol, while allowing older devices to use WPA2 Personal (AES) instead.

## WPA2-Personal (WPA2-PSK)

- `Wi-Fi Protected Access - Personal` or `Wi-Fi Protected Access - Pre-Shared Key`
- Can use encryption `TKIP` or `AES`
- It's appropriate when you can't use one of the more secure modes
- In that case, also choose AES as the encryption or cipher type, if available.

## Unsecure security settings

- WPA/WPA2 mixed modes
- WPA Personal
- WEP, including WEP Open, WEP Shared, WEP Transitional Security Network, or Dynamic WEP (WEP with 802.1X)
- TKIP, including any security setting with TKIP in the name
