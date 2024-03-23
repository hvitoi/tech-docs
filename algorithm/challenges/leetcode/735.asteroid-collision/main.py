# %%
import unittest


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def asteroid_collision(asteroids: list) -> list:
    i = 0
    while i < len(asteroids) - 1:
        a1 = {
            "index": i,
            "direction": sign(asteroids[i]),
            "size": abs(asteroids[i]),
        }
        a2 = {
            "index": i + 1,
            "direction": sign(asteroids[i + 1]),
            "size": abs(asteroids[i + 1]),
        }
        if a1["direction"] == a2["direction"]:
            i += 1
        else:
            if a1["size"] < a2["size"]:
                asteroids.pop(a1["index"])
                i = i - 1 if i > 0 else 0
            elif a2["size"] < a1["size"]:
                asteroids.pop(a2["index"])
                i = i - 1 if i > 0 else 0

            else:
                asteroids.pop(a1["index"])
                asteroids.pop(a2["index"] - 1)
                i = i - 2 if i > 1 else 0

    return asteroids


def asteroid_collision2(asteroids: list) -> list:
    arr = []

    for incoming_asteroid in asteroids:
        incumbent_asteroid = arr[-1] if len(arr) > 0 else None

        if not incumbent_asteroid:
            arr.append(incoming_asteroid)
            continue

        if sign(incumbent_asteroid) == sign(incoming_asteroid):
            arr.append(incoming_asteroid)
            continue

        if abs(incoming_asteroid) >= abs(incumbent_asteroid):
            arr.pop()
            continue

    return arr


test_case = unittest.TestCase()

for fn in {asteroid_collision, asteroid_collision2}:
    test_case.assertEqual(
        fn([5, 10, -5]),
        [5, 10],
    )

    test_case.assertEqual(
        fn([8, -8]),
        [],
    )

    test_case.assertEqual(
        fn([10, 2, -5]),
        [10],
    )
