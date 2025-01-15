#include <string.h>

int main() {
  char s1[] = "abcd";
  char s2[] = "efgh";

  // copy n chars of s2 to s1
  strncpy(s1, s2, 1);

  return 0;
}
