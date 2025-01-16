#include <iostream>
#include <stack>
using namespace std;

int main() {
  stack<string> s;

  s.push("red");
  s.push("green");
  s.push("blue");

  // Consume elements from stack
  while (!s.empty()) {
    cout << s.top() << endl;
    s.pop();
  }

  return 0;
}
