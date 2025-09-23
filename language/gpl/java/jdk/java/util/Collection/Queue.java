import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new(); // -> Queue<E>

    // Instance methods
    _offer(); // -> boolean (mut)

    _poll(); // -> E (mut)
    _remove(); // -> E (mut)

    _peek(); // -> E (pure)
    _element(); // -> E (pure)

    // + Collection methods
  }

  static void _new() {
    Queue<String> queue = new LinkedList<>();
  }

  static void _offer() {
    Queue<String> queue = new LinkedList<>();
    // Same as add, but fail to insert if the capacity has been reached
    queue.offer("a");
  }

  static void _poll() {
    Queue<String> queue = new LinkedList<>(List.of("a", "b", "c"));
    // get the first element in the queue
    var el = queue.poll();
  }

  static void _remove() {
    Queue<String> queue = new LinkedList<>(List.of("a", "b", "c"));
    // same as pool, but throws if the queue is empty
    var el = queue.remove();
  }

  static void _peek() {
    Queue<String> queue = new LinkedList<>(List.of("a"));
    // peek first element without popping it
    String peeked = queue.peek();
  }

  static void _element() {
    Queue<String> queue = new LinkedList<>(List.of("a"));
    // same as peek, but throws if the queue is empty
    String peeked = queue.element();
  }
}
