# Finder

## Recent Files

- In order to disable the recent items in Finder you need to:
  - `System Settings` -> `Control Center` -> `Recent document, applications, and servers` select "None"

## Shortcuts

- `Cmd + Shift + G`: go to location
- `Cmd + Shift + .`: show hidden files

```shell
defaults write com.apple.Finder AppleShowAllFiles true
```

## Spotlight

- Even after disabling "recent files" spotlight is still able to scan through the filesystem and get recently opened files. In order to change this behavior you need to deny access to your device's Storage to `Spotlight`
  - `System Settings` -> `Spotlight` -> `Search Privacy` and select your whole HDD
- This will also affect you search for apps in Spotlight directly
