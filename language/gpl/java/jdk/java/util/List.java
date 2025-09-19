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
    _get();
    _add();
    _remove();
    _sort();
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
    var items = List.of("hey", "there");
  }

  static void _get() {
    var items = new ArrayList<>(List.of("a", "b", "c"));
    items.get(0); // get element by index

    try {
      items.get(99);
    } catch (IndexOutOfBoundsException e) {
    }
  }

  static void _add() {
    var items = new ArrayList<String>();
    items.add("a");
  }

  static void _remove() {
    var list = new ArrayList<>(List.of("a", "b", "c"));
    list.remove(0); // remove by index
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
