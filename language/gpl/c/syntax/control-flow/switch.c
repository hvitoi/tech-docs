#include <stdio.h>

int main() {

  int foo = 'a';

  switch (foo) {
  case 'a':
    printf("It's A!");
    break;
  case 'b':
    printf("It's B!");
    break;
  default:
    printf("???");
  }

  return 0;
}
