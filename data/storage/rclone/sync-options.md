# Sync Options

<https://rclone.org/flags/#sync>

## --track-renames & --track-renames-strategy string

<https://rclone.org/docs/#track-renames-strategy-string>

- Defines what criteria is used to track files that have been renamed

- `modtime`: modification time
- `hash`: hash of the file contents. Not supported on crypt remotes
- `leaf`: the file name
- `size`: the file size. This is always checked
