#include <iostream>
#include <list>
using namespace std;

// Return the iterator of the first element of the list

int main() {
  list<int> myList = {1, 2, 3};

  for (auto it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }

  return 0;
}
