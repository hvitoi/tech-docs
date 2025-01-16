#include <iostream>
#include <vector>
using namespace std;

// Vectors are dynamic arrays

int main() {
  vector<int> numbers = {1, 2, 3};

  for (auto it = numbers.begin(); it != numbers.end(); it++) {
    cout << *it << endl;
  }
}
