#include <stdio.h>

int main() {

  int foo = 1;

  if (foo == 1) {
    printf("It's one!");
  } else if (foo < 1) {
    printf("It's less than one!");
  } else {
    printf("It's more than one!");
  }

  return 0;
}
