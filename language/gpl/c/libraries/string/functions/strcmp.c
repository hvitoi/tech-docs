#include <stdio.h>
#include <string.h>

int main() {
  char s1[] = "abcd";
  char s2[] = "efgh";

  // Compare all chars

  int res = strcmp(s1, s2);
  printf("%d", res);

  // strcmpi(s1, s1);
  // strnicmp(s1, s1, 1);

  return 0;
}
