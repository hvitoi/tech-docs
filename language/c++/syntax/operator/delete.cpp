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

  cout << "" << endl;
  return 0;
}
