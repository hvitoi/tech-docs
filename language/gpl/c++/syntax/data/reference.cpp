#include <iostream>
#include <list>
using namespace std;

void printList(const list<int> &theList) {
  // const: prevents it from being modified
  // &: pass it by reference (instead of by value)
  for (auto it = theList.begin(); it != theList.end(); it++) {
    cout << *it << endl;
  }
}

int main() {

  list<int> myList = {1, 2, 3}; // copy-list initialization

  return 0;
}
