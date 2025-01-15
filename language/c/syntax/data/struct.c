#include <stdio.h>
#include <string.h>

// Similar to classes, but has no methods

// Create a struct (reference it as struct Player)
struct Player {
  char name[20];
  int score;
};
struct Player maria;

// Create a struct (reference it simply as Person)
// typedef gives a name for the struct
typedef struct {
  char name[20];
  int age;
} Person;
Person henry;

int main() {

  // Creation using name arguments
  strcpy(henry.name, "Henry");
  henry.age = 29;

  printf("name: %s, age: %d\n", henry.name, henry.age);
  printf("Memory Address: %p %p\n", &henry, henry);

  // Creation using positional arguments
  Person luigi = {"Luigi", 27};

  return 0;
}
