#include <stdio.h>
#include <stdlib.h>

// * : Dereference operator (value at the address)
// & : Address-of operator (address of the variable)

// Points can point to objects on the HEAP or STACK memory

typedef struct {
  int height;
  int age;
} Person;

typedef struct {
  int data;
  struct Node *left;
  struct Node *right;
} Node;

Node *createNode(int data) {
  Node *newNode = (Node *)malloc(sizeof(Node));
  if (newNode == NULL) {
    printf("Memory allocation failed!\n");
    exit(1);
  }
  newNode->data = data;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

int main() {
  // Pointer to a "Variable"
  int number = 29;
  int *pNumber = NULL; // Initialize the pointe with a NULL reference
  pNumber = &number;   // Assign the memory address of the age variable
  *pNumber = 99;       // Assign to the original age variable
  printf("number = %i\n", number);
  printf("*pNumber = %i\n", *pNumber); // dereferencing

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
