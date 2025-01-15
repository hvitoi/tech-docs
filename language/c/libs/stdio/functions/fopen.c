#include <stdio.h>

int main() {

  // Modes
  // w: write
  // a: append
  // r: read

  // WRITE
  FILE *pF = fopen("a.txt", "w");

  fprintf(pF, "Spongbob"); // (over)write to the file

  fclose(pF);

  // READ
  FILE *pG = fopen("a.txt", "r");
  char line[255];

  if (pG == NULL) {
    printf("File does not exist");
  }

  while (fgets(line, 255, pG) != NULL) {
    // when fgets reaches the EOF it returns null and exits the loop
    printf("%s", line);
  }

  fclose(pG);

  return 0;
}
