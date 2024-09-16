# idevicerestore

- Restore from extreme circumstances (i.e. something messed up the recovery partition, or partition table), your Mac may fail to boot.
- On the Mac mini this state is identifiable by a flashing orange power light indicating the Morse code for SOS
- On a Mac laptop, this state is identifiable by an illustration of an exclamation point in a circle on the screen with a link to Apple's website

- To restore from this state can use `idevicerestore` from another computer (Mac or Linux)
- This process requires you to unrecoverably destroy all data on the Mac's internal drive
- Connect to the other computer and invoke `DFU mode`

- <https://github.com/tpwrules/nixos-apple-silicon/blob/main/docs/uefi-standalone.md#recovering-from-boot-failure-with-idevicerestore>
