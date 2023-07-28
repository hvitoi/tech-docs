#include <stdio.h>
#include <string.h>

int main() {
  char s1[] = "abcd";
  char s2[] = "efgh";

  // Compare n chars
  strncmp(s1, s2, 1);

  return 0;
}
