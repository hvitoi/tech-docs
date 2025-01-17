#include <stdio.h>

// Stores more than 1 value of the same type
// The array size cannot be changed at runtime!

// If the size is not defined, it will be calculated as compile time

int main() {
  // Array of doubles
  double prices[] = {5.0, 10.0, 15.0, 25.0, 20.0};
  double prices2[] = {
      [0] = 5.0, [1] = 10.0, [2] = 15.0, [3] = 25.0, [4] = 20.0};

  // Array of chars
  char name[] = "Hello World";
  char name2[12] = "Hello World";

  // Array of integers
  int numbers[10] = {8, 1, 4, 3}; // fixed size

  // Matrix
  char matrix[][3] = {
      {'a', 'b', 'c'},
      {'d', 'e', 'f'},
  }; // the first dimension size is optional (calculated at compile time)

  // Access/Modify (by index)
  prices[0] = 42;
  printf("%f", prices[0]);

  // trying to access/modify an out of bounds index does not throw
  prices[99] = 88;
  printf("%f", prices[99]);

  return 0;
}
