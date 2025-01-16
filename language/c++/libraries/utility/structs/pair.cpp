#include <iostream>
#include <utility>
using namespace std;

int main() {
  pair<string, int> myPair = pair<string, int>("a", 1);

  cout << myPair.first << " " << myPair.second << endl;

  return 0;
}
