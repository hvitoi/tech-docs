#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<string> colors = {"red", "blue", "green"};

  // Traditional for Loop
  for (size_t i = 0; i < colors.size(); ++i) {
    cout << colors[i] << endl;
  }

  // Range-Based for Loop
  for (string color : colors) {
    cout << color << endl;
  }

  return 0;
}
