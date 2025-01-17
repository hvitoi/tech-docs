#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
  int data;
  Node *next;

  Node(int value) : data(value), next(nullptr) {}
  Node(int value, Node *node) : data(value), next(node) {}
};

class LinkedList {
private:
  Node *head;

public:
  LinkedList() : head(nullptr) {}

  void push_left(int value) {
    Node *new_node = new Node(value, head);
    head = new_node;
  }

  // Add node to the end of the list
  void push_right(int value) {
    Node *new_node = new Node(value);

    if (!head) {
      head = new_node;
      return;
    }

    Node *current = head;
    while (current->next) {
      current = current->next;
    }
    current->next = new_node;
  }

  // Convert LinkedList to a vector
  vector<int> toList() {
    vector<int> list;

    Node *current = head;
    while (current) {
      list.push_back(current->data);
      current = current->next;
    }

    return list;
  }

  void print() {
    Node *current = head;
    while (current) {
      cout << current->data << " -> ";
      current = current->next;
    }
    cout << "nullptr" << endl;
  }

  // Destructor to free allocated memory
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
  LinkedList ll;
  ll.push_right(10);
  ll.push_right(20);
  ll.push_right(30);

  // Print
  ll.print();

  // To List
  auto actual = ll.toList();
  vector<int> expected{10, 20, 30};
  assert(actual == expected);

  return 0;
}
