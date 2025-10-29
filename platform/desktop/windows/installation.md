# Installation

- Press `Shift + F10` to open terminal at installation

## Bootable Media

- **Rufus**: <https://github.com/pbatard/rufus> (Windows)
- **WinDiskWrite**: <https://github.com/TechUnRestricted/WinDiskWriter> (MacOS)
- For older system it has to be formatted in FAT-32 (ExFAT won't be recognized)

- Installation ISO
  - <https://www.microsoft.com/pt-br/software-download/windows11>
  - If installing in a VM, make sure it has at least 2 cores set up, UEFI and TPM enabled

## Bypass Hardware Check

- **Rufus**
  - It's possible to include some "registry hacks" that allow installing W11 on unsupported hardware

- **W11 Server Installation** (upgrading from W10)
  - Run the W11 installation from cmd
  - `E:\setup.exe /product server`
  - Make sure to also disable updates during the setup
  - <https://www.youtube.com/watch?v=q3aWGBkH9P4>

- **W11 Clean Installation**
  - Press `Shift + F10` to open regedit during the installation
  - Add registry to bypass certain hardware verification
  - DWORD Value (32-bit) `HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig\BypassTMPCheck` = 1 (hex)
  - DWORD Value (32-bit) `HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig\BypassCPUCheck` = 1 (hex)

## Answer files (unattend.xml)

- <https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs>
- <https://schneegans.de/windows/unattend-generator/>
- <https://www.youtube.com/watch?v=JUTdRZNqODY>

- Answer files need to be included to the root of the installation media
  - `unattend.xml`
  - `autounattend.xml`
