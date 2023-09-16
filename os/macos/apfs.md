# Apple Filesystem

- Replaces `HFS+` (MacOS Extended)

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
