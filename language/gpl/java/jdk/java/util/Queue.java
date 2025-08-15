import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
  public static void main(String[] args) {
    // Implementations
    implementations();

    // Static methods
    _new();

    // Instance methods
    add();
    addAll();
    peek();
  }

  static void implementations() {
    Queue<String> queue = new LinkedList<>();
  }

  static Queue _new() {
    Queue<String> queue = new LinkedList<>();
    return queue;
  }

  static void add() {
    Queue<String> queue = QueueNew.run();
    queue.add("a");
  }

  static void addAll() {
    Queue<String> queue = QueueNew.run();
    queue.addAll(Arrays.asList("a", "b", "c"));
  }

  static void peek() {
    Queue<String> queue = QueueNew.run();
    queue.add("a");

    String peeked = queue.peek(); // peek first element without poping
  }
}
