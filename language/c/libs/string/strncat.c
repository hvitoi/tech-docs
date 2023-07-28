#include <stdio.h>
#include <string.h>

int main() {
  char s1[] = "abcd";
  char s2[] = "efgh";

  // appends n chars from s2 to s1
  strncat(s1, s2, 1);

  return 0;
}
