#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> numbers;
  numbers.push_back(1);
  numbers.push_back(2);
  numbers.push_back(3);

  for (auto it = numbers.begin(); it != numbers.end(); it++) {
    cout << *it << endl;
  }
}
