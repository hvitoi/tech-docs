# Prototype

- Inheritance from an object that already been created

```typescript
// the object, the prototype
const zombie = {
  eatBrains() {
    return "yum 🧠";
  },
};

// inherit properties from the object + additional properties
const chad = Object.create(zombie, { name: { value: "chad" } });
chad.__proto__; // access proto
Object.getPrototypeOf(chad); // access proto

// further inherit properties
const babyChad = Object.create(chad, { baby: { value: true } });
```
