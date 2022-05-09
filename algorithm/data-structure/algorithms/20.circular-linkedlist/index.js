// --- Directions
//   Given a linked list, return true if the list
//   is circular, false if it is not.
// --- Examples
//   const l = new List();
//   const a = new Node('a');
//   const b = new Node('b');
//   const c = new Node('c');
//   l.head = a;
//   a.next = b;
//   b.next = c;
//   c.next = b;
//   circular(l) // true
module.exports = circular;

// In circular list there's no tail node
function circular(list) {
  let slow = list.head;
  let fast = list.head;

  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true; // If it is circular, at some point in time they will match!
  }

  return false; // Returns false if a tail (fast.next === null) is found
}
