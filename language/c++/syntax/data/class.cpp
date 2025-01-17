#include <iostream>
using namespace std;

class Calculator {

  // All members of a class are private by default
  // To make it public add the keyword "public"
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
  // Instance is created on the STACK (automatically destroyed when it goes out
  // of scope). No need to worry about memory management (freeing it up)
  Calculator calc;

  // Instance is created in the HEAP. It will persist until explicitly
  // deallocated
  Calculator *calc2 = new Calculator();

  cout << calc.add(1, 2) << endl;
  cout << calc.subtract(1, 2) << endl;
  return 0;
}
