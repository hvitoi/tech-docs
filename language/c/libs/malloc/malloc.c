#include <malloc.h>
#include <stdio.h>

// Allocate memory and returns its address
// Returns "*void", therefore it must be casted

int main() {
  // allocate the size of an "int"
  int *intPointer = (int *)malloc(sizeof(int));
  printf("%i", intPointer);

  return 0;
}
