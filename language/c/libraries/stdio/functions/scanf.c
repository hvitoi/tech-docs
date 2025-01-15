#include <stdio.h>

int main() {
  char name[25];
  int age;

  // & means the address in memory

  printf("What is your name?");
  scanf("%s", name); // "%s" expects the address of the first element
  // scanf("%s", &name); // incorrect, it's the address of the entire array

  printf("How old are you?");
  scanf("%d", &age);

  printf("Hi, %s. You are %d years old.", name, age);

  return 0;
}
