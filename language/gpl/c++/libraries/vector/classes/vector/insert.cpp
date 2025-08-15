#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<string> colors{"red", "blue", "green"};

  // Insert at Index
  colors.insert(colors.begin(), "pink");     // at index 0
  colors.insert(colors.begin() + 1, "grey"); // at index 1

  // Append other vector
  vector<int> vec1{1, 2};
  vector<int> vec2{3, 4};
  vec1.insert(vec1.end(), vec2.begin(), vec2.end());

  for (auto el : vec1) {
    cout << el << " ";
  }

  return 0;
}
