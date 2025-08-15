#include <stdio.h>

int main() {
  char name[25];

  printf("What's your name?");

  // get 25 chars from stdin (including whitespaces)
  // includes the return (\n)
  fgets(name, 25, stdin);

  return 0;
}
