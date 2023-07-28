#include <stdlib.h>

int main() {

  int the_random = rand(); // between 0 - 32767

  const int MIN = 1;
  const int MAX = 100;

  // random number between min and max
  int foo = (rand() % MAX) + MIN;

  return 0;
}
