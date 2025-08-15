#include <stdio.h>
#include <stdlib.h>

// In functions you can pass the elements by reference or by value
// By reference means you will be manipulating the original element
// By value means the element is duplicated

void hey(char name[]) {
  printf("hey, %s!", name);
  printf("Welcome!");
}

int square(double x) { return x * x; }

typedef struct {
  int data;
  struct Node *left;
  struct Node *right;
} Node;

Node *createNode(int data) {
  Node *newNode = (Node *)malloc(sizeof(Node));
  if (newNode == NULL) {
    printf("Memory allocation failed!\n");
    exit(1);
  }
  newNode->data = data;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

int main() {
  hey("John");
  return 0;
}
