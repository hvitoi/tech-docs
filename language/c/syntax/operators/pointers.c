#include <stdio.h>
#include <stdlib.h>

// * : Dereference operator (value at the address)
// & : Address-of operator (address of the variable)

typedef struct {
  int height;
  int age;
} Person;

int main() {
  // Pointer to a "Variable"
  int age = 29;
  int *pAge = NULL; // Initialize the pointe with a NULL reference
  pAge = &age;      // Assign the memory address of the age variable
  *pAge = 99;       // Assign to the original age variable
  printf("a = %i\n", age);
  printf("*b = %i\n", *pAge); // dereferencing

  // Pointer to a "Struct"
  Person henry;
  Person *pHenry = &henry;
  pHenry->age = 12;
  pHenry->height = 170;
  printf("henry.age = %i, henry.height = %i\n", henry.age, henry.height);
  printf("pHenry->age = %i, pHenry->height = %i\n\n", pHenry->age,
         pHenry->height);

  // Manual memory allocation
  int *c = (int *)malloc(sizeof(int));

  if (c == NULL) {
    printf("Memory allocation failed.\n");
    return 1;
  }

  *c = 99;
  printf("Pointer address: %p, Value: %i\n", (void *)c, *c);

  // Memory:         Array of bytes within RAM
  // Memory Block:   A portion of one byte in the memory
  // Memory Address: The Address of a memory block

  char myChar = 'a';
  printf("%p\n", &myChar); // prints the memory block address of the variable

  char myArray[] = "abc";
  printf("%p\n", &myArray); // prints the memory block address of the entire arr
  printf("%p\n", myArray);  // prints the memory block address of the first el

  return 0;
}
