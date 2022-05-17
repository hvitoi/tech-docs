import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {
  public static void main(String[] args) {
    // Implementations
    QueueImplementations.run();

    // Static methods
    QueueNew.run();

    // Instance methods
    QueueAdd.run();
    QueueAddAll.run();
    QueuePeek.run();
  }
}

class QueueImplementations {
  static void run() {
    Queue<String> queue = new LinkedList<>();
  }
}

class QueueNew {
  static Queue run() {
    Queue<String> queue = new LinkedList<>();
    return queue;
  }
}

class QueueAdd {
  static void run() {
    Queue<String> queue = QueueNew.run();
    queue.add("a");
  }
}

class QueueAddAll {
  static void run() {
    Queue<String> queue = QueueNew.run();
    queue.addAll(Arrays.asList("a", "b", "c"));
  }
}

class QueuePeek {
  static void run() {
    Queue<String> queue = QueueNew.run();
    queue.add("a");

    String peeked = queue.peek(); // peek first element without poping
  }
}
