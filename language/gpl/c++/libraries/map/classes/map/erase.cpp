#include <iostream>
#include <map>
using namespace std;

int main() {
  map<string, int> m;

  m.insert(pair<string, int>("a", 1));
  m.erase("a");

  cout << m.size() << endl;

  return 0;
}
