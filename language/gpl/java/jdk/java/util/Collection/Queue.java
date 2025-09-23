import java.util.LinkedList;
import java.util.List;
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

  static void _new() {
    Queue<String> queue = new LinkedList<>();
  }

  static void _add() {
    Queue<String> queue = new LinkedList<>();
    queue.add("a");
  }

  static void _addAll() {
    Queue<String> queue = new LinkedList<>();
    queue.addAll(List.of("a", "b", "c"));
  }

  static void _peek() {
    Queue<String> queue = new LinkedList<>();
    queue.add("a");
    String peeked = queue.peek(); // peek first element without popping it
  }
}
