# plutil

- Read plist files
- Similar to "defaults" command

```shell
# read content from a binary plist
plutil -p ~/Library/Preferences/com.googlecode.iterm2.plist

# Convert binary → XML (readable) -- in-place
plutil -convert xml1 ~/Library/Preferences/com.googlecode.iterm2.plist

# Convert back to binary -- in-place
plutil -convert binary1 ~/Library/Preferences/com.googlecode.iterm2.plist
```
