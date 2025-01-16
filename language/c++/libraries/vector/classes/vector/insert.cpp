#include <vector>
using namespace std;

int main() {
  vector<string> colors = {"red", "blue", "green"};

  colors.insert(colors.begin(), "pink");     // at index 0
  colors.insert(colors.begin() + 1, "grey"); // at index 1

  return 0;
}
