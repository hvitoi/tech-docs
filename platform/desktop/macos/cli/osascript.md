# osascript

- `AppleScript` is a scripting language created by Apple, primarily used to automate tasks on macOS
- File extensions
  - `.applescript`: plain text format. It is compiled just before the execution
  - `.scpt`: compiled app
- Place scripts at `~/Library/Scripts/` to run them from menu bar

```applescript
tell application "Finder"
  try
    mount volume "http://127.0.0.1:8080/"
  end try
end tell
```

```applescript
display dialog "Hello, World!"
```

```shell
# Run inline script
osascript -e 'display dialog "Hello, World!"'

## Multiline inline
osascript <<EOF
tell application "Finder"
    activate
    display dialog "Hello from Finder!"
end tell
EOF

# Run from file
osascript script.scpt
osascript script.applescript

# With arguments
osascript script.applescript "Henry"
```

```applescript
on run argv
    display dialog "Argument passed: " & item 1 of argv
end run
```
