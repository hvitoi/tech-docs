#include <iostream>
#include <list>
using namespace std;

int main() {
  list<int> myList;
  myList.push_back(1);
  myList.push_back(2);
  myList.push_back(3);

  // Erase the element by its iterator
  myList.erase(myList.begin());  // remove the first element

  for (auto it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }

  return 0;
}
