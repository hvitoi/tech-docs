# Proxy

- Replace the target object with a proxy
- Allows new logic to be introduced to the target (side effects)

```typescript
const original = { name: "jeff" };

// target (original), proxy (reactive)
// takes a target (1st arg) and a handler (2nd arg)
const reactive = new Proxy(original, {
  get(target, key) {
    console.log("Tracking: ", key);
    return target[key];
  },
  set(target, key, value) {
    console.log("updating UI...");
    return Reflect.set(target, key, value);
  },
});

reactive.name; // 'Tracking: name'
reactive.name = "bob"; // 'updating UI...'
```
