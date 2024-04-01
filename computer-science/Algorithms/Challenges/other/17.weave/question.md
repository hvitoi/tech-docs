# Questions

- Weave-receives two queues as arguments and combines the contents of each into a new, third queue.
- The third queue should contain the alterating content-of the two queues.
- The function should handle queues of different lengths

- Example

```javascript
const queueOne = new Queue();
queueOne.add(1);
queueOne.add(2);

const queueTwo = new Queue();
queueTwo.add('Hi');
queueTwo.add('There');

const q = weave(queueOne, queueTwo);

q.remove() // 1
q.remove() // 'Hi'
q.remove() // 2
q.remove() // 'There'
```
