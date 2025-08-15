#include <iostream>
#include <list>
#include <map>
using namespace std;

// Keys are ordered in ascending order

int main() {
  map<string, int> m;
  m.insert(pair<string, int>("c", 3));
  m.insert(pair<string, int>("a", 1));
  m.insert(pair<string, int>("b", 2));

  map<string, list<string>> m1;
  m1.insert(pair<string, list<string>>("z", {"Hello", "World"}));

  // Iterate
  for (auto pair : m) {
    cout << pair.first << " " << pair.second << endl;
  }

  // Write
  m["b"] = 99;

  // Access
  cout << m["b"] << endl;

  return 0;
}
