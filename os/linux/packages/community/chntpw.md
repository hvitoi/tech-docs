# chntpw

- Mount Windows
- At `/media/hvitoi/Windows/Windows/System32/config`

```sh
# Regedit
cd "/media/hvitoi/Windows/Windows/System32/config"
chntpw -e SYSTEM

# Check user records in Security Account Manager (SAM)
chntpw -l SAM # list
chntpw -i SAM # edit
```

## Bluetooth pairing on Windows and Linux simultaneously

- Connect device on Linux and afterwards on Windows
- Boot Linux again

```sh
cd "/media/hvitoi/Windows/Windows/System32/config"
chntpw -e SYSTEM
```

```powershell
# Navigate to bluetooth keys folder
cd ControlSet001\Services\BTHPORT\Parameters\Keys # if there is no CurrentControlSet, then try ControlSet001

# List bluetooth ports mac addresses
ls
cd 3413E8C296A0

# Show device connection key
ls
hex 001f20eb4c9a # response like 00000 XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX ...ignore..chars..
```

```txt
Device 5C:C6:E9:A0:BB:15 EDIFIER W800BT
HEX 7EFA5045CA230CE4F6AF6FDDCAA5C863

Device 60:F4:3A:29:91:D0 EDIFIER R1080BT
HEX 2C593CC1A8683DB42A62BBDF78B9CA47

Device 5C:FB:7C:88:FA:49 JBL TUNE110BT
HEX F082CC36B73C800C7FBA9D2225BDAFE6
```

```sh
sudo -s
cd "/var/lib/bluetooth/port-mac/device-mac"
vim info # change to LinkKey to windows key
```
