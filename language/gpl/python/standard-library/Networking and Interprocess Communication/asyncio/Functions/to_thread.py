# %%
import asyncio
import time

# Transforms a "normal" function into a coroutine which is executed in a separate Thread under the hood


def just_wait(delay):
    print("Task started")
    time.sleep(delay)
    print("Task finished")


async def main():
    # Creates a separate thread is which it will run. It is not started yet!
    coroutine = asyncio.to_thread(just_wait, 5)

    time.sleep(10)
    await coroutine  # start the thread and wait for the result


if __name__ == "__main__":
    asyncio.run(main())
