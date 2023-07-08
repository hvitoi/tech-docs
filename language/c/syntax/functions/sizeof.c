#include <stdio.h>

typedef struct {
  int weight;
  int height;
} Person;

int main() {
  // "sizeof" receives a type as input
  printf("%i\n", sizeof(int));    // 4
  printf("%i\n", sizeof(float));  // 4
  printf("%i\n", sizeof(Person)); // 8

  return 0;
}
