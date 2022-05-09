# shared_preferences

- Stores key-value database in the device
- Similar to `localstorage` and `sqflite`

- Wraps platform-specific persistent storage for simple data
  - `NSUserDefaults` on iOS and macOS,
  - `SharedPreferences` on Android, etc
- Data may be persisted to disk asynchronously, and there is no guarantee that writes will be persisted to disk after returning
- Supported data types: `int`, `double`, `bool`, `String` and `List<String>`
