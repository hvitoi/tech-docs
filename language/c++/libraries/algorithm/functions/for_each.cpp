#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> numbers = {1, 2, 3};

  for_each(numbers.begin(), numbers.end(),
           [](int number) { std::cout << number << endl; });

  return 0;
}
