#include <stdio.h>

// Function prototype is the signature of the function (the header!)
// This allows the actual implementation to be declared after its call

// Due to the fact that many C compiler do not check the function parameters,
// you can even compile a function that has been defined after, however you
// might get error if not passing the right args at runtime. Having a prototype
// resolves this problem too

void hey(char name[]); // function prototype! (the header!)

int main() {
  hey("John");
  return 0;
}

void hey(char name[]) {
  printf("hey, %s!", name);
  printf("Welcome!");
}
