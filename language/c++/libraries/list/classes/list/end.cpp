#include <iostream>
#include <list>
using namespace std;

// Return the iterator of the last element of the list

int main() {
  list<int> myList;
  myList.push_back(1);
  myList.push_back(2);
  myList.push_back(3);

  for (auto it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }

  return 0;
}
