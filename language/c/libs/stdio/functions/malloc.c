#include <stdio.h>
#include <stdlib.h>

int main() {
  int *ptr = (int *)malloc(sizeof(int)); // Allocate the size of an integer
  int *ptr2 = malloc(sizeof(int));       // Also work in modern compilers

  if (ptr == NULL) {
    printf("Memory allocation failed.\n");
    return 1;
  }

  *ptr = 42; // Store a value at the allocated memory

  printf("Pointer address: %p\n", (void *)ptr);
  printf("Value: %i\n", *ptr);

  // Free the allocated memory
  free(ptr);

  return 0;
}
