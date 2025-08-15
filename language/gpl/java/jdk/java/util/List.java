import java.util.ArrayList; // implementation
import java.util.Comparator;
import java.util.LinkedList; // implementation
import java.util.List; // interface
import java.util.Vector; // implementation
import java.util.function.Consumer;

class Main {
  public static void main(String[] args) {

    // Implementations
    implementations();

    // Static methods
    _new();

    // Instance methods
    add();
    get();
    remove();
    sort();
  }

  static void implementations() {

    /**
     * * Lists accept duplicate values
     * * Lists are ordered collections (or sequences)
     * * Lists are indexed
     * * "List Interface" is implemented by ArrayList, LinkedList and Vector
     * * "List Interface" extends the "Collection Interface"
     */

    // ArrayList (good to iterate, bad to modify)
    List<String> arrayList = new ArrayList<>();

    // LinkedList (good to modify, bad to iterate)
    List<String> linkedList = new LinkedList<>();

    // VectorList (manipulate a list across call stacks (thread safe))
    List<String> vectorList = new Vector<>();

  }

  static List _new() {

    List<String> list1 = new ArrayList<>(); // empty list
    List<String> list2 = new ArrayList<>(5, 1, -3); // initial size 1, but it can be expanded
    List<String> list3 = new ArrayList<>(list2); // new list with initial values from another list

    return list2;
  }

  static void add() {
    List list = ListNew.run();
    list.add("hey");
  }

  static void get() {
    List list = ListNew.run();
    list.get(0); // get element by index
  }

  static void remove() {
    List list = ListNew.run();
    list.remove(0); // remove by index
  }

  static void sort() {

    List<Integer> numberList = new ArrayList<>();
    numberList.add(5);
    numberList.add(-3);
    numberList.add(2);

    List<String> stringList = new ArrayList<>();
    stringList.add("hey");
    stringList.add("12");
    stringList.add("awesome");

    List<Person> personList = new ArrayList<>();
    personList.add(new Person(5, "Henry"));
    personList.add(new Person(9, "Albert"));
    personList.add(new Person(4, "John"));

    /**
     * * Sorting (natural order)
     */
    numberList.sort(null); // built-in compareTo
    stringList.sort(null); // built-in compareTo
    personList.sort(null); // user-defined compareTo

    /**
     * * Sorting (comparator)
     */
    personList.sort(new PersonComparator()); // sorts using comparator

    personList.sort((p1, p2) -> Integer.compare(p1.number, p2.number)); // lambda-expression comparator
    personList.sort((p1, p2) -> p1.name.compareTo(p2.name)); // lambda-expression comparator

    personList.sort(Comparator.comparing(Person::getNumber));
    personList.sort(Comparator.comparing(Person::getName));

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

  // For Sorting
  @Override
  public int compareTo(Person other) {
    return Integer.compare(this.number, other.number); // 0: equal, -1: smaller, +1: bigger
  }

  // For Searching
  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((name == null) ? 0 : name.hashCode());
    result = prime * result + number;
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
    if (number != other.number)
      return false;
    return true;
  }

}

class PersonComparator implements Comparator<Person> {

  @Override
  public int compare(Person p1, Person p2) {
    return Integer.compare(p1.number, p2.number); // 0: equal, -1: smaller, +1: bigger
  }

}

class PersonConsumer implements Consumer<Person> {

  @Override
  public void accept(Person p) {
    System.out.println("Person number: " + p.number + ". Person name:" + p.name);
  }

}
