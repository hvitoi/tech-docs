#include <iostream>
using namespace std;

class Node {
public:
  int data;
  Node *next;

  // Constructors
  Node(int value) : data(value), next(nullptr) {}
  Node(int value, Node *node) : data(value), next(node) {}
};

class LinkedList {
  // All members of a class are private by default
private:
  Node *head;

public:
  LinkedList() : head(nullptr) {}

  void push_left(int value) {
    Node *new_node = new Node(value, head);
    head = new_node;
  }

  void print() {
    Node *current = head;
    while (current) {
      cout << current->data << " -> ";
      current = current->next;
    }
    cout << "nullptr" << endl;
  }

  ~LinkedList() {
    Node *current = head;
    while (current) {
      Node *next = current->next;
      delete current;
      current = next;
    }
  }
};

int main() {
  // Instance is created on the STACK (automatically destroyed when it goes out
  // of scope). No need to worry about memory management (freeing it up)
  LinkedList ll;

  // Instance is created in the HEAP. It will persist until explicitly
  // deallocated
  LinkedList *ll1; // just a placeholder, object itself is not created yet
  LinkedList *ll2 = new LinkedList();

  delete ll2;

  return 0;
}
