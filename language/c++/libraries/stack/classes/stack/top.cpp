#include <iostream>
#include <stack>
using namespace std;

// Peek element from the top of the stack

int main() {
  stack<string> s;

  s.push("red");
  s.push("green");
  s.push("blue");

  cout << s.top() << endl;

  return 0;
}
