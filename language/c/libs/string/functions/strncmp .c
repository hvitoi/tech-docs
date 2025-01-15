#include <stdio.h>
#include <string.h>

int main() {
  char s1[] = "abcd";
  char s2[] = "efgh";

  // Compare n chars
  int res = strncmp(s1, s2, 1);
  printf("%d", res);

  return 0;
}
