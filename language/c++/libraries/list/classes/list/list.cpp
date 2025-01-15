#include <iostream>
#include <list>
using namespace std;

// A list is a dynamic type of container and it will automatically
// increase/shrink its size

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

  for (auto it = myList2.begin(); it != myList2.end(); it++) {
    cout << *it << endl;
  }

  return 0;
}
