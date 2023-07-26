#include <string.h>

int main() {
  char name[25] = "abcd";

  int name_size = strlen(name);
  name[name_size - 1] = '\0'; // remove trailing \n

  return 0;
}
