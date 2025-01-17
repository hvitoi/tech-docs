#include <iostream>
using namespace std;

// "cin" stops collection as soon as "enter" is pressed

int main() {
  string name;

  cout << "Enter your name: ";
  cin >> name; // does not support spaces. For that use "getline"

  cout << "Hello, " << name << "!" << endl;

  float sum = 0;
  float el;
  for (int i = 0; i < 3; i++) {
    cout << "Enter value " << i << ": ";
    cin >> el;
    sum += el;
  }
  cout << "The sum is: " << sum << endl;

  return 0;
}
