#include <stdio.h>

// "Struct" is a custom variable definition
// "Typedef" gives a name for the struct
typedef struct {
  int weight;
  int height;
} Person;

int main() {
  Person person;
  person.weight = 80;
  person.height = 185;

  printf("weight: %i, height: %i.\n", person.weight, person.height);
  printf("Addresses: %p %p.\n", &person, person);

  return 0;
}
