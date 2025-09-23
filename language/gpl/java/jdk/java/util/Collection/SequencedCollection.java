import java.util.ArrayList;
import java.util.SequencedCollection;
import java.util.List;

class Main {
  public static void main(String[] args) {

    // Static methods
    _new();

    // Instance methods
    _reversed(); // mut
    _addFirst(); // mut
    _addLast(); // mut
    _removeFirst(); // mut
    _removeLast(); // mut

    _getFirst(); // pure
    _getLast(); // pure

    // + Collections methods
    // + Iterable methods
  }

  static void _new() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
  }

  static void _reversed() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.reversed();
  }

  static void _addFirst() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.addFirst(".");
  }

  static void _addLast() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.addLast("d");
  }

  static void _getFirst() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.getFirst(); // Throws if the collection is empty
  }

  static void _getLast() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.getLast(); // Throws if the collection is empty
  }

  static void _removeFirst() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.removeFirst(); // remove and returns "a"
  }

  static void _removeLast() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.removeLast(); // remove and returns "c"
  }

}
