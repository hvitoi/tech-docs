#include <stdio.h>

// In functions you can pass the elements by reference or by value
// By reference means you will be manipulating the original element
// By value means the element is duplicated

void hey(char name[]) {
  printf("hey, %s!", name);
  printf("Welcome!");
}

int square(double x) { return x * x; }

int main() {
  hey("John");
  return 0;
}
