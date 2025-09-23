import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

class Main {
  public static void main(String[] args) {
    _new(); // -> Set<E>

    // + Collection methods
  }

  static void _new() {
    // Backed by a bash table - do not guarantee order
    // add, remove, contains: O(1)
    Set<String> hashSet = new HashSet<String>();

    // Maintains insertion order
    Set<String> linkedHashSet = new LinkedHashSet<String>();

    // Implements a sorted set
    // works only for comparable items
    Set<String> treeSet = new TreeSet<String>(); // optionally receives a comparator
  }

}
