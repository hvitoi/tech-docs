import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    /**
     * Sets do not accept duplicate values
     * Sets are good for searching (quick and inexpensive)
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
