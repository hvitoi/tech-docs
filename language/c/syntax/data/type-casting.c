#include <stdlib.h>

int main() {
  // Cast to a "Pointer to an integer" from a generic "pointer to void" (void *)
  // In C, a void * can be assigned to any pointer type without a cast
  int *ptr = (int *)malloc(sizeof(int)); // Cast void* to int*
  int *ptr = malloc(sizeof(int));        // This also works because void* is
                                  // automatically casted to int* by inference
                                  // (modern C compilers)

  return 0;
}
