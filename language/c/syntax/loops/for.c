#include <stdio.h>
#include <string.h>

int main() {

  // break: exit out of the code block entirely
  // continue: skip to the next loop iteration

  for (int i = 0; i < 10; i += 2) {
    printf("%d", i);
  }

  char name[] = "Henry";
  for (int i = 0; i < strlen(name); i++) {
    printf("%c", name[i]);
  }

  return 0;
}
