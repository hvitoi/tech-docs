#include <iostream>
#define ASSERT_EQ(expected, actual)                                            \
  do {                                                                         \
    if ((expected) != (actual)) {                                              \
      std::cerr << "Assertion failed: (" #actual " == " #expected "), "        \
                << "actual: " << (actual) << ", "                              \
                << "expected: " << (expected) << std::endl;                    \
      std::abort();                                                            \
    }                                                                          \
  } while (0)

int main() {
  int actual = 5;
  int expected = 10;

  // Using the custom assertion macro
  ASSERT_EQ(expected,
            actual); // This will fail and print a detailed error message

  return 0;
}
