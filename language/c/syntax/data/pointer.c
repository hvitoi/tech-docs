#include <malloc.h>
#include <stdio.h>

typedef struct {
  int height;
  int age;
} Person;

int main() {
  // variable pointer
  int a = 98;
  int *b = &a; // int pointer
  *b = 99;     // value pointed by the int pointer
  printf("a = %i\n", a);
  printf("*b = %i\n\n", *b);

  // struct pointer
  Person p1;
  Person *p2 = &p1;
  p2->age = 12;
  p2->height = 170;
  printf("p1.age = %i, p1.height = %i\n", p1.age, p1.height);
  printf("p2->age = %i, p2->height = %i\n\n", p2->age, p2->height);

  // Manual memory allocation
  int *c = (int *)malloc(sizeof(int));
  *c = 77;
  printf("%i: %i", c, *c);

  return 0;
}
