#include <iostream>
using namespace std;

// The "new" keyword dynamically allocate memory in the HEAP memory

// Memory allocated on the heap persists until you explicitly free it using the
// delete keyword (for single objects) or delete[] (for arrays of objects).

// Unlike stack memory, heap memory does not automatically go out of scope when
// the function or block ends.

struct Node {
  int data;
  Node *left;
  Node *right;
};

class Node2 {
public:
  int data;
  Node *left;
  Node *right;
};

int main() {
  Node *root = new Node();
  root->data = 42;
  root->left = root->right = nullptr;
  delete root;

  Node2 *root2 = new Node2();
  root2->data = 42;
  root2->left = root2->right = nullptr;
  delete root2;

  // Allocate a variable dynamically
  int *number = new int(42); // Declare and Assign
  delete number;             // Delete
  number = new int(43);      // Re-assign
  delete number;             // Delete

  cout << "" << endl;
  return 0;
}
