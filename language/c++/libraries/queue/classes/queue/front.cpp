#include <iostream>
#include <queue>
using namespace std;

int main() {
  queue<string> q;
  q.push("red");
  q.push("green");
  q.push("blue");

  cout << q.front() << endl;

  return 0;
}