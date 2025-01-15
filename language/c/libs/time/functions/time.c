#include <stdio.h>
#include <time.h>

int main() {

  // current time in unix epoch
  long now = time(0);

  printf("%ld", now);

  return 0;
}
