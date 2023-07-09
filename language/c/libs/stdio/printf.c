#include <stdio.h>

int main() {
  printf("Hello World!");
  printf("1\t2\t3\n4\t5\t6\n7\t8\t9");

  // with variable
  char name[] = "Bro";
  int age = 29;
  char grade = 'A';
  float gpa = 6.78;
  printf("%s, you are %d years old, your grade is %c with gpa %3.2f", name, age,
         grade, gpa);

  return 0;
}
