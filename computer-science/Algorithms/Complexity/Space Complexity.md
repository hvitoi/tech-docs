# Space complexity

- Measures the `memory aspect` of an algorithm
- Measures how much `additional memory` is used as part of execution
- What consumes space/memory?
  - Variables
  - Data structures
  - Function Calls
  - Allocations

## $O(1)$

```javascript
// No assignments are made beyond for counter
function foo(coll) {
  for (let i = 0; i < coll.length; i++) {
    console.log("Hey!");
  }
}
```

## $O(n)$

```javascript
// Memory allocation increases as the input increases
function foo(coll) {
  let hiArr = [];
  for (let i = 0; i < coll.length; i++) {
    hiArr.push('hi');
  }
}
```
