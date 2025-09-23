import java.util.ArrayList;
import java.util.SequencedCollection;
import java.util.List;

class Main {
  public static void main(String[] args) {
    _new(); // -> SequencedCollection<E>

    // Instance methods
    _reversed(); // -> SequencedCollection<E> (mut)

    _addFirst(); // -> void (mut)
    _addLast(); // -> void (mut)
    _removeFirst(); // -> E (mut)
    _removeLast(); // -> E (mut)

    _getFirst(); // -> E (pure)
    _getLast(); // -> E (pure)

    // + Collection methods
  }

  static void _new() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
  }

  static void _reversed() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    var reversedList = items.reversed();
  }

  static void _addFirst() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.addFirst("z");
  }

  static void _addLast() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.addLast("d");
  }

  static void _removeFirst() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    String removed = items.removeFirst(); // remove and returns "a"
  }

  static void _removeLast() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    String removed = items.removeLast(); // remove and returns "c"
  }

  static void _getFirst() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    String el = items.getFirst(); // Throws if the collection is empty
  }

  static void _getLast() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    String el = items.getLast(); // Throws if the collection is empty
  }

}
