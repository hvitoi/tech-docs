#include <cassert>
#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *left;
  Node *right;
};

Node *createNode(int data) {
  Node *newNode = new Node();
  newNode->data = data;
  newNode->left = newNode->right = nullptr;
  return newNode;
}

void printTree(Node *root) {
  // DFS In-Order

  if (root == nullptr)
    return;

  cout << root->data << endl;
  printTree(root->left);
  printTree(root->right);
}

int main() {
  Node *root = createNode(1);
  root->left = createNode(2);
  root->right = createNode(3);
  root->left->left = createNode(4);

  assert(root->data == 1);

  return 0;
}
