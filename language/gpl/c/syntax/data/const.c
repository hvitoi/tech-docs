#include <stdio.h>

typedef struct {
  int id;
  char name[50];
} Something;

void displayObject(const Something *obj) {
  printf("Object ID: %d\n", obj->id);
  printf("Object Name: %s\n", obj->name);
  // obj->id = 42;  // Compilation Error: assignment of read-only location
}

int main() {
  // Constant variable
  const float PI = 3.14; // cannot change during execution

  // Constant function argument
  Something myObject = {1, "My First Object"};
  displayObject(&myObject);

  return 0;
}
