#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<string> colors;
  colors.push_back("red");
  colors.push_back("green");
  colors.push_back("blue");

  for (string color : colors) {
    cout << color << endl;
  }
}
