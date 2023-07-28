#include <stdio.h>

void hey(char name[]) {
  printf("hey, %s!", name);
  printf("Welcome!");
}

int square(double x) { return x * x; }

int main() {
  hey("John");
  return 0;
}
