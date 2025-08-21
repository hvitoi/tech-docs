# plist

- A `property list` is a file format used on macOS and iOS to store serialized data, mostly application preferences and settings.
- It comes from the NeXTSTEP days (before macOS) and is deeply integrated into Apple's frameworks.
- A plist can be either `XML plist` or `Binary plist`
  - Historically it has been XML, but more recently binary is adopted (smaller and faster to parse)

- Location: You'll see them in `~/Library/Preferences/` or `/Library/Preferences/`
  - Example: ~/Library/Preferences/com.googlecode.iterm2.plist

```shell
# Check the plist format
file ~/Library/Preferences/com.googlecode.iterm2.plist

# read content from a binary plist
plutil -p ~/Library/Preferences/com.googlecode.iterm2.plist
```

```xml
<!-- XML plist (easier to version-control) -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>WindowFrame</key>
    <string>100 100 800 600</string>
    <key>ShowStatusBar</key>
    <true/>
</dict>
</plist>
```
