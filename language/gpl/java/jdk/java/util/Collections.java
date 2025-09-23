import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Main {
  public static void main(String[] args) {
    // Static methods
    _emptySet(); // -> Set
    _emptyList(); // -> List
    _singletonList(); // -> List
    _nCopies(); // -> List
    _unmodifiableList(); // -> List
    _unmodifiableSet(); // -> Set

    _sort(); // mut (List)
    _reverse(); // mut (List)
    _shuffle(); // mut (List)
    _swap(); // mut (List)

  }

  static void _emptySet() {
    // create unmodified empty set
    var set = Collections.<String>emptySet();
  }

  static void _emptyList() {
    var list = Collections.<String>emptyList();
  }

  static void _singletonList() {
    // List with a single immutable element
    var list = Collections.singletonList("hey");
  }

  static void _nCopies() {
    // Array with size 20 with "hey"
    var list = Collections.nCopies(20, "hey");
  }

  static void _unmodifiableList() {
    var list = new ArrayList<>(List.of("a", "b", "c"));
    // return a new reference to a list that is unmodifiable
    var unmodifiable = Collections.unmodifiableList(list);
  }

  static void _unmodifiableSet() {
    var set = new HashSet<String>(Set.of("a", "b", "c"));
    // return a new reference to a Set that is unmodifiable
    var unmodifiable = Collections.unmodifiableSet(set);
  }

  static void _sort() {
    var numberList = new ArrayList<>(List.of(3, 1, 2));
    var stringList = new ArrayList<>(List.of("a", "b", "c"));
    var personList = new ArrayList<>(List.of(new Person("Henry", 3), new Person("Albert", 1), new Person("John", 2)));

    /*
     * Sorting (natural order) - Uses the class-defined "compareTo" function
     */
    Collections.sort(numberList); // built-in "compareTo"
    Collections.sort(stringList); // built-in "compareTo"
    Collections.sort(personList); // overridden "compareTo"

    /*
     * Sorting (comparator) - Uses a custom comparator
     */
    Collections.sort(personList, (p1, p2) -> Integer.compare(p1.age, p2.age));
    Collections.sort(personList, (p1, p2) -> p1.name.compareTo(p2.name));
    Collections.sort(personList, Comparator.comparing(Person::getName));

  }

  static void _reverse() {
    var list = new ArrayList<>(List.of(3, 2, 1));
    Collections.reverse(list);
  }

  static void _shuffle() {
    var list = new ArrayList<>(List.of(3, 2, 1));
    Collections.shuffle(list);
  }

  static void _swap() {
    var list = new ArrayList<>(List.of("a", "b", "c"));
    Collections.swap(list, 0, 2); // change value from index 0 to index 2
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
