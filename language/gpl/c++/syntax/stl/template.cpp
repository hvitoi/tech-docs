#include <iostream>
using namespace std;

// Templates make the function/class flexible so that it can receive any type

// Template Function
template <typename T>
T add(T a, T b) {
  return a + b;
  ;
}

// Template Class
template <typename T>
class Calculator {
 public:
  T add(T a, T b) {
    return a + b;
    ;
  }

  T subtract(T a, T b) {
    return a - b;
    ;
  }
};

int main() {
  cout << add(5, 7) << endl;
  cout << add(5.3, 7.7) << endl;

  Calculator<int> intCalculator;
  cout << intCalculator.add(1, 2) << endl;
  cout << intCalculator.subtract(1, 2) << endl;

  Calculator<float> floatCalculator;
  cout << floatCalculator.add(3.3, 2.2) << endl;
  cout << floatCalculator.subtract(3.3, 2.2) << endl;

  return 0;
}
