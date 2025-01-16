#include <stdio.h>
#include <string.h>

int main() {

  // break: exit out of the code block entirely
  // continue: skip to the next loop iteration

  for (int i = 0; i < 10; i += 2) {
    printf("%d", i);
  }

  int numbers[] = {10, 20, 30, 40, 50};
  int size = sizeof(numbers) / sizeof(numbers[0]);
  for (int i = 0; i < size; i++) {
    printf("%d\n", numbers[i]);
  }

  char name[] = "Henry";
  for (int i = 0; i < strlen(name); i++) {
    printf("%c", name[i]);
  }

  return 0;
}
