# profile

- Profiles Settings: `/var/db/ConfigurationProfiles/Settings/`

```shell
# Lists MDM Enrollment Profiles
profiles show -type enrollment
profiles remove -all
```

## Mobile Device Management (MDM)

- It's a way to manage apple computers remotely
  - FileVault encryption

```conf
# MDM hosts
0.0.0.0 iprofiles.apple.com
0.0.0.0 mdmenrollment.apple.com
0.0.0.0 deviceenrollment.apple.com
```
