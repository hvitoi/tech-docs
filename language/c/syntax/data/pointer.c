#include <malloc.h>
#include <stdio.h>

// The reason why it exists is that some tasks are performed more easily with
// pointers

typedef struct {
  int height;
  int age;
} Person;

int main() {
  // pointer to a variable
  int age = 29;     // Pointer to a memory address that contains a integer value
  int *pAge = NULL; // It's a good practice to declare a point assigning it NULL
  pAge = &age;
  *pAge = 99; // value pointed by the int pointer
  printf("a = %i\n", age);
  printf("*b = %i\n", *pAge); // dereferencing

  // pointer to a struct
  Person henry;
  Person *pHenry = &henry;
  pHenry->age = 12;
  pHenry->height = 170;
  printf("henry.age = %i, henry.height = %i\n", henry.age, henry.height);
  printf("pHenry->age = %i, pHenry->height = %i\n\n", pHenry->age,
         pHenry->height);

  // Manual memory allocation
  int *c = (int *)malloc(sizeof(int));
  *c = 77;
  printf("%i: %i", c, *c);

  return 0;
}
