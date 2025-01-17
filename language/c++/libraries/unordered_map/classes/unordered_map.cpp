#include <iostream>
#include <unordered_map>
using namespace std;

// Newer elements are appended to the front

int main() {
  unordered_map<string, int> m;

  m.insert(pair<string, int>("c", 3));
  m.insert(pair<string, int>("a", 1));
  m.insert(pair<string, int>("b", 2));
  m.insert(pair<string, int>("z", 99));

  for (auto pair : m) {
    cout << pair.first << " " << pair.second << endl;
  }

  return 0;
}
