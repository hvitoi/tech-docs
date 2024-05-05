# Race condition

- When a resource is acquired by two or more processed at the same time
- It may lead to resource's inconsistency
- E.g., two functions incrementing a counter at the same time

## Mutual exclusion (Mutex)

- A technique to avoid race conditions
- The resource uses then a `Mutual Exclusion Object` (mutex) that acts like a `lock` to signalize that the resource is being used
- It `synchronizes the threads` so that one waits for the other
- With that, only one process can have access to the resource at a time

- **Cons**
  - May lead to deadlocks
  - May slow down the system since the resource access is now bottlenecked

## Signaling

- A technique to avoid race conditions
- While a signal is on , no other resource can access it
- Uses the `Dekkers's Algorithm` to avoid deadlocks

- Elements: 2 signals + 1 turn indicator
- Pieces

```txt
my_light = on

while other_light == on:
    if current_turn == other:
        my_light = off
        wait until current_turn = my
        my_light = on
access resource
current_turn = other
my_light = off
```
