# Iterator

- Traverse through a collection
- `for` is an abstraction for iterator
- The object must have the `next()` method that returns the next element in the collection

```typescript
function range(start: number, end: number, step = 1) {
  return {
    [Symbol.iterator]() {
      return this;
    },
    next() {
      if (start < end) {
        start = start + step;
        return { value: start, done: false };
      }
      return { done: true, value: end };
    },
  };
}

for (const n of range(0, 100, 5)) {
  console.log(n);
}
```
