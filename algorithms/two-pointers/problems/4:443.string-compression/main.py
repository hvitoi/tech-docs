# %%
import unittest


def compress(chars: list) -> int:
    compressed = []
    for i in range(len(chars)):
        if (i != 0) and (chars[i] == chars[i - 1]):
            compressed[-1] += 1
        else:
            compressed.extend([chars[i], 1])
    return len("".join(map(lambda el: str(el), filter(lambda el: el != 1, compressed))))


def compress2(chars: list) -> int:
    compressed = []
    for i in range(len(chars)):
        if (i != 0) and (chars[i] == chars[i - 1]):
            compressed[-1] += 1
        else:
            compressed.extend([chars[i], 1])
    return len("".join([str(el) for el in compressed if el != 1]))


test_case = unittest.TestCase()

for fn in {compress, compress2}:
    test_case.assertEqual(fn(["a", "a", "b", "b", "c", "c", "c"]), 6)
    test_case.assertEqual(fn(["a"]), 1)
    test_case.assertEqual(
        fn(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]), 4
    )
