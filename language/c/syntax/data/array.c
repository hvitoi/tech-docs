#include <stdio.h>

// Stores more than 1 value of the same type
// The array size cannot be changed at runtime!

int main() {

  // If the size is not defined, it will be calculated as compile time
  double prices[] = {5.0, 10.0, 15.0, 25.0, 20.0};
  char name[] = "Henry";

  // If the size is defined, it will be fixed, regardless of the number of
  // elements
  int numbers[10] = {8, 1, 4, 3};
  char matrix[][3] = {
      {'a', 'b', 'c'},
      {'d', 'e', 'f'},
  }; // the first dimension size is optional (calculated at compile time)

  prices[0]; // 5.0

  return 0;
}
