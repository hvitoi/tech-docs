# asr

- `Apple Software Restore` copies volumes (e.g. from disk images)
- There is only one tool that can successfully copy the `Signed System Volume` (SSV), and that is `Apple Software Restore (ASR)`
- Copies full MacOS installations, including
  - System volume
  - Data volume
  - Preboot content
  - Recovery content
- <https://discussions.apple.com/docs/DOC-250005828>

- The procedure must be run from `macOS Recovery` because `System Integrity Protection` blocks most writes to the Preboot volume for the booted macOS
- All macOS installations in a given APFS container share the same Preboot volume, and if the Preboot volume in the destination container is locked (because the current macOS uses it), ASR won’t be able to update it as part of the cloning process.
- macOS Recovery doesn’t have this restriction and freely allows the Preboot volume to be modified.

## restore

- **Source**: the `System` volume (not data, preboot or recovery). E.g., "Macintosh HD"
- **Target**: the container

```shell
# Unlock the data volume (only for FileVault encrypted macos installations)
diskutil list # get disk identifiers
diskutil apfs listvolumegroups
diskutil apfs unlock
```

```shell
# Clone the sealed snapshot
# Stub volumes do not have a snapshot
diskutil mount disk0s0
diskutil apfs listsnapshots disk0s0 # get the snapshot UUID
```

```shell
# Preserve the existing data and volumes inside the destination container and install the clone alongside it
asr restore \
  --source /dev/disk0s0 \ # volume id (the system volume)
  --target /dev/disk0s0 \ # container id
  --no-personalization

# Bless the stub volume in order to make it the default boot volume
bless \
  --setBoot \
  --mount "/Volumes/Foo"
```
