#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *left;
  Node *right;
};

int main() {
  Node *root = new Node();
  root->data = 42;
  root->left = root->right = nullptr;

  delete root; // Free up the object from HEAP memory

  // This just frees the memory, but the pointer is still a memory address, not
  // nullptr. Therefore it's a good practice to explicitly override it
  root = nullptr;

  cout << "" << endl;
  return 0;
}
