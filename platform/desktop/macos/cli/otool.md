# otool

- Inspect a binary's metadata
- Useful to identify which libraries are associated with a command
  - `/System/Library/Frameworks/CoreData.framework`
  - `/System/Library/Frameworks/CoreFoundation.framework`
  - `/System/Library/Frameworks/CoreServices.framework`
  - `/System/Library/Frameworks/DirectoryService.framework`
  - `/System/Library/Frameworks/DiskArbitration.framework`
  - `/System/Library/Frameworks/Foundation.framework`
  - `/System/Library/Frameworks/LocalAuthentication.framework`
  - `/System/Library/Frameworks/OpenDirectory.framework`
  - `/System/Library/Frameworks/Security.framework`
  - ...

```shell
otool -L /usr/bin/du
```
