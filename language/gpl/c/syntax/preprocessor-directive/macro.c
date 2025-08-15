#include <stdio.h>
#include <stdlib.h>

#define ASSERT_EQ(expected, actual)                                            \
  do {                                                                         \
    if ((expected) != (actual)) {                                              \
      fprintf(stderr,                                                          \
              "Assertion failed: (" #actual " == " #expected "), "             \
              "actual: %d, expected: %d\n",                                    \
              (actual), (expected));                                           \
      abort();                                                                 \
    }                                                                          \
  } while (0)

int main() {
  int actual = 5;
  int expected = 10;

  ASSERT_EQ(expected, actual);

  return 0;
}
