import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

class Main {
  public static void main(String[] args) {
    _new(); // -> Collection<E>

    // Instance methods
    _add(); // -> boolean (mut)
    _addAll(); // -> boolean (mut)

    _remove(); // -> boolean (mut)
    _removeAll(); // -> boolean (mut)
    _removeIf(); // -> boolean (mut)
    _retainAll(); // -> boolean (mut)
    _clear(); // -> void (mut)

    _isEmpty(); // -> boolean (pure)
    _contains(); // -> boolean (pure)
    _containsAll(); // -> boolean (pure)

    _size(); // -> int (pure)

    _stream(); // -> Stream<E> (pure)
    _parallelStream(); // -> Stream<E> (pure)
    _spliterator(); // -> Spliterator<E> (pure)

    // + Iterable methods
  }

  static void _new() {
    Collection<String> items = new ArrayList<>(List.of("a", "b", "c"));
  }

  static void _add() {
    Collection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    boolean isAdded = items.add("d"); // Where it is added depends on the implementation
    // items.add(0, "z"); // Implemented in Lists only
  }

  static void _addAll() {
    Collection<String> items = new ArrayList<>(List.of("a", "b", "c"));

    // add a whole list to the list
    boolean isAdded = items.addAll(List.of("d", "e"));
  }

  static void _remove() {
    Collection<String> items = new ArrayList<>(List.of("a", "a", "b"));

    // removes the FIRST element with a given value
    // if the element does not exist, simply remove nothing
    boolean isRemoved = items.remove("a"); // [a, b]
  }

  static void _removeAll() {
    Collection<String> items = new ArrayList<>(List.of("a", "a", "b", "b", "c"));

    // removes ALL elements with a given value
    boolean isRemoved = items.removeAll(List.of("a", "b")); // [c]
  }

  static void _removeIf() {
    Collection<Integer> items = new ArrayList<>(List.of(1, 2, 3, 4));
    items.removeIf((num) -> num % 2 == 0); // remove even numbers
  }

  static void _retainAll() {
    Collection<String> items = new ArrayList<>(List.of("a", "a", "b", "b", "c"));

    // "Intersection". And also retain also duplicates
    boolean ok = items.retainAll(List.of("a", "c"));
  }

  static void _clear() {
    Collection<String> items = new ArrayList<>(List.of("a", "b", "c"));

    // removes all the elements from the list
    items.clear();
  }

  static void _isEmpty() {
    Collection<String> items = List.of();
    boolean res = items.isEmpty(); // true
  }

  static void _contains() {
    Collection<String> items = List.of("a", "b", "c");
    boolean res = items.contains("a"); // true
  }

  static void _containsAll() {
    Collection<String> items = List.of("a", "b", "c");
    items.containsAll(List.of("a")); // true
    items.containsAll(List.of("a", "a")); // true
    items.containsAll(List.of("a", "b", "c", "z")); // false
  }

  static void _size() {
    Collection<String> col = List.of("a", "b", "c");
    int size = col.size();
  }

  static void _stream() {
    Collection<String> items = List.of("a", "b", "c");
    var stream = items.stream();
  }

  static void _parallelStream() {
    Collection<String> items = List.of("a", "b", "c");
    var stream = items.parallelStream();
  }

  static void _spliterator() {
    Collection<String> items = List.of("a", "b", "c");
    var s = items.spliterator();
  }
}
