// --- Directions
//   Given a linked list and integer n, return the element n
//   spaces from the last node in the list.  Do not call the
//   'size' method of the linked list.  Assume that n will always
//   be less than the length of the list.
// --- Examples
//   const list = new List();
//   list.insertLast('a');
//   list.insertLast('b');
//   list.insertLast('c');
//   list.insertLast('d');
//   fromLast(list, 2).data // 'b'
module.exports = fromLast;

function fromLast(list, n) {
  if (n >= 0 && n > list.size() - 1) return null; // n out of bounds

  let slow = list.head;
  let fast = list.head;

  // Move the 'fast' to the n position
  for (i = 0; i < n; i++) fast = fast.next;

  // Move both nodes at same time
  while (fast.next) {
    fast = fast.next;
    slow = slow.next;
  }
  return slow;
}
