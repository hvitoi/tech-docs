# iBoot

- It's the apple's boot firmware
- Version: `iBoot-11881.1.1`

## MacOS installation

- A macOS installation is composed of:
  - `System Volume`: "Macintosh"
  - `Data Volume`: "Macinttosh - HD"
  - `Preboot Volume`: a nested directory (named as the id of the VG) inside of the preboot volume

- The system & data volumes are grouped in a single Volume Group (VG)

## LocalPolicy

- A `LocalPolicy` can be created by using for a macOS installation using `bless` or `bputil`.
- It basically sets the a macOS installation (the VG) as the `default boot VGID`

## System Volume

### .IAPhysicalMedia

The file `IAPhysicalMedia.plist` can be placed at the root of the system volume. It indicates which entrypoint executable (*.app) needs to be executed on the next boot in 1TR

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
        <key>AppName</key>
        <string>Finish Installation.app</string>
        <key>ProductBuildVersion</key>
        <string>00A191</string>
        <key>ProductVersion</key>
        <string>12.1</string>
</dict>
</plist>
```

This file is usually renamed (e.g., to "IAPhysicalMedia-disabled.plist") to that it won't run on the second boot
