import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _add();
    _addAll();
    _peek();
  }

  static Queue<String> _new() {
    Queue<String> queue = new LinkedList<>();
    return queue;
  }

  static void _add() {
    Queue<String> queue = _new();
    queue.add("a");
  }

  static void _addAll() {
    Queue<String> queue = _new();
    queue.addAll(Arrays.asList("a", "b", "c"));
  }

  static void _peek() {
    Queue<String> queue = _new();
    queue.add("a");
    String peeked = queue.peek(); // peek first element without poping
  }
}
