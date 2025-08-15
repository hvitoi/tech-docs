// typedef gives an alias to something
typedef struct {
  int weight;
  int height;
} Person;

typedef char CharWithSizeTen[10];

int main() {
  Person henry;
  CharWithSizeTen greeting = "Hey!";
  return 0;
}
