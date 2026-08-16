# Global Flags

- <https://rclone.org/flags/>

## Copy Flags

### --checksum

<https://rclone.org/docs/#c-checksum>

- By default rclone looks at the `modification time` and `file size` to determine two files are equal
- When this is enabled, it checks the `file hash` and `file size`
- Crypt remotes do not support it

### --size-only

<https://rclone.org/docs/#size-only>

- By default rclone looks at the `modification time` and `file size` to determine two files are equal
- When this is enabled, it checks only the `file size`

### --modify-window

<https://rclone.org/docs/#modify-window-duration>

- This is the time difference tolerance between the two files to be considered the same
- On MacOS this should be 1s

## Sync Flags

### --track-renames & --track-renames-strategy string

<https://rclone.org/docs/#track-renames-strategy-string>

- Defines what criteria is used to track files that have been renamed

- `modtime`: modification time
- `hash`: hash of the file contents. Not supported on crypt remotes
- `leaf`: the file name
- `size`: the file size. This is always checked
