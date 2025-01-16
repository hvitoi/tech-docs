#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> numbers = {1, 2, 3};

  // Traditional for Loop
  for (size_t i = 0; i < numbers.size(); ++i) {
    cout << numbers[i] << endl;
  }

  // Range-Based for Loop
  for (int number : numbers) {
    cout << number << endl;
  }

  // Iterator
  for (vector<int>::iterator it = numbers.begin(); it != numbers.end(); it++) {
    cout << *it << endl;
  }

  // Const Iterator
  for (std::vector<int>::const_iterator it = numbers.cbegin();
       it != numbers.cend(); ++it) {
    std::cout << *it << " ";
  }

  // Reverse Iterator
  for (std::vector<int>::reverse_iterator it = numbers.rbegin();
       it != numbers.rend(); ++it) {
    std::cout << *it << " ";
  }

  // Const Reverse Iterator
  for (std::vector<int>::const_reverse_iterator it = numbers.crbegin();
       it != numbers.crend(); ++it) {
    std::cout << *it << " ";
  }

  return 0;
}
