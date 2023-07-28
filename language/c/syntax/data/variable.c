#include <stdio.h>

int main() {
  int x;     // declaration
  x = 9;     // initialization
  int y = 9; // declaration + initialization

  // Signed
  signed char letter2 = 'A'; // same as char letter2
  char letter = 'z';         // 1 byte (-128 to + 127)
  int age = 21;              // 4 bytes
  float gpa = 2.05;          // 4 bytes
  double money = 3.1415;     // 8 bytes

  // Unsigned
  unsigned char letter3 = 'Z'; // (0 to 255)

  // Short
  short int h = 9;          // 2 bytes (-32,768 to +32,767)
  short i = 9;              // 2 bytes (-32,768 to +32,767)
  unsigned short int j = 9; // 2 bytes (0 to 65,535)

  // Long
  long long int u = 1; // 8 bytes

  // Constant
  const float PI = 3.14; // cannot change during execution

  // Arrays
  char name[] = "Henry";

  // Null (from stdio.h)
  int *pAge = NULL;

  return 0;
}
