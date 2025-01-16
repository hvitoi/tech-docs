#include <iostream>
#include <list>
using namespace std;

// Implements a "doubly-linked list"

void printList(const list<int> &theList) {
  // const: prevents it from being modified
  // &: pass it by reference (instead of by value)
  for (list<int>::const_iterator it = theList.begin(); it != theList.end();
       it++) { // alternatively use "auto"
    cout << *it << endl;
  }
}

int main() {
  // Initialize Empty List
  list<int> numbers;
  numbers.push_back(1);
  numbers.push_back(2);
  numbers.push_back(3);

  // Initialize Pre-filled List
  list<int> myList2 = {1, 2, 3}; // copy-list initialization
  list<int> myList3{1, 2, 3};    //  direct-list initialization

  // Iterate
  for (auto it = numbers.begin(); it != numbers.end(); it++) {
    cout << *it << endl;
  }
  for (int number : numbers) {
    cout << number << endl;
  }

  return 0;
}
