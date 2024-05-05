# Race condition

- When a resource is acquired by two or more processed at the same time
- It may lead to resource's inconsistency
- E.g., two functions incrementing a counter at the same time

```java
class Main {
  public static void main(String[] args) throws InterruptedException {

    counter = new Counter();

    Runnable job = () -> {
      for (int i = 0; i <= 1000; i++) {
        counter.increment();
      }
    };

    Thread t1 = new Thread(job);
    Thread t2 = new Thread(job);

    t1.start();
    t2.start();

    t1.join()
    t2.join()

    System.out.println(c.count); // won't be equal to 2000 (will be around ~1800)

  }
}

class Counter {
  int count = 0;

  // public synchronized void increment() { // this would ensure that this method can be called only once per time
  public void increment() {
    count++;
  }
}
```

## Handling Race Conditions

- Technique to prevent two or more threads to access the same resource at same time

### Mutex (Mutual exclusion)

> Mutex is an object owned by a thread, so there is a ownership in mutex. Mutex allows only one thread to access the resource

- The resource uses then a `Mutual Exclusion Object` (mutex) that acts like a **lock** to signalize that the resource is being used
- If a process tries to access the resource while it's locked, it will error out

- **Cons**
  - May slow down the system since the resource access is now bottlenecked

### Semaphore (Signaling)

> Semaphore is a signaling mechanism. It allows a maximum number of threads to access shared resources

- While a signal is on, no other resource can access it
- If a process tries to access the resource while the signal is on, it will wait (with light turned off) until the resource it freed

- Uses the **Dekkers's Algorithm** to avoid deadlocks

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
