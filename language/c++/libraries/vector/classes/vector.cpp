#include <iostream>
#include <vector>
using namespace std;

// Vectors are dynamic arrays

int main() {
  // Create
  vector<string> colors = {"red", "blue", "green"};

  // Create (based on another vector)
  auto concatenated(colors);

  // Access
  cout << colors[0] << endl;
  cout << colors[3] << endl; // does not throw

  // Iterate
  for (auto it = colors.begin(); it != colors.end(); it++) {
    cout << *it << endl;    // element
    cout << &(*it) << endl; // address of element
    cout << &it << endl;    // address of the iterator
  }

  for (string color : colors) {
    cout << color << endl;
  }
}
