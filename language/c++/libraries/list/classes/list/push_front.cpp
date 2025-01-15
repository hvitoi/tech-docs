#include <iostream>
#include <list>
using namespace std;

int main() {
  list<int> myList;
  myList.push_front(1);
  myList.push_front(2);
  myList.push_front(3);

  for (auto it = myList.begin(); it != myList.end(); it++) {
    cout << *it << endl;
  }
  return 0;
}
