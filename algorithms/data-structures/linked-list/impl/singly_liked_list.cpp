#include <cassert>
#include <iostream>
#include <stdexcept>
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

  void to_list_recursive_helper(Node *node, vector<int> &result) const {
    if (!node) {
      return;
    }
    result.push_back(node->data);
    to_list_recursive_helper(node->next, result);
  }

public:
  LinkedList() : head(nullptr) {}

  void print() {
    Node *current = head;
    while (current) {
      cout << current->data << " -> ";
      current = current->next;
    }
    cout << "nullptr" << endl;
  }

  void push_left(int value) {
    Node *new_node = new Node(value, head);
    head = new_node;
  }

  int pop_left() {
    if (!head) {
      throw underflow_error("Empty list");
    }

    Node *new_head = head->next;
    int popped = head->data;
    delete head;
    head = new_head;
    return popped;
  }

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

  int pop_right() {
    // Case 1: List is empty
    if (!head) {
      throw underflow_error("Empty list");
    }

    // Case 2: List has only one element
    if (!head->next) {
      int popped = head->data;
      delete head;
      head = nullptr;
      return popped;
    }

    // Case 3: List has at least 2 elements
    auto current = head;
    while (current->next->next) {
      // move to second-to-last item
      current = current->next;
    }
    int popped = current->next->data; // pop the last item
    delete current->next;
    current->next = nullptr;
    return popped;
  }

  vector<int> to_list() const {
    vector<int> list;

    Node *current = head;
    while (current) {
      list.push_back(current->data);
      current = current->next;
    }

    return list;
  }

  vector<int> to_list_recursive() const {
    vector<int> result{};
    to_list_recursive_helper(head, result);
    return result;
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
  LinkedList ll;

  // Print
  ll.print();

  // Push Right
  ll.push_right(30);
  ll.push_right(40);

  // Push Left
  ll.push_left(20);
  ll.push_left(10);

  // Print
  ll.print();

  // To List
  {
    auto actual = ll.to_list();
    vector<int> expected{10, 20, 30, 40};
    assert(actual == expected);
  }

  // To List (Recursive)
  {
    auto actual = ll.to_list_recursive();
    vector<int> expected{10, 20, 30, 40};
    assert(actual == expected);
  }

  // Pop Left
  {
    auto actual = ll.pop_left();
    auto expected = 10;
    assert(actual == expected);
  }

  // Pop Right
  {
    auto actual = ll.pop_right();
    auto expected = 40;
    // assert(actual == expected);
  }

  // Print
  ll.print();

  return 0;
}
