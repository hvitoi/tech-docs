import java.util.HashSet; // implementation
import java.util.LinkedHashSet; // implementation
import java.util.Set; // interface
import java.util.TreeSet;

class Main {
  public static void main(String[] args) {
    // Implementations
    SetImplementations.run();

    // Static methods
    SetNew.run();
  }
}

class SetImplementations {
  static void run() {

    /**
     * * Sets do not accept duplicate values
     * * Sets are good for searching (quick and inexpensive)
     */

    // do not guarantee order
    Set<String> hashSet = new HashSet<String>();
    hashSet.add("Henry");

    // guarantee order
    Set<String> linkedHashSet = new LinkedHashSet<String>();
    linkedHashSet.add("Henry");

    // works only for comparable items
    Set<String> treeSet = new TreeSet<String>(); // optionally receives a comparator
    treeSet.add("Henry");

  }
}

class SetNew {
  static void run() {
    Set<String> set = new HashSet<String>();
  }
}
