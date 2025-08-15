#include <iostream>
#include <map>
using namespace std;

int main() {
  map<string, int> m;
  m.insert(pair<string, int>("a", 1));
  m.insert(pair<string, int>("b", 2));
  m.insert(pair<string, int>("c", 3));

  // returns 1 if the key is found, 0 otherwise

  cout << m.count("c") << endl;

  return 0;
}
