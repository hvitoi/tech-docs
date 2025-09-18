import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _add();
    _addAll();
    _clear();
    _contains();
    _isEmpty();
    _iterator();
    _remove();
    _size();
    _stream();

    // inherited from Iterable
    // _forEach()
  }

  static Collection<String> _new() {
    Collection<String> col = new ArrayList<>();
    col.add("awesome");
    return col;
  }

  static void _add() {
    Collection<String> col = _new();

    col.add("cool"); // add element to end
    // col.add(0, "great"); // Implemented in Lists only
  }

  static void _addAll() {
    Collection<String> col1 = _new();
    Collection<String> col2 = _new();

    col1.addAll(col2); // add a whole list to the list
    // col1.addAll(col2.stream().map(RespostaDto::new).collect(Collectors.toList()));
  }

  static void _clear() {
    Collection<String> col = _new();
    col.clear(); // clear all the elements
  }

  static void _contains() {
    Collection<String> col = _new();

    col.add("abc");
    col.add("abcd");

    /**
     * Contains: Search an element in the array using the method equals for each
     * element in the list. The equals method must be @Override in order to
     * customize the behavior of the comparison. The default implementation of
     * equals compare the references
     *
     */
    // public boolean equals(Object ref)
    col.contains("abc"); // verify if a list contains a single element

  }

  static void _isEmpty() {
    Collection<String> col = _new();
    col.isEmpty(); // true or false
  }

  static void _iterator() {

    Collection<String> col = _new();
    col.add("henry");
    col.add("john");
    col.add("albert");

    /**
     * * Listing with Iterator
     */
    Iterator<String> it = col.iterator(); // must be reset in order to iterate again
    while (it.hasNext()) {
      it.next();
    }

  }

  static void _remove() {
    Collection<String> col = _new();

    col.remove(0); // remove element at index 0
  }

  static void _size() {
    Collection<String> col = _new();
    col.size(); // get size
  }

  static void _stream() {
    Collection<String> col = _new();
    col.stream(); // returns a Stream object
  }
}

class Person {
  private int number;
  private String name;
  private Map<Integer, Person> numberToPerson = new HashMap<>();

  public Person(int number, String name) {
    this.number = number;
    this.name = name;
    this.numberToPerson.put(this.number, this);
  }

  public int getNumber() {
    return number;
  }

  public String getName() {
    return name;
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
    Person other = (Person) obj;
    return this.name.equals(other.name);
  }

}
