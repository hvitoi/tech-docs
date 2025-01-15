#include <iostream>
using namespace std;

// All members of a class are private by default
// To make it public add the keyword "public"

class Calculator {
 public:
  int add(int a, int b) {
    return a + b;
    ;
  }

  int subtract(int a, int b) {
    return a - b;
    ;
  }
};

int main() {
  Calculator calc;
  cout << calc.add(1, 2) << endl;
  cout << calc.subtract(1, 2) << endl;
  return 0;
}
