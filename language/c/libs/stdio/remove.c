#include <stdio.h>

int main() {

  if (remove("a.txt") == 0) {
    printf("File deleted sucessfully");
  }

  return 0;
}
