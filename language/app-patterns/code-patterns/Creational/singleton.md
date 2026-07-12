# Singleton

- An object can be instantiated only once

```typescript
class Settings {
  static instance: Settings;
  public readonly mode = "dark";

  // prevent new objects with private constructor
  private constructor() {}

  static getInstance(): Settings {
    if (!Settings.instance) {
      Settings.instance = new Settings();
    }

    return Settings.instance;
  }
}

const settings = new Settings(); // throws error
const settings = Settings.getInstance();
```
