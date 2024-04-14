# Deadlocks (Impasse)

- When the `process A get stuck` because it requires a `resource that is busy` because it's being used by `process B` that requires process A to complete
  - In this situation none of the process will ever continue: a deadlock
- Happens due to `sharing resources` because each process has `exclusive access to the resource`
- Can happen either for `hardware resources` and for `software resources`
  - Usually with `non-preemptive` resources that are not gracefully shutdown

## Code example

```txt
Thread A: Acquiring printer resource
Thread A: Using printer resource

Thread B: Acquiring camera resource
Thread B: Using camera resource

Thread A: Acquiring camera resource
Thread B: Acquiring printer resource
```

```python
# %%
import threading
import time

# resources
printer = threading.Lock()
camera = threading.Lock()


def use_printer_then_camera():
    thread = threading.current_thread().name

    print(f"{thread}: Acquiring printer resource")
    printer.acquire()
    print(f"{thread}: Using printer resource")

    time.sleep(1)

    print(f"{thread}: Acquiring camera resource")
    camera.acquire()
    print(f"{thread}: Using camera resource")

    print(f"{thread}: Releasing printer resource")
    printer.release()
    print(f"{thread}: Released printer resource")

    print(f"{thread}: Releasing camera resource")
    camera.release()
    print(f"{thread}: Released camera resource")


def use_camera_then_printer():
    thread = threading.current_thread().name

    print(f"{thread}: Acquiring camera resource")
    camera.acquire()
    print(f"{thread}: Using camera resource")

    time.sleep(2)

    print(f"{thread}: Acquiring printer resource")
    printer.acquire()
    print(f"{thread}: Using printer resource")

    print(f"{thread}: Releasing camera resource")
    camera.release()
    print(f"{thread}: Released camera resource")

    print(f"{thread}: Releasing printer resource")
    printer.release()
    print(f"{thread}: Released printer resource")


thread_a = threading.Thread(target=use_printer_then_camera, name="Thread A")
thread_b = threading.Thread(target=use_camera_then_printer, name="Thread B")


thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()
```
