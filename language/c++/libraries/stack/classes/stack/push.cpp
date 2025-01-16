#include <iostream>
#include <stack>
using namespace std;

// Add element to the top of the stack

int main() {
  stack<string> s;

  s.push("red");
  s.push("green");
  s.push("blue");

  cout << "It's a stack!" << endl;

  return 0;
}
