#include <iostream>
#include <stack>
using namespace std;

// Remove element from the top of the stack

int main() {
  stack<string> s;

  s.push("red");
  s.push("green");
  s.push("blue");

  // Pop does not return the popped element
  // Therefore you must first get the element with "top" before popping it
  while (!s.empty()) {
    cout << s.top() << endl;
    s.pop();
  }

  // s.pop(); // popping after the stack is exhausted throws!

  return 0;
}
