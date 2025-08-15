#include <stdio.h>
#include <string.h>

// Similar to classes, but has no methods

// Create a struct (reference it as "struct Player")
struct Player {
  char name[20];
  int score;
};

struct Node {
  int data;
  struct Node *left; // reference itself
  struct Node *right;
};

// Create a struct (reference it simply as "Person")
// typedef gives an alias for the struct
typedef struct {
  char name[20];
  int age;
} Person;

int main() {

  // Create
  struct Player maria;
  Person henry;                              // empty
  Person luigi = {"Luigi", 27};              // positional args
  Person john = {.name = "John", .age = 30}; // name args

  printf("Name: %s, Age: %d\n", henry.name, henry.age);
  printf("Name: %s, Age: %d\n", luigi.name, luigi.age);
  printf("Name: %s, Age: %d\n", john.name, john.age);

  // Access/Modify
  strcpy(henry.name, "Henry2");
  henry.age = 42;

  printf("Name: %s, Age: %d\n", henry.name, henry.age);

  // Access/Modify (via pointers)
  Person *pHenry = &henry;
  strcpy(pHenry->name, "Henry3");
  pHenry->age = 43;

  printf("Name: %s, Age: %d\n", pHenry->name, pHenry->age);

  return 0;
}
