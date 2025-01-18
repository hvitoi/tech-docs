#include <iostream>

// stdin
// "cin" stops collection as soon as "enter" is pressed

int main() {
  std::string name;

  std::cout << "Enter your name: ";
  std::cin >> name; // does not support spaces. For that use "getline"

  std::cout << "Hello, " << name << "!" << std::endl;

  float sum = 0;
  float el;
  for (int i = 0; i < 3; i++) {
    std::cout << "Enter value " << i << ": ";
    std::cin >> el;
    sum += el;
  }
  std::cout << "The sum is: " << sum << std::endl;

  return 0;
}
