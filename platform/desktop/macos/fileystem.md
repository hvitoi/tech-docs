# Filesystem

## System Volume

System volume is mounted into root `/`

## Data Volume

Data volume is mounted into `/System/Volumes/Data`

- **/home**
  - Symlinked to `<DataMountpoint>/home`
  - Usually empty. The actually home dir is located at `/Users/<user>`
