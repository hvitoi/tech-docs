#include <stdio.h>

int main() {
  printf("Hello World!");
  printf("1\t2\t3\n4\t5\t6\n7\t8\t9");

  char name[] = "Bro"; // %s
  int age = 29;        // %d
  char grade = 'A';    // %c (char) or %d (int)
  float gpa = 6.78;    // %f
  double pi = 3.1515;  // %lf
  unsigned int k = 1;  // %u
  long long int l = 1; // %lld

  printf("%s, you are %d years old, your grade is %c with gpa %.2f", name, age,
         grade, gpa);

  return 0;
}
