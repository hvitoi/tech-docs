#include <stdio.h>

// by default it's assigned the number of the index
// Red=0, Green=1, Blue=2
enum Colors { Red, Green, Blue };

// Force the number
enum Day { Sun = 1, Mon = 2, Tue = 3, Wed = 4, Thu = 5, Fri = 6, Sat = 7 };

int main() {
  // For the sake of the program, the values are treated as integers!
  enum Day today = Tue;

  printf("%d", today);

  if (today == Tue) { // a lot more readable! (than today == 3)
    printf("Sad!");
  }

  return 0;
}
