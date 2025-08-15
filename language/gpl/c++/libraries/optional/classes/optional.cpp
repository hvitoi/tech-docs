#include <iostream>
#include <optional>
using namespace std;

int main() {
  optional<int> x = 42;
  cout << *x << endl;

  x.reset(); // "Remove" the variable's value
  x = 100;   // Re-assign
  cout << *x << endl;

  return 0;
}
