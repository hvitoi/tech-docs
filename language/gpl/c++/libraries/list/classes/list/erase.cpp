#include <iostream>
#include <list>
using namespace std;

int main() {
  list<int> myList = {1, 2, 3};

  // Erase the element by its iterator
  myList.erase(myList.begin()); // remove the first element

  for (auto it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }

  return 0;
}
