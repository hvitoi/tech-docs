#include <vector>
using namespace std;

int main() {
  vector<string> colors = {"red", "blue", "green"};

  colors.erase(colors.begin());     // from index 0
  colors.erase(colors.begin() + 1); // from index 1

  return 0;
}
