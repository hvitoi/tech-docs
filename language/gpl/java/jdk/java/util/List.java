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

    // Static methods
    _new();
    _of();

    // Instance methods
    _add(); // mut
    _addAll(); // mut
    _remove(); // mut
    _set(); // mut
    _replaceAll(); // mut
    _sort(); // mut

    _get(); // pure
    _indexOf(); // pure
    _lastIndexOf(); // pure
    _subList(); // pure

    // + SequencedCollection methods
    // + Collections methods
    // + Iterable methods
  }

  static void _new() {
    // ArrayList (good to iterate, bad to modify)
    List<String> list1 = new ArrayList<>();
    var list2 = new ArrayList<String>();
    var list3 = new ArrayList<>(List.of("hey", "there"));

    // LinkedList (good to modify, bad to iterate)
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
    items.add("z"); // add to end
    items.add(0, "a"); // add to index
  }

  static void _addAll() {
    // Method overload on method from Collection: allow insert on a given index
    List<String> items = new ArrayList<>();
    items.addAll(0, List.of("a", "b")); // add at index 0
  }

  static void _remove() {
    // Overrides the method from Collection: remove by index (instead of by element)
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.remove(0); // removes "a"
  }

  static void _set() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.set(0, "z"); // updates index 0
  }

  static void _replaceAll() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.replaceAll(s -> s.toUpperCase());
    // Works like a map
  }

  static void _sort() {
    var numberList = new ArrayList<>(List.of(3, 1, 2));
    var stringList = new ArrayList<>(List.of("a", "b", "c"));
    var personList = new ArrayList<>(List.of(new Person("Henry", 5), new Person("Albert", 9), new Person("John", 4)));

    /**
     * * Sorting (natural order)
     */
    numberList.sort(null); // built-in compareTo
    stringList.sort(null); // built-in compareTo
    personList.sort(null); // user-defined compareTo

    /**
     * * Sorting (comparator)
     */
    personList.sort((p1, p2) -> Integer.compare(p1.age, p2.age)); // lambda-expression comparator
    personList.sort((p1, p2) -> p1.name.compareTo(p2.name)); // lambda-expression comparator
    personList.sort(Comparator.comparing(Person::getAge));
    personList.sort(Comparator.comparing(Person::getName));
    personList.sort(new PersonComparator()); // comparator class (legacy)

  }

  static void _get() {
    var items = new ArrayList<>(List.of("a", "b", "c"));
    items.get(0); // get element by index

    try {
      items.get(99);
    } catch (IndexOutOfBoundsException e) {
    }
  }

  static void _indexOf() {
    List<String> items = new ArrayList<>(List.of("a", "a", "b", "c"));
    // Get the index of the FIRST appearance
    items.indexOf("a"); // 0
  }

  static void _lastIndexOf() {
    List<String> items = new ArrayList<>(List.of("a", "a", "b", "c"));
    // Get the index of the LAST appearance
    items.lastIndexOf("a"); // 1
  }

  static void _subList() {
    List<String> items = new ArrayList<>(List.of("a", "b", "c", "d", "e"));

    // Extract a chunk of the list
    // The original list is untouched
    var sub = items.subList(1, 3); // [1,3)
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

  // For Sorting
  @Override
  public int compareTo(Person other) {
    return Integer.compare(this.age, other.age); // 0: equal, -1: smaller, +1: bigger
  }

  // For Searching
  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((name == null) ? 0 : name.hashCode());
    result = prime * result + age;
    return result;
  }

  // For Searching
  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Person other = (Person) obj;
    if (name == null) {
      if (other.name != null)
        return false;
    } else if (!name.equals(other.name))
      return false;
    if (age != other.age)
      return false;
    return true;
  }

}

class PersonComparator implements Comparator<Person> {
  @Override
  public int compare(Person p1, Person p2) {
    return Integer.compare(p1.age, p2.age); // 0: equal, -1: smaller, +1: bigger
  }
}
