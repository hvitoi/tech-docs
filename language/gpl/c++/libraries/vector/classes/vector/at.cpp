#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<string> colors = {"red", "blue", "green"};

  cout << colors.at(0) << endl;
  cout << colors[0] << endl; // same

  // cout << colors.at(3) << endl; // throws
  cout << colors[3] << endl; // does not throw

  return 0;
}
