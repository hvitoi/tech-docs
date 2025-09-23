import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

/*
 * Sets do not accept duplicate values
 * Sets are good for searching (quick and inexpensive)
 */

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _add();
  }

  static void _new() {
    // do not guarantee order
    Set<String> hashSet = new HashSet<String>();

    // guarantee order
    Set<String> linkedHashSet = new LinkedHashSet<String>();

    // works only for comparable items
    Set<String> treeSet = new TreeSet<String>(); // optionally receives a comparator
  }

  static void _add() {
    Set<String> set = new HashSet<String>();
    set.add("Henry");

  }
}
