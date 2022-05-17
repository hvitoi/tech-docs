import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.function.Consumer;

class Main {
  public static void main(String[] args) {

    // Static methods
    CollectionNew.run();

    // Instance methods
    CollectionAdd.run();
    CollectionAddAll.run();
    CollectionClear.run();
    CollectionContains.run();
    CollectionIsEmpty.run();
    CollectionIterator.run();
    CollectionRemove.run();
    CollectionSize.run();
    CollectionStream.run();
    // CollectionForEach.run(); // Inherited from Iterable
  }
}

class CollectionNew {
  static Collection run() {
    Collection<String> col = new ArrayList<>();
    col.add("awesome");
    return col;
  }
}

class CollectionAdd {
  static void run() {
    Collection<String> col = CollectionNew.run();

    col.add("cool"); // add element to end
    // col.add(0, "great"); // Implemented in Lists only

  }
}

class CollectionAddAll {
  static void run() {
    Collection<String> col1 = CollectionNew.run();
    Collection<String> col2 = CollectionNew.run();

    col1.addAll(col2); // add a whole list to the list
    // col1.addAll(col2.stream().map(RespostaDto::new).collect(Collectors.toList()));
  }
}

class CollectionClear {
  static void run() {
    Collection<String> col = CollectionNew.run();
    col.clear(); // clear all the elements
  }
}

class CollectionContains {
  static void run() {
    Collection<String> col = CollectionNew.run();

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
}

class CollectionIsEmpty {
  static void run() {
    Collection<String> col = CollectionNew.run();
    col.isEmpty(); // true or false
  }
}

class CollectionIterator {
  static void run() {

    Collection<String> col = CollectionNew.run();
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
}

class CollectionRemove {
  static void run() {
    Collection<String> col = CollectionNew.run();

    col.remove(0); // remove element at index 0
  }
}

class CollectionSize {
  static void run() {
    Collection<String> col = CollectionNew.run();
    col.size(); // get size
  }
}

class CollectionStream {
  static void run() {
    Collection<String> col = CollectionNew.run();
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
