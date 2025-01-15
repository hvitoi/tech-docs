#include <iostream>
#include <list>
using namespace std;

int main() {
  list<int> myList = {1, 2, 3};

  // Insert an element at a specific position
  // The other elements are then "shifted" (not exactly because it's a LL)
  myList.insert(myList.begin(), 0);

  for (auto it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }

  return 0;
}
