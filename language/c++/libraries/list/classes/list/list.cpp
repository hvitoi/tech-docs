#include <iostream>
#include <list>
using namespace std;

// Implements a "doubly-linked list"

void printList(const list<int> &theList) {
  // const: prevents it from being modified
  // &: pass it by reference (instead of by value)

  for (list<int>::const_iterator it = theList.begin(); it != theList.end();
       it++) {
    cout << *it << endl;
  }

  // for (auto it = theList.begin(); it != theList.end(); it++) {
  //   cout << *it << endl;
  // }
}

int main() {
  // Initialize Empty List
  list<int> myList;
  myList.push_back(1);
  myList.push_back(2);
  myList.push_back(3);

  // Initialize Pre-filled List
  list<int> myList2 = {1, 2, 3};

  // Iterate
  for (list<int>::iterator it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }
  printList(myList);
  printList(myList2);

  return 0;
}
