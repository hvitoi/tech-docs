#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<string> colors = {"red", "blue", "green"};

  // Iterator
  for (vector<string>::iterator it = colors.begin(); it != colors.end(); it++) {
    cout << *it << endl;
  }

  // Const Iterator
  for (std::vector<string>::const_iterator it = colors.cbegin();
       it != colors.cend(); it++) {
    std::cout << *it << endl;
    // *it = 42; // compile error. Cannot be modified
  }

  // Reverse Iterator
  for (std::vector<string>::reverse_iterator it = colors.rbegin();
       it != colors.rend(); it++) {
    std::cout << *it << endl;
  }

  // Const Reverse Iterator
  for (std::vector<string>::const_reverse_iterator it = colors.crbegin();
       it != colors.crend(); it++) {
    std::cout << *it << endl;
  }

  return 0;
}
