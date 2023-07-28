#include <stdio.h>
#include <string.h>

int main() {
  char s1[] = "Mustang";
  char s2[] = "Tesla";

  // copy s2 to s1
  // copying different string sizes may lead to errors!
  strcpy(s1, s2);

  printf("%s", s1); // Tesla!

  return 0;
}
