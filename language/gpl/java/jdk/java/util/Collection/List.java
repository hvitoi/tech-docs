import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;

/**
 * Lists accept duplicate values
 * Lists are ordered collections (or sequences)
 * Lists are indexed
 * "List Interface" is implemented by ArrayList, LinkedList and Vector
 * "List Interface" extends the "Collection Interface"
 */

class Main {
  public static void main(String[] args) {
    _new(); // -> List<E>

    // Static methods
    _of(); // -> List<E>

    // Instance methods
    _add(); // -> boolean/void (mut)
    _addAll(); // -> boolean (mut)

    _remove(); // -> E/void (mut)
    _set(); // -> E (mut)
    _replaceAll(); // -> void (mut)

    _sort(); // -> void (mut)

    _get(); // -> E (pure)
    _indexOf(); // -> int (pure)
    _lastIndexOf(); // -> int (pure)
    _subList(); // -> List<E> (pure)

    _listIterator(); // -> ListIterator<E> (pure)

    // + SequencedCollection methods
  }

  static void _new() {
    // ArrayList (backed by an array)
    List<String> list1 = new ArrayList<>();
    var list2 = new ArrayList<String>();
    var list3 = new ArrayList<>(List.of("hey", "there"));

    // LinkedList (doubly-linked list)
    var list4 = new LinkedList<String>();

    // VectorList (manipulate a list across call stacks (thread safe))
    var list5 = new Vector<String>();
  }

  static void _of() {
    // Immutable list
    var items1 = List.of("hey", "there");
    var items2 = List.of(); // empty list
  }

  static void _add() {
    // Method overload on method from Collection: allow insert on a given index
    List<String> items = new ArrayList<>();
    boolean isAdded = items.add("z"); // add to end
    items.add(0, "a"); // add to index
  }

  static void _addAll() {
    // Method overload on method from Collection: allow insert on a given index
    List<String> items = new ArrayList<>();
    boolean isAdded = items.addAll(List.of("c", "d")); // add at first (index 0)
    boolean isAdded2 = items.addAll(0, List.of("a", "b")); // add at index 0
  }

  static void _remove() {
    // Overrides the method from Collection: remove by index (instead of by element)
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));
    String removedElement = items.remove(0); // removes "a" (index 0)
    boolean removedElement2 = items.remove("b"); // removes "b" (behavior from Collection class)
  }

  static void _set() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));
    String oldElement = items.set(0, "z"); // updates index 0
  }

  static void _replaceAll() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));

    // Works like a map
    items.replaceAll(s -> s.toUpperCase());
  }

  static void _sort() {
    var numberList = new ArrayList<>(List.of(3, 1, 2));
    var stringList = new ArrayList<>(List.of("a", "b", "c"));
    var personList = new ArrayList<>(List.of(new Person("Henry", 3), new Person("Albert", 1), new Person("John", 2)));

    /*
     * Sorting (natural order) - Uses the class-defined "compareTo" function
     */
    numberList.sort(null);
    stringList.sort(null);
    personList.sort(null);

    /*
     * Sorting (comparator) - Uses a custom comparator
     */
    personList.sort((p1, p2) -> Integer.compare(p1.age, p2.age)); // lambda-expression comparator
    personList.sort((p1, p2) -> p1.name.compareTo(p2.name)); // lambda-expression comparator
    personList.sort(Comparator.comparing(Person::getAge)); // comparator class (built using the "comparing" helper)
    personList.sort(Comparator.comparing(Person::getName)); // comparator class (built using the "comparing" helper)
    personList.sort(new Comparator<Person>() { // comparator class (built using an anonymous class)
      @Override
      public int compare(Person p1, Person p2) {
        return Integer.compare(p1.age, p2.age); // 0: equal, -1: smaller, +1: bigger
      }
    });

  }

  static void _get() {
    var items = new ArrayList<>(List.of("a", "b", "c"));
    items.get(0); // get element by index

    try {
      String el = items.get(99);
    } catch (IndexOutOfBoundsException e) {
    }
  }

  static void _indexOf() {
    List<String> items = new ArrayList<>(List.of("a", "a", "b", "c"));
    // Get the index of the FIRST appearance
    int i = items.indexOf("a"); // 0
  }

  static void _lastIndexOf() {
    List<String> items = new ArrayList<>(List.of("a", "a", "b", "c"));
    // Get the index of the LAST appearance
    int i = items.lastIndexOf("a"); // 1
  }

  static void _subList() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c", "d", "e"));

    // Extract a chunk of the list, works like a substring
    // The original list is untouched
    List<String> subItems = items.subList(1, 3); // [1,3)
  }

  static void _listIterator() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));
    var it = items.listIterator();
  }

}

class Person implements Comparable<Person> {
  String name;
  int age;

  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public String getName() {
    return name;
  }

  public int getAge() {
    return age;
  }

  @Override
  public int compareTo(Person other) {
    return Integer.compare(this.age, other.age); // 0: equal, -1: smaller, +1: bigger
  }

}
