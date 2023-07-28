#include <stdio.h>

// Memory:         Array of bytes within RAM
// Memory Block:   A portion of one byte in the memory
// Memory Address: The Address of a memory block

int main() {
  char a = 'a';
  char b = 'b';
  char c = 'c';

  printf("%p\n", &a); // prints the first memory block address
  printf("%p\n", &b);
  printf("%p\n", &c);

  //

  return 0;
}
