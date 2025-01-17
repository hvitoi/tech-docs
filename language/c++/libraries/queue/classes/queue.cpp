#include <iostream>
#include <queue>
using namespace std;

int main() {
  queue<string> q;
  q.push("red");
  q.push("green");
  q.push("blue");

  // Consume items from queue
  while (!q.empty()) {
    cout << q.front() << endl;
    q.pop();
  }

  return 0;
}
