# profile

- Profiles Settings: `/var/db/ConfigurationProfiles/Settings/`

## list

- List installed profiles

```shell
profiles list
```

## status

```shell
# status of all profiles installed
profiles status

# Show if there are enrollment profiles (DEP or MDM)
profiles status --type enrollment
```

## show

```shell
# Lists MDM Enrollment Profiles (fetched from server DEP configuration)
profiles show -type enrollment
```

## remove

```shell
profiles remove -all
```

## Mobile Device Management (MDM)

- It's a way to manage apple computers remotely

```conf
# MDM host
0.0.0.0 iprofiles.apple.com
```

```conf
# Other hosts
0.0.0.0 mdmenrollment.apple.com
0.0.0.0 deviceenrollment.apple.com
0.0.0.0 albert.apple.com
0.0.0.0 acmdm.apple.com
0.0.0.0 gdmf.apple.com # system updates
```

- Daemons
  - `/System/Library/LaunchDaemons/com.apple.ManagedClient*`
  - `/System/Library/LaunchDaemons/com.apple.mdmclient*`
- Agents
  - `/System/Library/LaunchAgents/com.apple.ManagedClient*`
  - `/System/Library/LaunchAgents/com.apple.mdmclient*`

```shell
# Disable all daemons and agents
launchctl disable system/com.apple.ManagedClientAgent.enrollagent
launchctl disable system/com.apple.mdmclient.daemon
launchctl disable system/com.apple.devicemanagementclient.teslad
```

```shell
# test
/usr/libexec/teslad
/usr/libexec/mdmclient
```

## Device Enrollment Program (DEP)

- Similar to MDM
