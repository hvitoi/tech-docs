#include <stdio.h>

// typedef gives an alias to something

typedef struct {
  int weight;
  int height;
} Person;
Person henry;

typedef char CharWithSizeTen[10];

int main() {

  CharWithSizeTen greeting = "Hey!";
  return 0;
}
