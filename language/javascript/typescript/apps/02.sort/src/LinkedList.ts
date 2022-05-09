import { Sorter } from './Sorter';

class Node {
  next: Node | null = null;
  constructor(public data: number) {}
}

export class LinkedList extends Sorter {
  head: Node | null = null;

  add(data: number): void {
    const new_node = new Node(data);

    // If there is no head ...
    if (!this.head) {
      this.head = new_node;
      return;
    }

    // Go to the last node
    let node = this.head;
    while (node.next) {
      node = node.next;
    }

    // Assign a next value to the last node
    node.next = new_node;
  }

  get length(): number {
    let size = 0;
    let node: Node | null = this.head;
    while (node) {
      size++;
      node = node.next;
    }
    return size;
  }

  at(index: number): Node {
    // Out of bounds index
    if (index < 0 || index >= this.length)
      throw new Error('Index out of bounds');
    if (!this.head) throw new Error('Linked list is empty.');

    // Go to the position 'index' and return the node
    let node: Node | null = this.head;
    let counter = 0;
    while (node) {
      if (counter === index && node) return node;
      node = node.next;
      counter++;
    }

    // If no index is found at all
    throw new Error('Index not found');
  }

  compare(leftIndex: number, rightIndex: number): boolean {
    // Out of bound index
    if (
      leftIndex < 0 ||
      leftIndex >= this.length ||
      rightIndex < 0 ||
      rightIndex >= this.length
    ) {
      throw new Error('Index out of bounds');
    }
    // No head
    if (!this.head) throw new Error('Linked list is empty.');

    // return the comparison
    return this.at(leftIndex).data > this.at(rightIndex).data;
  }

  swap(leftIndex: number, rightIndex: number): void {
    // Get nodes
    const leftNode = this.at(leftIndex);
    const rightNode = this.at(rightIndex);

    // Swap values of the nodes
    const aux = leftNode.data;
    leftNode.data = rightNode.data;
    rightNode.data = aux;
  }

  print(): void {
    if (!this.head) return;
    let node: Node | null = this.head;
    while (node) {
      console.log(node.data);
      node = node.next;
    }
  }
}
