import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Main {
  public static void main(String[] args) {
    // Static methods
    _emptySet();
    _nCopies();
    _reverse();
    _shuffle();
    _singletonList();
    _sort();
    _swap();
    _unmodifiableList();
    _unmodifiableSet();
  }

  static void _emptySet() {
    // create unmodified empty set
    Set<String> set = Collections.emptySet();
  }

  static void _nCopies() {
    // Array with size 1000 with nulls
    List<String> list = Collections.nCopies(1000, null);
  }

  static void _reverse() {
    List<Integer> list = Arrays.asList(3, -3, 2);
    Collections.reverse(list);
  }

  static void _shuffle() {
    List<Integer> list = Arrays.asList(3, -3, 2);
    Collections.shuffle(list);
  }

  static void _singletonList() {
    Collections.singletonList("hey"); // List with a single immutable element
  }

  static void _sort() {
    var numberList = Arrays.asList(3, -3, 2);
    var stringList = Arrays.asList("hey", "12", "awesome");
    var objectList = Arrays.asList(new Person(5, "Henry"), new Person(9, "Albert"), new Person(4, "John"));

    /**
     * * sort() - natural order
     */
    Collections.sort(numberList); // built-in "compareTo"
    Collections.sort(stringList); // built-in "compareTo"
    Collections.sort(objectList); // overridden "compareTo"

    /**
     * * sort() - comparator
     */

    Collections.sort(objectList, new PersonComparator());

    Collections.sort(objectList, (p1, p2) -> Integer.compare(p1.number, p2.number));
    Collections.sort(objectList, (p1, p2) -> p1.name.compareTo(p2.name));

    Collections.sort(objectList, Comparator.comparing(Person::getNumber));
    Collections.sort(objectList, Comparator.comparing(Person::getName));

  }

  static void _swap() {
    List<Integer> list = Arrays.asList(3, -3, 2);

    Collections.swap(list, 0, 2); // change value from index 0 to index 2
  }

  static void _unmodifiableList() {
    List<Integer> list = Arrays.asList(3, -3, 2);

    Collections.unmodifiableList(list); // return a new reference to a list that is unmodifiable
  }

  static void _unmodifiableSet() {
    Set<Integer> numberSet = new HashSet<>();
    numberSet.add(5);
    numberSet.add(-3);
    numberSet.add(2);

    Collections.unmodifiableSet(numberSet); // return a new reference to a Set that is unmodifiable
  }
}

class Person implements Comparable<Person> {
  int number;
  String name;

  public Person(int number, String name) {
    this.number = number;
    this.name = name;
  }

  public int getNumber() {
    return number;
  }

  public String getName() {
    return name;
  }

  @Override
  public int compareTo(Person other) {
    return Integer.compare(this.number, other.number); // 0: equal, -1: smaller, +1: bigger
  }

}

class PersonComparator implements Comparator<Person> {

  @Override
  public int compare(Person p1, Person p2) {
    return Integer.compare(p1.number, p2.number); // 0: equal, -1: smaller, +1: bigger
  }

}
