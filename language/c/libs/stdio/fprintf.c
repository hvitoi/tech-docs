#include <stdio.h>

int main() {

  FILE *pF = fopen("a.txt", "w");

  fprintf(pF, "Spongbob"); // (over)write to the file

  fclose(pF);

  return 0;
}
