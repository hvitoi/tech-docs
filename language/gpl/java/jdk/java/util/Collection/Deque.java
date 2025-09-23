import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.NoSuchElementException;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new(); // -> Deque<E>

    // Instance methods
    _offerFirst(); // -> boolean (mut)
    _offerLast(); // -> boolean (mut)

    _pollFirst(); // -> E (mut)
    _pollLast(); // -> E (mut)
    _pop(); // -> E (mut)

    _peekFirst(); // -> E (pure)
    _peekLast(); // -> E (pure)

    _descendingIterator(); // -> Iterator<E> (pure)

    // + Queue methods
  }

  static void _new() {
    Deque<String> deque1 = new ArrayDeque<>();
    Deque<String> deque2 = new ArrayDeque<>(List.of("a", "b", "c"));
  }

  static void _offerFirst() {
    Deque<String> deque = new ArrayDeque<>();
    // Insert at the front, respect the capacity
    deque.offerFirst("a");
  }

  static void _offerLast() {
    Deque<String> deque = new ArrayDeque<>();
    // Insert at the front, respect the capacity
    deque.offerLast("a");
  }

  static void _pollFirst() {
    Deque<String> deque = new ArrayDeque<>(List.of("a", "b", "c"));

    // returns null is deque is empty
    String el = deque.pollFirst();
  }

  static void _pollLast() {
    Deque<String> deque = new ArrayDeque<>(List.of("a", "b", "c"));

    // returns null is deque is empty
    String el = deque.pollLast();
  }

  static void _pop() {
    Deque<String> deque = new ArrayDeque<>(List.of("a", "b", "c"));

    try {
      String el = deque.pop(); // remove first element
    } catch (NoSuchElementException e) {
      // deque is empty...
      e.printStackTrace();
    }
  }

  static void _peekFirst() {
    Deque<String> deque = new ArrayDeque<>(List.of("a", "b", "c"));
    String el = deque.peekFirst(); // a
  }

  static void _peekLast() {
    Deque<String> deque = new ArrayDeque<>(List.of("a", "b", "c"));
    String el = deque.peekLast(); // c
  }

  static void _descendingIterator() {
    Deque<String> deque = new ArrayDeque<>();
    // iterator from tail to head
    var it = deque.descendingIterator();
  }

}
