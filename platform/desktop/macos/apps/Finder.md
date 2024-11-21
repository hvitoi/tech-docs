# Finder

## Recents Folder

- In order to disable the recent items in Finder you need to:
  - `System Settings` -> `Control Center` -> `Recent document, applications, and servers` select "None"

- **Spotlight**
  - Even after disabling "recent files" spotlight is still able to scan through the filesystem and get recently opened files. In order to change this behavior you need to deny access to your device's Storage to `Spotlight`
  - `System Settings` -> `Spotlight` -> `Search Privacy` and select your home folder
  - This might also affect your search in Spotlight directly

## Applications Folder

The application shortcut at finder compiles all the apps in your computer, including the folders:

- **/Applications**
  - Applications installed by the user

- **/System/Applications**
  - MacOS built-in applications

## Shortcuts

- `Cmd + Shift + G`: go to location
- `Cmd + Shift + .`: show hidden files

```shell
defaults write com.apple.Finder AppleShowAllFiles true
```
