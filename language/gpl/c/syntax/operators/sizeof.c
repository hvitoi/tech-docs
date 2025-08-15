#include <stdio.h>

typedef struct {
  int weight;
  int height;
} Person;

int main() {
  // Size of a data structure in bytes
  // "sizeof" receives a type as input
  sizeof(int);    // 4
  sizeof(float);  // 4
  sizeof(Person); // 8

  // size of an array
  int foo[] = {1, 2, 3, 4};
  int the_size = sizeof(foo) / sizeof(foo[0]);

  return 0;
}
