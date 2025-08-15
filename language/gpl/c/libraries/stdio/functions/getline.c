#include <stdio.h>
#include <stdlib.h>

int main() {
  char *line = NULL; // Pointer to the buffer (must be initialized to NULL)
  size_t len = 0;    // Size of the buffer (can be 0 for getline to allocate)

  printf("Enter your full name: ");
  ssize_t nread = getline(&line, &len, stdin);

  if (nread != -1) {
    // Remove the trailing newline character
    if (line[nread - 1] == '\n') {
      line[nread - 1] = '\0';
    }
    printf("Hello, %s!\n", line);
  } else {
    printf("Error reading input.\n");
  }

  free(line); // Free the buffer allocated by getline
  return 0;
}
