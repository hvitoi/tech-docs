#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

  long now = time(0);

  // Seed random!
  // generates a random value using a seed
  srand(now);

  return 0;
}
