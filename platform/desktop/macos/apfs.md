# Apple Filesystem

- Replaces `HFS+` (MacOS Extended)

## Concepts

- `Container`: contains volumes
- `Volume Group`: logically classify volumes
- `Volume`: unit of filesystem inside of containers

- `Volume Name`: the "LABEL"
- `Volume UUID`: the "UUID"

## Chracteristics

- **Space sharing**

  - Volumes inside of a container share free space
  - However, `reserved` and `quota` sizes that also be defined

- **Cloning**

  - Cloning a file happens instantly and takes no additional space
  - This is possible due to `Copy-On-Write` (COW)
  - Only new changes are stored
  - That open possibilities for `Snapshots`
  - `Time Machine` is used to manage snapshots

- **Atomic safe-save**

  - Guarantees atomic save even for document bundles (documents that are actually folders with multiple files)

## Container Roles

- **Data**
  - Sealed: no
  - FileVault: yes
  - Encrypted: yes
- **System**
  - Sealed: yes
  - FileVault: yes
  - Encrypted: no
  - Snapshot is taken from it
- **Preboot**
  - Sealed: no
  - FileVault: no
- **VM**
  - Sealed: no
  - FileVault: no
- **Recovery**
  - Sealed: no
  - FileVault: no

### Special Containers

- On Apple Silicon machines, there are 2 special APFS containers
  - **iBoot System Container**
    - Type: `Apple_APFS_ISC`
    - The first partition on the disk
  - **System Recovery**
    - Type: `Apple_APFS_Recovery`
    - The last one on the disk
- These partitions should never be touched

## Crypto Users/Keys (APFSCryptoUserType)

- Get the crypto users for a given APFS filesystem using `fdesetup list -extended` or `diskutil apfs listCryptoUsers diskX`

- **Local Open Directory User** / OS User / LocalOpenDirectory
  - A local user
  - It has a unique UUID for every new user created
- **Personal Recovery User** / Personal Recovery Record / PersonalRecovery / PRK
  - Alphanumeric string generated at the time of encryption
  - Its UUID is the same for every File Vault 2 encrypted MacOs in the world: EBC6C064-0000-11AA-AA11-00306543ECAC
- **MDM Bootstrap Token External Key** / Bootstrap Token / MDMRecovery
  - This key is managed by an organization
  - It's unique for a mac computer, even on fresh installs
- **Institutional Recovery Key** / IRK

## Signed System Volume (SSV)

- It's a `read-only` system volume
- SSV features a kernel mechanism that verifies the integrity of the system content at runtime
- SSV uses APFS snapshots to be mounted on the root filesystem
- The root node's hash value of the SSV snapshot is called a `seal`
- The seal of the filesystem can be broken due to being mounted as writable in the past (even if it doesn’t modify any files or metadata). But the only important seal is the snapshot
- Also referred to as "Sealed System Volume"

## fstab

```conf
LABEL=Macintosh\040HD none auto noauto
LABEL=Macintosh\040HD\040-\040Data none auto noauto
```
